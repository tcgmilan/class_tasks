def task1():
    print(f"\n1.feladat\nA hét legelső útja {data[0].km} km volt!")
def task2():
    print(f"\n2.feladat\nA hét legutolsó útja {data[-1].km} km volt!")
def task3():
    days = [1,2,3,4,6,7]
    for x in data:
        if x.day in days:
            days.remove(x.day)
    y = ", ".join(str(x) for x in days)
    print(f"\n3.feladat\nA futár {y} nap(okon) tartott szünetet!")
def task4_5():
    days = [0,0,0,0,0,0,0]
    km = [0,0,0,0,0,0,0]
    for x in data:
        days[x.day - 1] += 1
        km[x.day - 1] += x.km

    y = days.index(max(days))

    print(f"\n4.feladat\nA futár a(z) {str(y)}. napon fuvarozott a legtöbbet!")
    print(f"""
5.feladat
1. nap: {km[0]}km
2. nap: {km[1]}km
3. nap: {km[2]}km
4. nap: {km[3]}km
5. nap: {km[4]}km
6. nap: {km[5]}km
7. nap: {km[6]}km
""")
def task6():
    choice = int(input("Adj meg egy tetszőleges távolságot: "))
    cash = 0
    if choice in range(1,3):
        cash = 500
    elif choice in range(3,6):
        cash = 700
    elif choice in range(6,11):
        cash = 900
    elif choice in range(11,21):
        cash = 1400
    elif choice in range(21,31):
        cash = 2000
    print(f"\n6.feladat\nA kapott összeg az útért {str(cash)} ft!")
def task7():
    file = open("dijazas.txt","w", encoding = "utf8")
    file.write("")
    file.close()
    new_list = sorted(data, key = operator.attrgetter("day", "driveno"))
    for x in new_list:
        if x.km in range(1,3):
            cash = 500
        elif x.km in range(3,6):
            cash = 700
        elif x.km in range(6,11):
            cash = 900
        elif x.km in range(11,21):
            cash = 1400
        elif x.km in range(21,31):
            cash = 2000
        file = open("dijazas.txt", "a", encoding = "utf8")
        file.write(f"{x.day}. nap {x.driveno}. út: {cash} Ft\n")
        file.close()
def task8():
    total = 0
    for x in data:
        if x.km in range(1,3):
            total += 500
        elif x.km in range(3,6):
            total += 700
        elif x.km in range(6,11):
            total += 900
        elif x.km in range(11,21):
            total += 1400
        elif x.km in range(21,31):
            total += 2000
    print(f"\n8.feladat\nA heti munkáért összesen {str(total)} ft jár!")
def main():
    import operator
    global data
    class NewData:
        def __init__(self, day : int, driveno : int, km : int):
            self.day = day
            self.driveno = driveno
            self.km = km
    data = []
    
    for x in open("tavok.txt", "r", encoding = "utf8").readlines():
        x = x.strip()
        data.append(NewData(int(x.split(" ")[0]), int(x.split(" ")[1]), int(x.split(" ")[2])))
    
    task1()
    task2()
    task3()
    task4_5()
    task6()
    task7()
    task8()
if __name__ == "__main__":
    main()