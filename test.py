import argparse # парсер аргументов командной строки 
import json 
 
 
# DONE: Читать файл конфига и выводить 
# TODO: Открывать файл и менять настройку(ки) 
# TODO: Написать документацию 
# TODO: Написать README 
 
# Функция которая читает конфиг 
def read_config(filepath): 
    with open(filepath, 'r', encoding='utf-8') as f: 
        data = json.load(f) 
        print(json.dumps(data, indent=2)) 
 
 
def main(): 
    # Создаем парсер аргуменотов 
    parser = argparse.ArgumentParser(description="Работа с .json файлом конфигураций") 
    parser.add_argument('action',type=str, choices=['read', 'write']) # Создание аргумента для выбора действия 
 
    # Создание аргумента для имени файла, принимает путь до файла для функции read_config 
    parser.add_argument('filepath', type=str) 
    # Парсер аругментов и сохранение в args 
    args = parser.parse_args() 
 
    if args.action == 'read': 
        read_config(args.filepath) 
    elif args.action == 'write': 
        print('write') 
 
if __name__ == "__main__": 
    main()
