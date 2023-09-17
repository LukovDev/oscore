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
    # Читаем конфигурационный файл:
    with open("../config.json", "r+", encoding="utf-8") as f:
        conf = json.load(f)

    # Читаем конфигурационный файл сборки:
    with open("build-config.json", "r+", encoding="utf-8") as f:
        build_conf = json.load(f)

    # Получение путей инструментов и прочих данных:
    if True:
        device   = f"{conf['device']}"
        port     = f"{conf['port']}"
        b        = f"{conf['-b']}"
        out_name = f"{build_conf['output-name']}"
        avrdude  = f"../{build_conf['avrdude']}"

    # Строки для компиляции:
    if True:
        avrdud       = f"\"{os.path.split(__file__)[0]}/{avrdude}/avrdude\""
        avrdud_flags = f"-C {avrdude}/avrdude.conf -v -p {device} -c avr109 -P {upload_port} -b {b}"

    if os.path.isfile(f"out/{out_name}.hex"):
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

        upload_avrdude = f"{avrdud} {avrdud_flags} -D -U flash:w:out/{out_name}.hex:i"
        print(upload_avrdude)
        os.system(upload_avrdude)


# Если этот файл запускают:
if __name__ == "__main__":
    main()
