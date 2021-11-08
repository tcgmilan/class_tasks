import operator

def main():
    global data
    data = [x.strip() for x in open("verseny.txt", "r", encoding = "utf8").readlines()]
    data.pop(0)

def task2():
    success = []
    i = 1
    for x in data:
        hit = False
        for y in x:
            if y == "+":
                if not hit:
                    hit = True
                elif hit:
                    if str(i) not in success:
                        success.append(str(i))
            else:
                hit = False
        i += 1
    print("2.feladat\n"+" ".join(success)+"\n")

def task3():
    result = []
    for x in data:
        result.append(len(x))
    print(f"3.feladat\nLegtöbbet lövő játékos sorszáma: {result.index(max(result))+1}\n")

def task4(sor : str):
    global loertek
    def loertek(sor : str):
        aktpont = 20
        ertek = 0
        for i in range(len(sor)):
            if aktpont > 0 and sor[i] == "-":
                aktpont -= 1
            else:
                ertek += aktpont
        return ertek
    return loertek(sor)

def task5():
    global on_streak, loertek
    index = int(input("5.feladat\nAdjon meg egy rajtszámot! "))
    hits = []
    i = 1
    for x in data[index-1]:
        if x == "+":
            hits.append(str(i))
        i += 1
    _ = " ".join(hits)
    streak = 1
    on_streak = False
    print(data[index-1])
    for x in data[index-1]:
        if x == "-":
            on_streak = False
        elif on_streak:
            streak += 1
        elif x == "+":
            on_streak = True

    print(f"\n5a. feladat Célt érő lövések: {_}")
    print(f"5b. feladat Az eltalált korongok száma: {len(hits)}")
    print(f"5c. A leghosszabb hibátlan sorozat hossza: {streak}")
    print(f"5c. A versenyző pontszáma: {task4(data[index-1])}")

def task6():
    results = []
    class Data:
        def __init__(self, index : int, point : int):
            self.index = index
            self.point = point
    i = 1  
    for x in data:
        results.append(Data(i, task4(x)))
        i += 1
    _ = sorted(results, key = operator.attrgetter("point", "index"))
    file = open("sorrend.txt", "w", encoding = "utf8")
    for x in _:
        file.write(str(_.index(x) + 1) + "    " + str(x.index) + "     " + str(x.point) + "     " + "\n")
    file.close()

if __name__ == "__main__":
    main()
    task2()
    task3()
    task5()
    task6()