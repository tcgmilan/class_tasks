import os

data = []

class Reservation:
    def __init__(self, forname : str, surname : str, date : str, reservation : str):
        self.forname = forname
        self.surname = surname
        self.date = date
        self.reservation = reservation

for x in open("fogado.txt", "r").readlines():
    forname, surname, date, reservation = x.split()
    data.append(Reservation(forname, surname, date, reservation))

def task1():
    print("1.feladat")
    print("Fájl beolvasás sikeres")

def task2():
    print("\n")
    print("2.feladat")
    print(f"Fogalások száma: {len(data)}")

def task3():
    print("\n")
    print("3.feladat")
    i = 0
    forname, surname = input("Adjon meg egy nevet: ").split()
    for x in data:
        if x.forname == forname and x.surname == surname: i += 1
    print(f"{forname} {surname} néven {i} időpontfoglalás van.")

def task4():
    print("\n")
    print("4.feladat")
    res = []
    y = input("Adjon meg egy érvényes időpontot (pl. 17:10): ")
    for x in data:
        if x.date == y:
            res.append(" ".join([x.forname, x.surname]))
    res = sorted(res)
    open((y.replace(":","")+".txt"), "w").writelines((x + "\n") for x in res)
    for x in res:
        print(x)

def task5():
    print("\n")
    print("5.feladat")
    print("Tanár neve: " + data[0].forname + " " + data[0].surname)
    print("Foglalt időpont: " + data[0].date)
    print("Foglalás ideje: " + data[0].reservation)

def task6():
    print("\n")
    print("6.feladat")
    dates = list(pd.date_range("16:00", "17:50", freq="10min").strftime("%H:%M"))
    for x in data:
        if x.forname == "Barna" and x.surname == "Eszter":
            if x.date in dates:
                dates.remove(x.date)
    for x in dates:
        print(x)
    print(f"Barna Eszter legkorábban távozhat: {dates[-2]}")


def main():
    print("Horváth Balázs | 12.H | Feladat: fogadoora")
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()

if __name__ == "__main__":
    try:
        import pandas as pd 
    except:
        try:
            os.system("pip install pandas")
            os.system("pip3 install pandas")
        except:
            exit("Install pandas package!")

    main()
        