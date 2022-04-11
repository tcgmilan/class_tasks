from time import strftime
data = []
class Data:
    def __init__(self, stop : int, geton : str, id : int, type : str, valid : str):
        self.stop = stop
        self.geton = geton
        self.id = id
        self.type = type
        self.valid = valid

def data_load(data : list):
    for x in open("utasadat.txt", "r", encoding = "utf-8"):
        data.append(Data(
            int(x.split(" ")[0]),
            x.split(" ")[1],
            int(x.split(" ")[2]),
            x.split(" ")[3],
            x.split(" ")[4],
            ))


def task1():
    print("2.feladat")
    temp = []
    for x in data:
        if x.stop != 30:
            temp.append(x)
    print(f"Összesen {len(temp)} utas szállt fel a buszra!")

def task2():
    print("3.feladat")
    i = 0
    for x in data:
        if int(x.geton.split("-")[0]) > int(x.valid):
            i += 1
    print(f"A buszsofőrnek {i} utas jegyét kellett volna elutasítani.")

def task3():
    print("4.feladat")
    counter = []
    for x in range(30):
        counter.append(0)
    for x in data:
        counter[x.stop] += 1
    print(f"A legtöbb utas {max(counter)} a {counter.index(max(counter))}. megállóban próbált felszállni.")
def task4():
    print("5.feladat")
    free = 0
    discount = 0
    for x in data:
        if x.type not in ["FEB", "JGY"] and int(x.geton.split("-")[0]) <= int(x.valid):
            if x.type in ["NYP", "RVS", "GYK"]:
                free += 1
            else:
                discount += 1

    print(f"Ingyenesen utazók száma: {free}.")
    print(f"Kedvezményese utazók száma: {discount}.")


def napokszama(e1 : int, h1 : int, n1 : int, e2 : int, h2 : int, n2 : int):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 / 10
    d1 = 365 * e1 + e1 / 4 - e1 / 100 + e1 / 400 + (h1 * 306 + 5) / 10 + n1 -1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 / 10
    d2 = 365 * e2 + e2 / 4 - e2 / 100 + e2 / 400 + (h2 * 306 + 5) / 10 + n2 -1
    return d2 - d1

def task5():
    print("6.feladat")
    alerts = []
    for x in data:
        if len(x.valid) not in [1, 2, 3]:
            y = int(x.valid[:4])
            m = int(x.valid[4:6])
            d = int(x.valid[6:])
            if napokszama(2019,3,26, y, m, d) <= 3:
                alerts.append(f"{x.id} {y}-{m}-{d}")
    with open("figyelmeztetes.txt", "w", encoding = "utf-8") as f:
        for x in alerts:
            f.write(x + "\n")
        f.close()



    print("figyelmeztetes.txt létrehozva!")

def main():
    data_load(data)
    task1()
    task2()
    task3()
    task4()
    task5()

if __name__ == "__main__":
    main()