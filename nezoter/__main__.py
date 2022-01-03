data = []

class Seat:
	def __init__(self, row : int, seat : int, is_reserved : bool, category : int):
		self.row = row
		self.seat = seat
		self.is_reserved = is_reserved
		self.category = category

def createdata():
	row = 1
	seat = 1
	category = 0
	i = 0
	is_reserved = False
	for x in open("foglaltsag.txt", "r", encoding = "utf8"):
		x = x.strip()
		for n in x:
			if n == "x":
				is_reserved = True
			elif n == "o":
				is_reserved = False
			data.append(Seat(row, seat, is_reserved, category))	
			seat += 1 
		row += 1
	for y in open("kategoria.txt", "r", encoding = "utf8"):
		y = y.strip()
		for m in y:
			data[i].category = int(m)
			i += 1

def task2():
	print("2.feladat")
	n = int(input("Adjon meg egy sorszámot: "))
	m = int(input("Adjon meg egy székszámot: "))

	for x in data:
		if x.row == n and x.seat == m:
			print("Az adott hely sajnos már foglalt!") if x.is_reserved else print("Az adott hely még nem foglalt!")
			return

def task3():
	all_seat = len(data)
	reserved_seat = 0
	percentage = 0
	for x in data:
		if x.is_reserved:
			reserved_seat += 1
	percentage =  round(reserved_seat / all_seat * 100)
	print("3.feladat")
	print(f"Az előadásra eddig {all_seat} jegyet adtak el, ez a nézőtér {percentage}%-a.")

def task4():
	counter = [0, 0, 0, 0, 0]
	for x in data:
		counter[x.category - 1] += 1
	print("4.feladat")
	print(f"A legtöbb jegyet a(z) {counter.index(max(counter))+1}. árkategóriában értékesítették.")

def task5():
	cat_1 = 5000
	cat_2 = 4000
	cat_3 = 3000
	cat_4 = 2000
	cat_5 = 1000
	money = 0

	for x in data:
		if x.category == 1:
			money += cat_1
		elif x.category == 2:
			money += cat_2
		elif x.category == 3:
			money += cat_3
		elif x.category == 4:
			money += cat_4
		elif x.category == 5:
			money += cat_5

	print("5.feladat")
	print(f"Összesen {money}Ft bevétele van a színháznak!")

def task6():
	db = 0
	i = 0
	is_empty = False
	for x in data:
		if i == 0 and x.is_reserved == False:
			is_empty = True
			i += 1
		elif i == 1 and x.is_reserved == False:
			db += 1
			i = 0
		else:
			is_empty = False
			i = 0
	print(f"Összesen {db}db páros üres hely van!")

def task7():
	file = open("szabad.txt", "w", encoding = "utf8")
	string = ""
	row = 1
	for x in data:
		if x.row != row:
			string += "\n"
			row = x.row
		if x.is_reserved == False:
			string += "x"
		else:
			string += str(x.category)
	file.write(string)
	file.close()

def main():
	createdata()
	task2()
	task3()
	task4()
	task5()
	task6()
	task7()

if __name__ == "__main__":
	main()