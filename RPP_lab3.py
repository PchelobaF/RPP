from operator import itemgetter
import os, csv, datetime

def new_data(data: list) -> (int, list):
	#Добавление новых строк в data
	while True:
		match input("Хотите чтото добавить в файл?\n1.Да\n2.Нет\nВаш выбор: "):
			case "1":
				print("Чтобы закончить добовление напишите 'КОНЕЦ' (обязательно каждая буква с заглавной)")
				row = []
				while True:
					value = {}
					value["№"] = len(data) + len(row) + 1
					value["дата и время"] = f"{datetime.datetime.now():%d.%m.%Y %H:%M}"
					for key in data[0].keys():
						if key != "дата и время" and key != "№":
							new = input(f"Что добавить в поле {key}?\n")
							if new != "КОНЕЦ":
								value[key] = new
							else:
								for i in row:
									data.append(i)
								print(f"Вы добавили {len(row)} строк(и)", *[i for i in row], sep="\n")
								return 1, data
					row.append(value)
			case "2":
				return 0, data
			case _:
				print("Такого варианта ответа нет")

def dpath() -> (bool, bool, str):
	#Добавление пути до папки
	dir_path = input("Введите путь к папке в которой хотите узнать кол-во файлов: ")
	if os.path.exists(dir_path):
		print("Путь к папке успешно добавлен")
		return True, True, dir_path
	else:
		print("Нет такой папки!!!")
		return vibor(), False, None

def fpath() -> (bool, bool, str):
	#Добавление пути до файла
	file_path = input("Введите путь к csv файлу (включая сам файл): ")
	if os.path.isfile(file_path):
		print("Путь к файлу успешно добавлен")
		return False, True, file_path
	else:
		print("По этому пути нет файла")
		return vibor(), False, None

def vibor() -> int:
	#Выбор пользователя ввести путь заново или выйти из программы
	try:
		v = int(input("1.Ввести заново\n2.Выход\nВаш выбор: "))
		if v == 1:
			return True
	except ValueError:
		print("Нужно ввести только число (буквы и символы нельзя)")
	return False

def row_formating(row: dict) -> dict:
	#Форматируем данные
	row = row[0].split(";")
	row[0] = int(row[0])
	row[2] = float(row[2])
	return row

def count_files_in_dir(dir_path: str) -> int:
	#Подсчет количества файлов в директории
    return sum(len(files) for root, dirs, files in os.walk(dir_path))

def read_data_from_csv(file_path: str) -> list:
	#Чтение данных из CSV файла
	data = []
	with open(file_path, 'r') as f:
		reader = csv.reader(f)
		headers = next(reader)[0].split(";")
		for row in reader:
			row_data = {}
			row = row_formating(row)
			for name, value in zip(headers,row):
				row_data[name] = value
			data.append(row_data)
	return data

def sort_data(data: list, vib: int) -> (str, list):
	#Сортировка данных
	match vib:
		case "1":
			return "Отсортированно по числовому полю", sorted(data, key=itemgetter("№"))
		case "2":
			return "Отсортированно по строковому полю", sorted(data, key=itemgetter("дата и время"))
		case "3":
			return "Отсортированно по числовому полю", sorted(data, key=itemgetter("сумма"))
		case "4":
			return "Отсортированно по строковому полю", sorted(data, key=itemgetter("наименование товарной позиции"))
		case _:
			return "Такого варианта ответа нет"

def filter_data(data: list, vib: int) -> list:
	#Фильтрация числовых данных по критерию
	try:
		crit = input("Введите больше какого числа нужны данные или оставьте поле пустым если хотите выйти\nВаш ответ: ")
		if crit == "":
			return "Завершение работы"
		crit = float(crit)
	except ValueError:
		print("Нужно ввести только число (буквы и символы нельзя)")
	match vib:
		case "1":
			return [row for row in data if row["№"] > crit]
		case "2":
			return [row for row in data if row["сумма"] > crit]
		case _:
			return "Такого варианта ответа нет"

def write_data_to_csv(data: list, file_path: str) -> None:
	#Запись данных в CSV файл
	try:
		with open(file_path, 'w') as f:
			writer = csv.DictWriter(f, delimiter = ";", fieldnames=data[0].keys(), lineterminator="\r")
			writer.writeheader()
			writer.writerows(data)
	except PermissionError:
		print("Открытый файл!\nНевозможно обновить данные")

def main(dir_path: str, file_path: str) -> None:
	s = "1.№\n2.дата и время\n3.сумма\n4.наименование товарной позиции\nВаш выбор: "
	print(f"Кол-во файлов в папке {dir_path.split('/')[-1]} = {count_files_in_dir(dir_path)}")
	data = read_data_from_csv(file_path)
	print(f"В файле {file_path.split('/')[-1]} находятся данные:",*data, sep="\n")
	vib = input(f"Выберите по какому полю отсортировать.\nВ вашем файле есть поля:\n{s}")
	stroka, spisok = sort_data(data, vib)
	print(stroka, *spisok, sep="\n")
	vib = input(f"Выберите по какому полю отфильтровать.\nВ вашем файле есть подходящие поля:\n1.№\n2.сумма\nВаш выбор: ")
	print(*filter_data(data, vib), sep="\n")
	con, data = new_data(data)
	if con:
		write_data_to_csv(data, file_path)

if __name__ == '__main__':
	v = True
	d, f = False, False
	while v:
		if not f and d:
			v, f, file_path = fpath()

		if not d:
			v, d, dir_path = dpath()
	if d and f:
		main(dir_path.replace('\\', "/"), file_path.replace('\\', "/"))	