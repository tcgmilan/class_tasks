class User:
    def __init__(self, id : str, answer : str):
        self.id = id
        self.answer = answer.replace("X", "-")
data = []

f = open("valaszok.txt", "r", encoding = "utf8").readlines()
z = open("valaszok.txt", "r", encoding = "utf8")

solution = [x for x in f[0]]
solution.remove("\n")

next(z)

for x in z:
    data.append(User(x.split(" ")[0], x.split(" ")[1]))

def task1():
    print("1.feladat: Az adatok beolvasása")

def task2():
    print(f"2. feladat: A vetélkedőn {len(data)} versenyző indult.")

def task3():
    y = input("3.feladat: A versenyző azonosítója = ")
    for x in data:
        if x.id == y:
            print(f"A versenyző válasza: {x.answer}")
            task4(x.answer)
            break

def task4(x):
    global solution
    res = []
    i = 0
    for y in x:
        try:
            if y == solution[i]:
                res.append("+")
            else:
                res.append(" ")
            i += 1
        except:
            break
    print("4.feladat:")
    print("".join(solution)+"\n"+"".join(res))

def task5():
    i = int(input("5. feladat: A feladat sorszáma = "))
    c = 0
    for x in data:
        if x.answer[i - 1] == solution[i - 1]:
            c += 1
    r = len(data) - c
    print(f"A feladatra {r} fő, a versenyzők ?%-a adott helyes választ!")


def main():
    task1()
    task2()
    task3()
    task5()



if __name__ == "__main__":
    main()