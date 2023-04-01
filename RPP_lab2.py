import numpy as np

def MakeMatr() -> list:
	#Заполняем матрицу [5,10] рандомными числами от 0 до 9 
    Matr = np.random.randint(0, 10, size=(5,10))
    return Matr

def write_to_file(Matr: list, midcol: float, midrow: float) -> None:
	#Добавляем к исходной матрице результаты вычислений 
	Matr = np.column_stack((Matr, midrow))
	midcol = np.append(midcol, [""])
	Matr = np.vstack((Matr, midcol))
	#Записываем все в текстовый файл
	with open("output.txt", "w") as f:
		np.savetxt(f, Matr, fmt='%s')

def midl_colandrow(Matr: list) -> None:
	#Вычисляем средние значения по столбцам и также по строкам
	midcol = np.mean(Matr, axis=0)
	midrow = np.mean(Matr, axis=1)
	write_to_file(Matr, midcol, midrow)

def main() -> None:
	midl_colandrow(MakeMatr())

if __name__ == "__main__":
	main()