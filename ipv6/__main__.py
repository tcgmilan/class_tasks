data = []

class Data:
    def __init__(self, ip : str, type : str):
        self.ip = ip
        self.type = type

for x in open("ip.txt", "r", encoding = "utf8").readlines():
    if "fc" in x.strip():
        data.append(Data(x, "local"))
    elif "fd" in x.strip():
        data.append(Data(x, "local"))
    elif "2001:0db8" in x.strip():
        data.append(Data(x, "document"))
    elif "2001:0e" in x.strip():
        data.append(Data(x, "global"))


def task2():
    print(f"2.feladat\nAz állományban {len(data)} darab adatsor van!\n")

def task3():
    smallest = data[0].ip
    for x in data:
        if x.ip < smallest:
            smallest = x.ip
    print(f"3.feladat\nA legalacsonyabban tárolt IP-cím:\n{smallest}")

def task4():
    doc = 0
    glob = 0
    loc = 0
    for x in data:
        if x.type == "local":
            loc += 1
        elif x.type == "document":
            doc += 1
        elif x.type == "global":
            glob += 1
    print(f"4.feladat\nDokumentációs címek: {doc}\nGlobális egyedi címek: {glob}\nHelyi egyedi címek: {loc}\n")

def task5():
    file = open("sok.txt", "w", encoding = "utf8")
    i = 1
    for x in data:
        if x.ip.count("0") >= 18:
            file.write(x.ip+"\n")
        i += 1

def task6():
    print("6.feladat")
    choose = int(input("Kérek egy számot: "))
    i = 0
    count = 0
    ip = data[choose-1].ip
    ip_split = ip.split(":")
    default = ip
    for x in ip_split:
        if "0000" in ip_split:
            count += 1
        if x.startswith("0"):
            ip_split[i] = x[1:]
        i += 1
    i = 0
    for x in ip_split:
        if x == "00" or x == "000" or x == "0000":
            ip_split[i] = "0"
        i += 1
    ip = ":".join(ip_split)

    print(default + ip)
    return default

def task7(ip : str):
    print("7.feladat")
    i = 0
    count = 0
    ip_split = ip.split(":")
    default = ip
    for x in ip_split:
        if "0000" in ip_split:
            count += 1
        if x.startswith("0"):
            ip_split[i] = x[1:]
        i += 1
    if count > 2:
        ip_split[count-1] = ""
    i = 0
    for x in ip_split:
        if x == "00" or x == "000" or x == "0000":
            ip_split[i] = "0"
        i += 1
    ip = ":".join(ip_split)

    print(ip)
    


def main():

    task2()
    task3()
    task4()
    task5()
    task7(task6())

if __name__ == "__main__":
    main()