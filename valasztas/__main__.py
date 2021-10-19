from operator import attrgetter, itemgetter
import operator
def task1():
    print(f"1.feladat\nA helyhatósági választáson {len(data)} képviselőjelölt indult!")
def task2():
    print("2.feladat")
    forname = input("Adja meg a képviselőjelölt vezetéknevét: ")
    surname = input("Adja meg a képviselőjelölt keresztnevét: ")
    name = forname + " " + surname
    for x in data:
         if x.name == name:
             print(f"{name} képviselőjelöltnek {x.count}db szavazata van!" )
             return
    print("Ilyen nevű képviselőjelölt nem szerepela nyilvántartásban!")
def task3():
    people = 12345
    voted = 0
    for x in data:
        voted += x.count
    print(f"3.feladat\nA választáson {people} állampolgár, a jogosultak {round((voted / people),2)}%-a vett részt!")
def task4():
    gyep = 0
    zep = 0
    hep = 0
    tisz = 0
    for x in data:
        if x.support == "HEP":
            hep += x.count
        elif x.support == "ZEP":
            zep += x.count
        elif x.support == "GYEP":
            gyep += x.count
        elif x.support == "TISZ":
            tisz += x.count
    voted = gyep + zep + hep + tisz
    print(f"4.feladat\nGyümölcsevők Pártja= {round((100 * gyep / voted),2)}%\nZöldségevők Pártja= {round((100 * zep / voted),2)}%\nHúsevők Pártja= {round((100 * hep / voted),2)}%\nTejivók Szövetsége= {round((100 * tisz / voted),2)}%")
def task5():
    support = max(data, key = lambda x: x.count).support
    if max(data, key = lambda x: x.count).support == "-":
        support = "független"
    print(f"5.feladat\nA legtöbb szavazatot {max(data, key = lambda x: x.count).name} képviselőjelölt kapta, támogató pártja: {support}!")
def task6():
    order = [[x for x in data if x.no == 1], [x for x in data if x.no == 2], [x for x in data if x.no == 3], [x for x in data if x.no == 4], [x for x in data if x.no == 5], [x for x in data if x.no == 6], [x for x in data if x.no == 7], [x for x in data if x.no == 8]]
    maxes = []
    for x in order:
        maxes.append(max(x, key = attrgetter("count")))
    f = open("kepviselok.txt", "w", encoding = "utf8")
    f.write("")
    f.close()
    for x in maxes:
        if x.support == "-":
            x.support = "független"
    f = open("kepviselok.txt", "a", encoding = "utf8")    
    for x in range(0, 8):
        f.write(f"Kerület: {maxes[x].no} Nyertes: {maxes[x].name} Szavazatok: {maxes[x].count} Támogató: {maxes[x].support}\n")
    f.close()
def main():
    global data
    class Candidate:
        def __init__(self, no : int, count : int, name : str, support : str):
            self.no = no
            self.count = count
            self.name = name
            self.support = support
    data = [Candidate(int(x.strip().split(" ")[0]), int(x.strip().split(" ")[1]), x.strip().split(" ")[2] + " " + x.strip().split(" ")[3], x.strip().split(" ")[4]) for x in open("szavazatok.txt", "r", encoding = "utf8").readlines()]
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
if __name__ == "__main__":
    main()