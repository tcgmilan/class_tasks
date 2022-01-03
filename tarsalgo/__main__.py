from collections import Counter
from datetime import dateitme
data = []
user = None

class Entry:
    def __init__(self, hour : int, minute : int, id : int, direction : str):
        self.hour = hour
        self.minute = minute
        self.id = id
        self.direction = direction

def fill_class():
    for x in open("ajto.txt", "r", encoding = "utf8"):
        y = x.strip().split(" ")
        data.append(Entry(int(y[0]), int(y[1]), int(y[2]), str(y[3])))
def task1():
    last = next(x for x in reversed(data) if x.direction == "ki")
    print("2.feladat")
    print(f"Elsőként érkező azonosítója: {data[0].id}")
    print(f"Utolsóként távozó azonosytója: {last.id}")

def task2():
    ids = []
    for z in data:
        ids.append(z.id)
    count = list(Counter(ids).values())
    x = [y for n, m in Counter(ids).most_common() for y in [n] * m]
    ids = list(dict.fromkeys(x))
    f = open("athaladas.txt", "w", encoding = "utf8")
    i = 1
    for y in ids:
        f.write(str(i) + ": " + str(y) + ", " + str(count[i - 1]) + "db"+"\n")
        i += 1

def task3():
    print("4.feladat")
    indoor = []
    outdoor = []
    for x in data:
        if x.direction == "be":
            indoor.append(x.id)
            try: outdoor.remove(x.id)
            except: pass
        else:
            outdoor.append(x.id)
            try: indoor.remove(x.id)
            except: pass
    print(", ".join(str(x) for x in list(dict.fromkeys(outdoor))))

def task4():
    print("5.feladat")
    indoor = []
    count = 0
    hour = 0
    minute = 0
    for x in data:
        if len(indoor) > count:
            count = len(indoor)
            hour = x.hour
            minute = x.minute
        if x.direction == "be":
            indoor.append(x)
        else:
            try: indoor.remove(x)
            except: pass
    print(f"A legtöbben {hour} óra {minute} perckor tartózkodtak bent!")

def task5():
    global user
    print("6.feladat")
    user = int(input("Adjon meg kérem egy azonosítót: "))
def task6():
    result = []
    _ = {"be" : "", "ki" : ""}
    global user
    print("7.feladat")
    for x in data:
        if x.id == user:
            if x.direction == "be":
                _["be"] = str(x.hour) + ":" + str(x.minute)
            if x.direction == "ki":
                _["ki"] = str(x.hour)+ ":" + str(x.minute)
                result.append(_)
                _ = {"be" : "", "ki" : ""}
    result.append(_)
    for x in result:
        print(x["be"] +" - " + x["ki"])
        
def main():
    
    fill_class()
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()


if __name__ == "__main__":
    main()