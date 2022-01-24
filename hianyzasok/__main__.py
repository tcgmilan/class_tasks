data = []

def task1():
    i = 0
    for x in data:
        i += len(x.students)
    print("2.feladat")
    print(f"A naplóban {i} bejegyzés van.")

def task2():
    cert = 0
    uncert = 0
    for x in data:
        for y in x.students:
            for z in y.pattern:
                if z == "X":
                    cert += 1
                elif z == "I":
                    uncert += 1
    print("3.feladat")
    print(f"Az igazolt hiányzások száma {cert}, az igazolatlanoké {uncert}.")

def task4():
    print("5.feladat")
    day = hetnapja(int(input("Adjon meg egy hónapot: ")), int(input("Adjon meg egy napot: ")))
    print(f"Azon a napon {day} volt.")

def task5():
    count = 0
    day = input("Kérem adjon meg egy napot (hétfő, kedd, szerda, csütörtök, péntek, szombat, vasárnap): ")
    i = int(input("Kérem adjon meg egy órát: "))
    for x in data:
        if hetnapja(int(x.month), int(x.day)) == day:
            for y in x.students:
                if y.pattern[i - 1] in ["X", "I"]:
                    count += 1
    print(f"Ekkor összesen {count} óra hiányzás történt.")

def hetnapja(month : int, day : int):
    days = ["vasárnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"]
    daynum = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    dayserialnum = (daynum[month - 1] + day) % 7
    weekday = days[dayserialnum]
    return weekday

def data_load():
    global day, students
    day = None
    i = 0

    class Day:
        def __init__(self, month : int, day : int, students : list):
            self.month = month
            self.day = day
            self.students = students


    class Student:
        def __init__(self, name : str, pattern : list, skips : int):
            self.name = name
            self.pattern = pattern
            self.skips = skips
    
    f = open("naplo.txt", "r", encoding = "utf8").readlines()
    last = len(f) - 1
    for l in f:
        if l[0] == "#" and i == 0:
            day = Day(l.split(" ")[1], l.split(" ")[2], [])
        elif l[0] == "#":
            data.append(day)
            day = Day(l.split(" ")[1], l.split(" ")[2], [])
        elif i == last:
            skips = 0
            for x in l.split(" ")[2].strip():
                if x in ["X", "I"]:
                    skips += 1
            
            day.students.append(Student(l.split(" ")[0] + " " + l.split(" ")[1], [x for x in l.split(" ")[2].strip()], skips))
            data.append(day)
        else:
            skips = 0
            for x in l.split(" ")[2].strip():
                if x in ["X", "I"]:
                    skips += 1
            day.students.append(Student(l.split(" ")[0] + " " + l.split(" ")[1], [x for x in l.split(" ")[2].strip()], skips))
        i += 1

def main():
    data_load()
    task1()
    task2()
    task4()
    task5()
    
if __name__ == "__main__":
    main()