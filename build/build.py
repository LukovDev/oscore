#
# build.py - Файл для компиляции ядра и пр. в бинарный файл для прошивки на файл.
#


# Импортируем:
if True:
    import os
    import json
    import shutil


# Функция поиска файлов:
def find_files(file_type: str) -> list:
    files_list = []
    one_dir = "src/"
    print(f"│\n├─ Find \"{file_type}\" (in \"{one_dir}\" dir):")
    for root, dirs, files in os.walk(f"../{one_dir}"):
        for file in files:
            if file.endswith(file_type):
                files_list.append(os.path.join(root, file))
                if len(files_list) == 1: print(f"│ ┌< {os.path.join(root, file)}")
                else: print(f"│ ├< {os.path.join(root, file)}")
    if len(files_list) == 0: print(f"│ ┌< \"{file_type}\" files not found.")
    print(f"│ │\n│ └> Total \"{file_type}\" files: {len(files_list)}")
    return files_list


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
        clock    = f"{conf['clock']}"
        out_name = f"{build_conf['output-name']}"
        avr      = f"../{build_conf['avr']}"
        avr_gcc  = f"../{build_conf['avr-gcc']}"

        # main_file = f"../{build_conf['main-file']}"
        # c_files = [main_file]

    # Строки для компиляции:
    if True:
        flags = f"-Wall -Os -DF_CPU={clock} -mmcu={device}"
        compil = f"\"{os.path.split(__file__)[0]}/{avr_gcc}/bin/avr-g++\""
        objcop = f"\"{os.path.split(__file__)[0]}/{avr_gcc}/bin/avr-objcopy\""
        avrsiz = f"\"{os.path.split(__file__)[0]}/{avr_gcc}/bin/avr-size\""

    # Поиск файлов:
    if True:
        print("┌─── Find Files: ───────────────────────────────────────────────")
        c_files = find_files(".c")  # Список .c файлов.
        print("│\n└───────────────────────────────────────────────────────────────")

    # Компиляция файлов:
    if True:
        print("\n\n┌─── Compiling Files: ──────────────────────────────────────────")
        # Предварительная работа с папками:
        if True:
            # Если папки tmp нет, создать её:
            if not os.path.isdir("tmp"): os.mkdir("tmp")
            # Иначе, удалить её и создать заново:
            else:
                shutil.rmtree("tmp")
                os.mkdir("tmp")

            # Проверяем, есть ли папка out. Если да, то удаляем:
            if os.path.isdir("out"): shutil.rmtree("out")
            os.mkdir("out")
        
        # Проходимся по списку файлов .c в папке src:
        for filepath in c_files:
            print(f"│\n├─ Compiling -> {filepath}")
            os.system(f"{compil} {flags} -c {filepath} -o tmp/{os.path.splitext(os.path.basename(filepath))[0]+'.o'}")
            print(f"├─ Output -> ./tmp/{os.path.splitext(os.path.basename(filepath))[0]+'.o'}")

        # os.system("{} -x assembler-with-cpp -c {} -o {}.o".format(COMPILE, file, os.path.splitext(file)[0]))
        print("│\n└───────────────────────────────────────────────────────────────")

    # Связывание файлов:
    if True:
        print("\n\n┌─── Linking Files: ────────────────────────────────────────────")
        # Создаём .elf файл:
        if True:
            objects = []

            # Получаем список .o файлов:
            for file in os.listdir("tmp/"):
                if os.path.isfile(os.path.join("tmp/", file)) and file.endswith('.o'):
                    objects.append(f"tmp/{file}")

            o_files = " ".join([os.path.splitext(obj)[0] + ".o" for obj in objects])
            os.system(f"{compil} {flags} -o out/{out_name}.elf {o_files}")
        shutil.rmtree("tmp")  # Удаляем tmp папку, т.к. она нам больше не нужна.
        print("│\n└───────────────────────────────────────────────────────────────")

    # Конвертация основного бинарного файла:
    if True:
        print("\n\n┌─── File Conversion: ──────────────────────────────────────────")
        os.system(f"{objcop} -j .text -j .data -O ihex out/{out_name}.elf out/{out_name}.hex")
        print("│\n└───────────────────────────────────────────────────────────────")

    # Выводим размер итогового файла:
    if True:
        os.system(f"{avrsiz} --format=avr --mcu={device} out/{out_name}.elf")


# Если этот файл запускают:
if __name__ == "__main__":
    main()
