import operator
data = []

class Report:
    def __init__(self, location : str, hour : str, minute : str, wind_dir : str, wind_force : str, temperature : str):
        self.location = location
        self.hour = hour
        self.minute = minute
        self.wind_dir = wind_dir
        self.wind_force = wind_force
        self.temperature = int(temperature)

with open("tavirathu13.txt", "r", encoding = "utf8") as f:
    for x in f:
        data.append(Report(
            x.split(" ")[0],
            x.split(" ")[1][:2],
            x.split(" ")[1][-2:],
            x.split(" ")[2][:3],
            x.split(" ")[2][-2:],
            x.split(" ")[3]
        ))

def task2():
    x = []
    print("2.feladat")
    z = input("Adja meg egy település kódját! Település: ")
    for y in data:
        if y.location == z:
            x.append(y)
    print(f"Az utolsó mérési adat a megadott településről {x[-1].hour}:{x[-1].minute}-kor érkezett.")

def task3():
    print("3.feladat")
    min_d = sorted(data, key = operator.attrgetter("temperature"))
    max_d = sorted(data, key = operator.attrgetter("temperature"), reverse = True)
    print(min_d[0].temperature)
    print(f"A legalacsonyabb hőmérséklet: {min_d[0].location} {min_d[0].hour}:{min_d[0].minute} {min_d[0].temperature} fok.\nA legmagasabb hőmérséklet: {max_d[0].location} {max_d[0].hour}:{max_d[0].minute} {max_d[0].temperature} fok.")

def task4():
    print("4.feladat")
    x = []
    for y in data:
        if y.wind_dir == "000" and y.wind_force == "00":
            x.append(y)
    if len(x):
        for y in x:
            print(f"{y.location} {y.hour}:{y.minute}")
    else:
        print("Nem volt szélcsend a mérések idején.")

def task5():
    print("5.feladat")
    locs = [x.location for x in data]
    locs = list(dict.fromkeys(locs))
    for x in locs:
        global avg, middle, name, temps, avgtemps, alltemps
        avg = 0
        middle = 0
        avgtemps = []
        alltemps = []
        hours = {"01" : 0, "07" : 0, "13" : 0, "19" : 0}
        name = x
        for y in data:

            if y.location == x:
                alltemps.append(int(y.temperature))
                if y.hour == "01":
                    hours["01"] = 1
                    avgtemps.append(int(y.temperature))
                elif y.hour == "07":
                    hours["07"] = 1
                    avgtemps.append(int(y.temperature))
                elif y.hour == "13":
                    hours["13"] = 1
                    avgtemps.append(int(y.temperature))
                elif y.hour == "19":
                    hours["19"] = 1
                    avgtemps.append(int(y.temperature))
        if hours["01"] == 1 and hours["07"] == 1 and hours["13"] == 1 and hours["19"] == 1:
            print(f"{name} Középhőmérséklet: {round(sum(avgtemps) / len(avgtemps))}; Hőmérséklet-ingadozás {round(max(alltemps) - min(alltemps))}")
        else:
            name += " NA;"
            print(f"{name} Hőmérséklet-ingadozás {round(max(alltemps) - min(alltemps))}")

def task6():
    locs = [x.location for x in data]
    locs = list(dict.fromkeys(locs))
    for x in locs:
        f = open(f"{x}.txt", "w", encoding = "utf8")
        str = ""
        f.write(x + "\n")
        for y in data:
            if y.location == x:
                hash = ""
                for z in range(int(y.wind_force)):
                    hash += "#"
                str += f"{y.hour}:{y.minute} " + hash + "\n"
        f.write(str)
        f.close()

    print("6.feladat\nA fájlok elkészültek")

def main():
    task2()
    task3()
    task4()
    task5()
    task6()

if __name__ == "__main__":
    main()