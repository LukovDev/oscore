#
# build.py - Файл для компиляции ядра и пр. в бинарный файл для прошивки на файл.
#


# Импортируем:
if True:
    import os
    import json


# Основная функция:
def main() -> None:
    to_return = "../../"  # Сколько раз вернуться назад, чтобы попасть в главный каталог.

    # Читаем конфигурационный файл:
    with open(f"{to_return}/build/config.json", "r+", encoding="utf-8") as f: conf = json.load(f)

    # Получение путей инструментов и прочих данных:
    if True:
        out_name = f"{conf['build-config']['output-file-name']}"
        avr_gcc  = f"{to_return}/{conf['build-config']['avr-gcc']}"

    # Строки для компиляции:
    if True:
        objdmp = f"\"{os.path.split(__file__)[0]}/{avr_gcc}/bin/avr-objdump\""

    # Выводим дамп файла:
    os.system(f"{objdmp} -d {to_return}/build/out/{out_name}.elf")


# Если этот файл запускают:
if __name__ == "__main__":
    main()
