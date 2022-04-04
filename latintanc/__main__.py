from collections import Counter
class Dance:
    def __init__(self, dancers : list = [], style : str = ""):
        self.dancers = dancers
        self.style = style

data = []

def load():
    current = Dance([], "")
    i = 0
    for x in open("tancrend.txt", "r", encoding = "utf-8"):
        
        if x.islower():
            current.style = x.strip()
            if i != 0:
                data.append(current)
                current = Dance([], "")
        else:
            current.dancers.append(x.strip())
        i += 1
        

def task1():
    print("1.feladat")
    print(f"Elsőként bemutatott tánc: {data[0].style}\nUtolsóként bemutatott tánc: {data[-1].style}")

def task2():
    print("2.feladat")
    i = 0
    for x in data:
        if x.style == "samba":
            i += 1
    print(f"Összesen {str(i)} pár táncolt sambát.")

def task3():
    dances = [x for x in data if "Vilma" in x.dancers]

    print("3.feladat")
    print(f"Vilma az alábbi táncokban szerepelt:")
    for x in dances:
        print(f"{' - '.join(x.dancers)}: {x.style}")

def task4():
    print("4.feladat")
    name = input("Kérem adja meg Vilma melyik táncára kíváncsi: ")
    for x in data:
        if "Vilma" in x.dancers and name == x.style:
            dancers = x.dancers
            dancers.remove("Vilma")
            dancers = dancers[0]

            print(f"A {name} bemutatóján Vilma párja {dancers} volt")
            return
    print(f"Vilma nem táncolt {name}-t.")

def task5():
    print("5.feladat")
    boys = []
    girls = []
    for x in data:
        if x.dancers[0] not in girls:
            girls.append(x.dancers[0])
        if x.dancers[1] not in boys:
            boys.append(x.dancers[1])
    f = open("szereplok.txt", "w", encoding = "utf-8")
    f.write(f"Fiúk: {', '.join(boys)}\n")
    f.write(f"Lányok: {', '.join(girls)}")
    f.close()
    print("szereplok.txt létrehozva.")

def task6():
    print("6.feladat")
    boys = []
    girls = []
    b_string = ""
    g_string = ""
    for x in data:
        girls.append(x.dancers[0])
        boys.append(x.dancers[1])
    a_boys = Counter(boys).most_common()
    a_girls = Counter(girls).most_common()
    b_int = 0
    g_int = 0
    for x in a_boys:
        if b_int <= x[1]:
            b_string += x[0] + ", "
            b_int = x[1]
    for x in a_girls:
        if g_int <= x[1]:
            g_string += x[0] + ", "
            g_int = x[1]
        
    print(f"Legtöbbször szerepelt fiú(k) neve(i): {b_string}")
    print(f"Legtöbbször szerepelt lány(ok) neve(i): {g_string}")

def main():
    load()
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()

if __name__ == "__main__":
    main()