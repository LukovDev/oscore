#
# build.py - Файл для компиляции ядра и пр. в бинарный файл для прошивки на файл.
#


# Импортируем:
if True:
    import os
    import json
    import shutil


# Функция поиска файлов:
def find_files(file_type: str, in_dir: str = "src/", to_return: str = "") -> list:
    files_list = []
    print(f"│\n├─ Find \"{file_type}\" (in \"{in_dir}\" dir):")
    for root, dirs, files in os.walk(f"{to_return}{in_dir}"):
        for file in files:
            if file.endswith(file_type):
                files_list.append(os.path.join(root, file))
                if len(files_list) == 1: print(f"│ ┌< /{str(os.path.join(root, file))[len(to_return):]}")
                else: print(f"│ ├< /{str(os.path.join(root, file))[len(to_return):]}")
    if len(files_list) == 0: print(f"│ ┌< \"{file_type}\" files not found.")
    print(f"│ │\n│ └> Total \"{file_type}\" files: {len(files_list)}")
    return files_list


# Основная функция:
def main() -> None:
    to_return = "../../"  # Сколько раз вернуться назад, чтобы попасть в главный каталог.

    # Читаем конфигурационный файл:
    with open(f"{to_return}/build/config.json", "r+", encoding="utf-8") as f: conf = json.load(f)

    # Получение путей инструментов и прочих данных:
    if True:
        device    = f"{conf['config']['device']}"
        clock     = f"{conf['config']['clock']}"
        out_name  = f"{conf['build-config']['output-file-name']}"
        avr_gcc   = f"{to_return}/{conf['build-config']['avr-gcc']}"
        gcc_flags = conf["build-config"]["avr-gcc-flags"]

        # Преобразование gcc флагов:
        flags = ""
        for flag in gcc_flags: flags += f"{flag} "
        gcc_flags = flags

        # main_file = f"../{build_conf['main-file']}"
        # c_files = [main_file]

    # Строки для компиляции:
    if True:
        flags = f"{gcc_flags} -DF_CPU={clock} -mmcu={device} -I {to_return}\\core\\includes\\"
        compil = f"\"{os.path.split(__file__)[0]}/{avr_gcc}/bin/avr-g++\""
        objcop = f"\"{os.path.split(__file__)[0]}/{avr_gcc}/bin/avr-objcopy\""
        avrsiz = f"\"{os.path.split(__file__)[0]}/{avr_gcc}/bin/avr-size\""

    # Поиск файлов:
    if True:
        print("┌─── Find Files: ───────────────────────────────────────────────")
        c_files = find_files(file_type=".c", in_dir="src/", to_return=to_return)         # Список .c файлов.
        c_files.extend(find_files(file_type=".c", in_dir="core/", to_return=to_return))  # Список .c файлов.
        print("│\n└───────────────────────────────────────────────────────────────")

    # Компиляция файлов:
    if True:
        print("\n\n┌─── Compiling Files: ──────────────────────────────────────────")
        # Предварительная работа с папками:
        if True:
            # Если папки tmp нет, создать её:
            if not os.path.isdir(f"{to_return}/build/tmp"): os.mkdir(f"{to_return}/build/tmp")
            # Иначе, удалить её и создать заново:
            else:
                shutil.rmtree(f"{to_return}/build/tmp")
                os.mkdir(f"{to_return}/build/tmp")

            # Проверяем, есть ли папка out. Если да, то удаляем:
            if os.path.isdir(f"{to_return}/build/out"): shutil.rmtree(f"{to_return}/build/out")
            os.mkdir(f"{to_return}/build/out")
        
        # Проходимся по списку файлов .c в папке src:
        for filepath in c_files:
            print(f"│\n├─ Compiling -> {filepath}")
            o_f = f"{to_return}/build/tmp/{os.path.splitext(os.path.basename(filepath))[0]+'.o'}"
            os.system(f"{compil} {flags} -c {filepath} -o {o_f}")
            print(f"├─ Output -> {o_f}")

        # os.system("{} -x assembler-with-cpp -c {} -o {}.o".format(COMPILE, file, os.path.splitext(file)[0]))
        print("│\n└───────────────────────────────────────────────────────────────")

    # Связывание файлов:
    if True:
        print("\n\n┌─── Linking Files: ────────────────────────────────────────────")
        # Создаём .elf файл:
        if True:
            objects = []

            # Получаем список .o файлов:
            for file in os.listdir(f"{to_return}/build/tmp/"):
                if os.path.isfile(os.path.join(f"{to_return}/build/tmp/", file)) and file.endswith('.o'):
                    objects.append(f"{to_return}/build/tmp/{file}")

            o_files = " ".join([os.path.splitext(obj)[0] + ".o" for obj in objects])
            os.system(f"{compil} {flags} -o {to_return}/build/out/{out_name}.elf {o_files}")
        shutil.rmtree(f"{to_return}/build/tmp")  # Удаляем tmp папку, т.к. она нам больше не нужна.
        print("│\n└───────────────────────────────────────────────────────────────")

    # Конвертация основного бинарного файла:
    if True:
        print("\n\n┌─── File Conversion: ──────────────────────────────────────────")
        file = f"{to_return}/build/out/{out_name}.hex"
        os.system(f"{objcop} -j .text -j .data -O ihex {to_return}/build/out/{out_name}.elf {file}")
        print("│\n└───────────────────────────────────────────────────────────────\n\n")

    # Выводим размер итогового файла:
    os.system(f"{avrsiz} --format=avr --mcu={device} {to_return}/build/out/{out_name}.elf")


# Если этот файл запускают:
if __name__ == "__main__":
    main()
