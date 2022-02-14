data = []
class Subject:
    def __init__(self, name : str, _class : str, subject: str, ammount: int):
        self.name = name
        self._class = _class
        self.subject = subject
        self.ammount = ammount

def task1():
    x = Subject(None, None, None, None)
    i = 0
    for y in open("beosztas.txt", "r", encoding = "utf8").readlines():
        if i == 0:
            x.name = y.strip()
        elif i == 1:
            x.subject = y.strip()
        elif i == 2:
            x._class = y.strip()
        elif i == 3:
            x.ammount = int(y)
            i = -1
            data.append(x)
            x = Subject(None, None, None, None)
        i += 1
    print("1.feladat")
    print("Adatállomány Beolvasva\n")

def task2():
    print("2.feladat")
    print(f"A fájlban {len(data)} bejegyzés van.\n")
    
def task3():
    print("3. feladat")
    x = 0
    for y in data:
        x += y.ammount
    print(f"Az iskolában a heti összóraszám: {x}\n")

def task4():
    n = input("Egy tanár neve= ")
    x = 0
    for y in data:
        if y.name == n:
            x += y.ammount
    print(f"A tanár heti óraszáma: {x}\n")

def task5():
    c = input("Osztály= ")
    s = input("Tantárgy= ")
    split = False
    for y in data:
        if c[:2] in y._class and s == y.subject:
            if "x" in y._class:
                split = True
    if split: print("Csoportbontásban tanulják.")
    else: print("Osztályszinten tanulják.")

def task6():
    x = []
    for y in data:
        if y.name not in x:
            x.append(y.name)
    print(f"Az iskolában {len(x)} tanár tanít.")

def task7():
    with open("of.txt", "w", encoding = "utf8") as f:
        x = []
        for y in data:
            if y.subject == "osztalyfonoki":
                x.append(f"{y._class} - {y.name}\n")
        f.writelines(x)


def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
if __name__ == "__main__":
    main()