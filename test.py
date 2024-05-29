import argparse # парсер аргументов командной строки
import json


# DONE: Читать файл конфига и выводить
# DONE: Открывать файл и менять настройку(ки)
# DONE: Написать документацию
# DONE: Написать README

# Функция чтения конфига
def read_config(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

# Функция записи конфига в файл
def write_config(filepath, config):
    with open(filepath, 'w', encoding='utf-8') as f:
        data = json.dump(config, f, indent=4)
    
errors = 0
# Изменение параметра о конфиге
def update_config(config, param, value):
    try:
        keys = param.split('.')     # Путь к параметру
        for key in keys[:-1]:   # Проходим по всем ключам, кроме последнего
            # переход на следующий уровень вложенности. Если ключа нет, то создаём пустой словарь
            data = config.setdefault(key, {})
        data[keys[-1]] = value   # устанавливаем новое значение для поледнего ключа 
    except UnboundLocalError:
        errors += 1
        print(f"Соблюдайте пример, обратитесь к категории, выберите параметр и напишите его значение. \nНапример: server.host=120.25.52.110\n           ^      ^          ^\n    категория  параметр   значение")


# server.host=4.5.67.8

def main():
    # Создаем парсер аргуменотов
    parser = argparse.ArgumentParser(description="Работа с .json файлом конфигураций")
    parser.add_argument('action',type=str, choices=['read', 'write'], help="Действие которое необходимо выполнить") # Создание аргумента для выбора действия

    # Создание аргумента для имени файла, принимает путь до файла для функции read_config
    parser.add_argument('filepath', type=str, help="путь к файлу конфигурации")
    # создание аргумента для параметра и его нового значения
    parser.add_argument("--param", type=str, help='Параметр и значение для этого параметра в формате: key.key=value (только для действия write)')

    # Парсер аругментов и сохранение в args
    args = parser.parse_args()

    if args.action == 'read':
        config_data = read_config(args.filepath)
        print(json.dumps(config_data, indent=2))
    elif args.action == 'write':
        config_data = read_config(args.filepath) # Хранит данные файла
        path, value = args.param.split("=") # Параметр и значение
        update_config(config_data, path, value) 
        write_config(args.filepath, config_data)
        if errors < 1:
            print(f"\nВвод успешен. \nПараметр: {path}\nЗначение: {value}")
        else:
            print("Программа завершилась с ошибками")
        # server.host=5.4.3.5

if __name__ == "__main__":
    main()
