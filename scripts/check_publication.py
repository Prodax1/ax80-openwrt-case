#!/usr/bin/env python3
"""Local-only, value-silent publication checks using Python and git grep."""
import argparse
import ipaddress
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
RULES = {
    'IPv4': r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])',
    'MAC': r'(?i)\b(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}\b',
    'private-key': r'-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----',
    'token': r'(?i)(?:gh[pousr]_[a-z0-9]{20,}|github_pat_[a-z0-9_]{20,}|tskey-[a-z]+-[a-z0-9-]{12,})',
    'host-fingerprint': r'SHA256:[A-Za-z0-9+/]{40,}={0,2}',
    'UUID': r'(?i)\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b',
    'credential-value': r'''(?im)^\s*(?:[+]|[-])?\s*(?:option\s+)?(?:password|passwd|psk|ssid|secret|token|authkey|api_key|serial|hwid)\s*(?:=|:)\s*["']?[A-Za-z0-9/+][^\n]{5,}''',
    'UCI-value': r'''(?im)^\s*(?:[+]|[-])?\s*option\s+(?:ssid|key|password)\s+["'][^"'\n]+["']''',
    'key-constant': r'(?im)^\s*(?:KEY|IV)\s*=\s*bytes\.fromhex\(',
    'control-character': r'[\x00-\x08\x0b\x0c\x0e-\x1f]',
    'private-path': r'(?i)(?:[A-Z]:[\\/](?:Users|GhostNet)|/h[o]me/[^/\s]+/|/m[n]t/[a-z]/)',
}
FORBIDDEN = {'.bin','.img','.itb','.fip','.ubi','.tgz','.gz','.tar','.zip','.7z','.key','.pem','.bundle','.jpg','.png'}
PUBLIC_DOMAINS = {'github.com','openwrt.org','forum.openwrt.org','ftp.denx.de',
                  'git.openwrt.org','downloads.openwrt.org','git.kernel.org',
                  'gitlab.com','sources.openwrt.org','example.org','x.example.org'}
GREP_PATTERN = r'([0-9]{1,3}\.){3}[0-9]{1,3}|([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}|gh[pousr]_[[:alnum:]]{20,}|github_pat_[[:alnum:]_]{20,}|tskey-[[:alpha:]]+-[[:alnum:]-]{12,}|BEGIN (OPENSSH |RSA |EC )?PRIVATE KEY'

def git(*args, cwd=ROOT):
    return subprocess.run(['git', *args], cwd=cwd, capture_output=True)

def findings(text):
    hits = [name for name, pattern in RULES.items() if re.search(pattern, text)]
    for raw in re.findall(r'(?i)(?<!\w)(?:[0-9a-f]{0,4}:){2,}[0-9a-f:]{0,39}(?!\w)',text):
        try:
            if ipaddress.ip_address(raw).version == 6:
                hits.append('IPv6')
                break
        except ValueError:
            pass
    for domain in re.findall(r'https?://(?:[^/@\s]+@)?([^/:\s<>"\']+)',text):
        if domain.lower() not in PUBLIC_DOMAINS and not domain.startswith('<'):
            hits.append('unapproved-domain')
    # Also catch bare real infrastructure-looking domains, without requiring a URL.
    if re.search(r'(?i)\b[\w.-]*ghostnet[\w.-]*\.(?:ru|com|net|org|io|dev|app|cloud)\b', text):
        hits.append('infrastructure-domain')
    return sorted(set(hits))

def self_test():
    fixtures = {
        'IPv4': '.'.join(map(str,[198,51,100,77])),
        'MAC': ':'.join(['ab','cd','ef','12','34','56']),
        'private-key': '-----BEGIN ' + 'OPENSSH PRIVATE KEY-----',
        'token': 'gh' + 'p_' + 'x'*25,
        'host-fingerprint': 'SHA256:' + 'A'*43,
        'UUID': '-'.join(['a'*8,'b'*4,'c'*4,'d'*4,'e'*12]),
        'credential-value': 'password' + '=' + 'fixture-value',
        'UCI-value': 'option ' + 'ssid ' + "'fixture-wifi'",
        'key-constant': 'KEY ' + '= bytes.fromhex(' + "'aa')",
        'control-character': chr(8),
        'private-path': '/' + 'home/example/work',
        'IPv6': ':'.join(['fd00','','1234']),
        'unapproved-domain': 'https://' + 'private.invalid/path',
        'infrastructure-domain': 'panel.' + 'ghostnet' + '.ru',
    }
    for category, fixture in fixtures.items():
        assert category in findings(fixture), category
    assert findings('Linux 6.18.26; CONFIG_PACKAGE_wpad=y; sha256=' + 'a'*64) == []
    with tempfile.TemporaryDirectory(prefix='ax80-public-check-') as folder:
        path = Path(folder)
        assert git('init','--quiet',cwd=path).returncode == 0
        (path/'fixture.txt').write_text(fixtures['IPv4'] + '\n' + fixtures['token'])
        assert git('add','fixture.txt',cwd=path).returncode == 0
        control = git('grep','--cached','-I','-l','-E',GREP_PATTERN,cwd=path)
        assert control.returncode == 0 and control.stdout.strip() == b'fixture.txt'
        (path/'fixture.txt').write_text('clean control\n')
        assert git('add','fixture.txt',cwd=path).returncode == 0
        clean = git('grep','--cached','-I','-l','-E',GREP_PATTERN,cwd=path)
        assert clean.returncode == 1 and not clean.stdout
    return len(fixtures)

def scan():
    issues, inventory = [], []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or '.git' in path.relative_to(ROOT).parts or '__pycache__' in path.parts:
            continue
        name = path.relative_to(ROOT).as_posix()
        if path.name == '.git':
            continue
        data = path.read_bytes()
        categories = []
        if path.suffix.lower() in FORBIDDEN:
            categories.append('forbidden-artifact')
        try:
            categories += findings(data.decode('utf-8-sig'))
        except UnicodeDecodeError:
            categories.append('non-text-file')
        inventory.append({'file':name,'bytes':len(data),'result':'PASS' if not categories else 'FAIL'})
        if categories:
            issues.append({'file':name,'categories':sorted(set(categories))})
    staged = git('grep','--cached','-I','-l','-E',GREP_PATTERN)
    if staged.returncode not in (0,1):
        issues.append({'file':'<git-index>','categories':['git-grep-unavailable']})
    elif staged.returncode == 0:
        issues += [{'file':name,'categories':['git-grep']} for name in staged.stdout.decode().splitlines()]
    # Inspect every reachable blob, including baseline and other local branches.
    objects = git('rev-list','--objects','--all')
    assert objects.returncode == 0
    blobs = 0
    for row in objects.stdout.decode().splitlines():
        oid = row.split(' ',1)[0]
        kind = git('cat-file','-t',oid)
        if kind.stdout.strip() != b'blob':
            continue
        blobs += 1
        data = git('cat-file','blob',oid).stdout
        try:
            categories = findings(data.decode('utf-8-sig'))
        except UnicodeDecodeError:
            categories = ['historical-binary']
        if categories:
            issues.append({'file':'<reachable-history-blob>','categories':categories})
    return {'status':'PASS' if not issues else 'FAIL','files':len(inventory),
            'inventory':inventory,'git_grep_exit':staged.returncode,
            'reachable_blobs':blobs,'issues':issues,
            'limitations':'Heuristic text checks; no device tests or legal approval. No matched values printed.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test',action='store_true')
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps({'self_test':'PASS','positive_categories':self_test(),'git_grep_positive_and_negative':'PASS'}))
    else:
        result = scan()
        print(json.dumps(result,indent=2))
        raise SystemExit(0 if result['status'] == 'PASS' else 1)
