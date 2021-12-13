from collections import Counter

data = []





def main():
    file = open("penztar.txt", "r", encoding = "utf8").readlines()
    temp = []
    for x in file:
        x = x.strip()
        if x == "F":
            data.append(temp)
            temp = []
        else:
            temp.append(x)

def task1():
    print("2.feladat")
    print("Fizetések száma: " + str(len(data)))

def task2():
    print("3.feladat")
    print(f"Az első vásárló {len(data[0])} darab árucikket vásárolt.")

def task3_4():
    print("4.feladat")
    index = int(input("Adja meg egy vásárlás sorszámát! "))
    item = input("Adja meg egy árucikk nevét! ")
    count = data[index - 1].count(item)
    buyers = []
    print(f"Az adott árucikkből a vásárló {count}db-ot vásárolt!")
    print("5.feladat")
    for x in data:
        for y in x:
            if y == item:
                buyers.append(data.index(x))
    print("Az első vásárlás sorszáma: " + str(buyers[0]))
    print("Az utolsó vásárlás sorszáma: " + str(buyers[-1]))
    print(f"{len(dict.fromkeys(buyers))} vásárlás során vettek belőle!")

def task5():
    print("6.feladat")
    count = int(input("Hány db árucikket szeretne vásárolni? "))
    print(f"{count}db vételkor fizetendő: {500 - (50 * (count - 1))}")

def task6():
    print("7.feladat")
    index = int(input("Adja meg egy vásárlás sorszámát! "))
    result = Counter(data[index - 1])
    for k, v in result.items():
        print(k + ": " + str(v))

def task7():
    f = open("osszeg.txt", "w", encoding = "utf8")
    i = 1
    for x in data:
        price = 0
        result = Counter(x)
        for k, v in result.items():
            if v > 3:
                price += 550 - 50 * 3
            else:
                price += 550 - 50 * v

        f.write(f"{i}: {price}\n")
        price = 0
        i += 1

    f.close()

if __name__ == "__main__":
    main()
    task1()
    task2()
    task3_4()
    task5()
    task6()
    task7()
