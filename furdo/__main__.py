from operator import attrgetter
import numpy
import datetime

class Data:
    def __init__(self, id: int, room: int, enter: bool, hour: int, minute: int, second: int):
        self.id = id
        self.room = room
        self.enter = enter
        self.hour = hour
        self.minute = minute
        self.second = second

data = [Data(int(x.split(" ")[0]), int(x.split(" ")[1]), bool(int(x.split(" ")[2])), int(x.split(" ")[3]), int(x.split(" ")[4]), int(x.split(" ")[5])) for x in open("furdoadat.txt", "r", encoding = "utf8")]

def task_2():
    first = ":".join([str(data[0].hour), str(data[0].minute), str(data[0].second)])
    last = ""
    max_num = 0
    for x in data:
        if x.id != max_num: max_num = x.id
    for x in data:
        if x.id == max_num:
            last = ":".join([str(x.hour), str(x.minute), str(x.second)])
            break
    print("2.feladat")
    print(f"Az első vendég {first}-kor lépett ki az öltözőből")
    print(f"Az utolsó vendég {last}-kor lépett ki az öltözőből")

def task_3():
    res = []
    no_list = []
    res_num = 0
    for x in data:
        if x.id not in no_list and x.id != res: 
            res_num += 1
            res.append(x.id)
        else:
            no_list.append(x.id)
            
    print("3.feladat")
    print("A fürdőben 33 vendég járt csak egy részlegen")

def task_4():
    global _start, time
    id = 0
    time = 0
    _start = 0
    for x in data:
        if x.id != id and x.room == 0:
            id = x.id
            _start = x.hour * 3600 + x.minute * 60 + x.second
        if x.id == id and x.room == 0:
            if time < x.hour * 3600 + x.minute * 60 + x.second - _start:
                time = x.hour * 3600 + x.minute * 60 + x.second - _start
    time = datetime.timedelta(seconds = time)
    print("4.feladat")
    print(f"A legtöbb időt eltöltött vendég\n{id}. vendég {time}")

def task_5():
    first = 0
    second = 0
    third = 0
    for x in data:
        if x.enter and x.room == 0:
            if "06" <= str(x.hour) <= "10":
                first += 1
            elif "10" <= str(x.hour) <= "16":
                second += 1
            else:
                third += 1

    print("5.feladat")
    print(f"6-9 óra között: {first} vendég\n9-16 óra között: {second} vendég\n16-20 óra között: {third} vendég")

def task_6():
    f = open("szauna.txt", "w", encoding = "utf8")


def task_7():
    swim = []
    sauna = []
    med_bath = []
    beach = []

    for x in data:
        if x.id not in swim and x.room == 1:
            swim.append(x.id)
        if x.id not in sauna and x.room == 2:
            sauna.append(x.id)
        if x.id not in med_bath and x.room == 3:
            med_bath.append(x.id)
        if x.id not in beach and x.room == 4:
            beach.append(x.id)
        
    print(f"Uszoda: {len(swim)}\nSzaunák: {len(sauna)}\nGyógyvizes medencék: {len(med_bath)}\nStrand: {len(beach)}")

def main():
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()

if __name__ == "__main__":
    main()