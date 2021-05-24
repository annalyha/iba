import datetime

class Air:

    def __init__(self, dir0, number0, plane0, time0, day0):
        self.dir = dir0
        self.number = number0
        self.plane = plane0
        self.time = time0
        self.day = day0

    def get_dir(self):
        return self.dir

    def get_number(self):
        return self.number

    def get_plane(self):
        return self.plane

    def get_time(self):
        return self.time

    def get_day(self):
        return self.day

    def __str__(self):
        return str(self.dir) + " " + str(self.number) + " " + str(self.day)

newAir = [
    Air("Москва", 123, "ТУ", 12.30, "понедельник"),
    Air("Рига", 345, "ТУ", 14.50, "вторник"),
    Air("Москва", 567, "АН", 15.00, "среда"),
    Air("Киев",  789, "АН", 15.30, "среда"),
    Air("Киев",  147, "ИЛ", 12.30, "четверг"),
    Air("Рига",  854, "ИЛ", 09.30, "понедельник"),
    Air("Киев", 258, "ТУ", 02.30, "вторник"),
]
d = input("Введите пункт назначения ")
for air in newAir:
   if air.get_dir() == d:
         print(air)

w = input("Введите день недели ")
for air in newAir:
    if air.get_day() == w:
        print(air)

