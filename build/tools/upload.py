#
# upload.py - Файл для загрузки прошивки на плату.
#


# Импортируем:
if True:
    import os
    import json
    import time
    import serial                   # |-> pip install pyserial
    import serial.tools.list_ports  # |


# Основная функция:
def main() -> None:
    to_return = "../../"  # Сколько раз вернуться назад, чтобы попасть в главный каталог.

    # Читаем конфигурационный файл:
    with open(f"{to_return}/build/config.json", "r+", encoding="utf-8") as f: conf = json.load(f)

    # Получение путей инструментов и прочих данных:
    if True:
        device   = f"{conf['config']['device']}"
        port     = f"{conf['config']['port']}"
        sps      = f"{conf['config']['serial-port-speed']}"
        out_name = f"{conf['build-config']['output-file-name']}"
        avrdude  = f"{to_return}/{conf['build-config']['avrdude']}"

    # Строки для компиляции:
    if True:
        avrdud       = f"\"{os.path.split(__file__)[0]}/{avrdude}/avrdude\""
        avrdud_flags = f"-C {avrdude}/avrdude.conf -v -p {device} -c avr109 -P {port} -b {sps}"

    if os.path.isfile(f"{to_return}/build/out/{out_name}.hex"):
        # Перетыкаем порт с ардуинкой для прошивки:
        # TODO: переделать. Сделать чтобы сначала проверялся что указанный порт существует и является ардуиной,
        # а после его отключение, включение, и повторный поиск но по имени ардуино. А после, возврат порта.
        if True:
            ser = serial.Serial(port, 1200)
            ser.close()
            ser.open()
            time.sleep(1)
            ser.close()
            print("Waiting for the port to upload...")
            # Поиск порта загрузки на COM4:
            upload_port = None
            while upload_port is None:
                ports = serial.tools.list_ports.comports()
                for new_port, desc, hwid in sorted(ports):
                    if new_port == "COM4":
                        upload_port = new_port
                        break
                time.sleep(1)
            print(f"The upload port was found on: {upload_port}\n")

        upload_avrdude = f"{avrdud} {avrdud_flags} -D -U flash:w:{to_return}/build/out/{out_name}.hex:i"
        
        """
            -F : Игнорировать проверку соединения с МК.
                 Разумеется, такая проверка желательна – поэтому использование этого флага стоит избегать.

            -v : Так называемый «многословный» (verbose) вывод – полезно для контроля и отладки.

            -p : Указываем тип МК для программирования. Например, если бы был ATtiny2313,
                 здесь нужно было бы написать: attiny2313. Мы же указываем нашу атмегу.
            m8 ATmega8
            m16 ATmega16
            m32 ATmega32

            -c : Указываем тип программатора. Если используется STK500 — пишем stk500 и т.д.

            -P : указывается коммуникационный порт, к которому подключён программатор.
                 Это может быть COM1 или LPT1 или даже USB.

            -b : Указывается скорость для работы с последовательным портом – нужно для программаторов,
                 работающих через COM-порт – таких как STK500.

            -D: Отключаем очистку МК перед прошивкой.

            -U :r|w|v:[:format]: Самая важная команда – выполнение прошивки.
            — тип памяти МК — flash или eeprom (или hfuse, lfuse, efuse для конфигурации фьюзов МК).
            r|w|v – флаги определяют, что мы хотим сделать:
            r (read — считать)
            w (write — записать)
            v (verify — проверить).
            файл для записи или чтения.
            [:format] флаг формата данных. Здесь всегда используется формат «Intel Hex», поэтому стоит i

            Таким образом, командой -Uflash:w:»file.hex»:I – мы записываем файл file.hex в FLASH-память МК.
            Если нам потребуется считать eeprom-память в файл «eedump.hex» – мы напишем -Ueeprom:r:eedump.hex:i

            Дополнительные параметры AVRDUDE:

            -C : Указываем путь до конфигурационного файла avrdude.
            -e : Очистка МК.
            -n : Ничего не записывать в МК. Защита, чтобы не отправить в МК ничего лишнего.
            -u : Указывает, что хотим модифицировать фьюзы МК.
            -t : Терминальный режим.
            -q : В противоположность -v – это «тихий» режим – меньше слов – больше дела.
        """

        print(f"avrdude: {upload_avrdude}")
        os.system(upload_avrdude)


# Если этот файл запускают:
if __name__ == "__main__":
    main()
