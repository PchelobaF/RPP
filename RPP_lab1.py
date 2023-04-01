import random

def autolist(n: int) -> list:
	#Заполняем список рандомными числами от 0 до 99
	list_numbers = [random.randint(0, 100) for _ in range(n)]
	return list_numbers

def userlist() -> list:
	#Заполняем список вручную
	list_numbers = list(map(int, input("Введите целые числа (в одну строчку через пробел): ").split()))
	return list_numbers

def del_min_num(start_chain: int, end_chain: int, list_numbers: list) -> None:
	#Удаляем минимальный элемент цепочки
	list_numbers.remove(min(list_numbers[start_chain:end_chain]))

def find_chain(list_numbers: list) -> list:
	#Находим индексы начала и конца цепочки четных чисел
	start_chain = 0
	end_chain = 0
	i = 1
	while i < len(list_numbers):
		if list_numbers[i] % 2 == 0 and list_numbers[i-1] % 2 != 0:
			start_chain = i

		if list_numbers[i] % 2 == 1 and list_numbers[i-1] % 2 != 1:
			del_min_num(start_chain, i, list_numbers)
			i -= 1

		elif i == len(list_numbers)-1 and list_numbers[i] % 2 != 1:
			del_min_num(start_chain, len(list_numbers), list_numbers)
		i += 1
	return list_numbers

def main():
	while True:
		match input("Выберите способ заполнения списка:\n1.Автомотическое заполнение\n2.Ручное заполнение\n3.Выход\nВаш выбор: "):
			case "1":
				try:
					list_numbers = autolist(int(input("Введите длину списка: ")))
					break
				except ValueError:
					print("Нужно ввести только число (буквы и символы нельзя)")
			case "2":
				list_numbers = userlist()
				break
			case "3":
				break
			case _:
				print("Нет такого способа")
	print(f"\nA[{len(list_numbers)}]: {list_numbers}")
	print("Вывод:\n\t ".replace(" ", " "*len(str(len(list_numbers)))), find_chain(list_numbers))

if __name__ == "__main__":
	main()