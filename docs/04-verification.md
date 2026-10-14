# 4. Что увидели после загрузки

Первый отдельный ребут загрузил recovery из новой цепочки. `/` был tmpfs, board — EU UBI, ядро 6.18.26. Это подтвердило аппаратный старт цепочки и recovery FIT на этом устройстве, но ещё не основную систему.

После изменения только bootcmd/bootmenu в двух env-копиях загрузили production. BL2/FIP/factory/fit/recovery повторно не писали. CRC обеих env проверили; после смены flags 1/2 активной стала вторая копия.

Исторический production bootcmd:

```text
run check_buttons; run boot_production; run boot_recovery; run boot_tftp_forever
```

Он пытается следующие ветки при возврате предыдущей команды. Если `bootm` уже передал управление ядру и оно зависло, последовательность не продолжится автоматически.

Команды чтения, использованные при приёмке:

```sh
ubus call system board
cat /proc/cmdline
cat /proc/mounts
df -h
ubinfo -a
cat /sys/class/mtd/<MTD_FROM_MAP>/bad_blocks
cat /sys/class/mtd/<MTD_FROM_MAP>/ecc_failures
```

Board/cmdline позволяют отличить OEM, RAM и production. Mounts показывают источник overlay; `df` — свободные файлы внутри UBIFS; `ubinfo` — распределение томов. Счётчики NAND сообщают зарегистрированные ошибки в данном снимке, не ресурс чипа на годы вперёд.

| Наблюдение | Вывод и граница |
| --- | --- |
| SquashFS /rom, UBIFS rw /overlay на внутреннем NAND | Production не зависит от USB extroot |
| Обычный повторный reboot, настройки сохранены | Persistence этой установки проверена; не тест новых образов |
| Factory readback совпал | Данные сохранены; RF-характеристики не испытаны |
| LAN доступ, WAN DHCP, DNS/HTTPS от роутера | Не доказывает трафик всех клиентов, VPN или каждый порт |
| Две Wi-Fi AP enabled | Не доказывает подключение клиента и пропускную способность |
| Физический WPS press, PBC 120 секунд на обеих AP | Кнопка и окно проверены; клиент не сопрягался |
| USB/ext4 обнаружены, LED настроен | Извлечение и произвольные ФС не проверены |
| LED/rear handler вызван программно | Физические short/long press задней кнопки не проверены |

После смены `wpad-basic-mbedtls` на полный `wpad-mbedtls` добавили `hostapd-utils`. Замена пакета не заменила старый работающий hostapd: он отвергал новые параметры WPS после wifi reload. Перезапуск wpad позволил открыть PBC. Новая чистая сборка использует basic; старую аппаратную проверку нельзя приписать ей.

Envtools сперва не знали новое board name. Локальный фикс настроил реальные env volumes и LEB-геометрию, а не vendor offsets. Две valid CRC в custom env не доказывают наличие redundant backend в чистом upstream loader.

Поздний audit показал около 27,9 МиБ свободного overlay (первый production snapshot — 31,5 МиБ). Разные моменты проверки дают разные числа; это не противоречие. Сохранённые excerpts приведены в [evidence](../evidence/README.md).
