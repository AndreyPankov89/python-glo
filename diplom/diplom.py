import os
import jsonpickle as jsp

jsp.set_encoder_options('json',indent=4, separators=(',',':'), ensure_ascii=False)

class File_IO:
    def __init__(self,filename):
        self.filename = filename


    def write(self, value):
        file = open(self.filename,'w',encoding='utf-8')
        file.write(value)
        file.close()
    
    def read(self):
        file = open(self.filename, 'r', encoding='utf-8')
        lines = file.read()
        file.close()
        return lines


class School:
    def __init__(self, name, adderess):
        self.__name = name
        self.__address = adderess
        self.__students = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property 
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,address):
        self.__address = address

    @property
    def count_students(self):
        print(type(self.__students))
        return len(self.__students)

    def add_student(self,student):
        self.__students.append(student)

    def delete_student(self, index):
        print('Вы действительно хотите удалить {}?'.format(self.__students[index].name))
        confirm = input()
        if (confirm.lower() == 'y'):
            self.__students.pop(index)


    def get_all_students(self):
        return self.__students
    
class Student():
    def __init__(self,name, age, class_number):
        self.__name, self.__age, self.__class_number = name, age, class_number

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age

    @property
    def class_number(self):
        return self.__class_number

    @class_number.setter
    def class_number(self, class_number):
        self.__class_number = class_number

class Storage():
    def __init__(self,path):
        self.__storage = []
        self.__path = path
        self.__file = File_IO(self.__path)
        if (os.path.exists(self.__path)):
            self.__storage = jsp.decode(self.__file.read())

    def get_all(self):
        return self.__storage

    def count(self):
        return len(self.__storage)

    def add(self, item):
        self.__storage.append(item)
        self.save()

    def edit(self, index,value):
        self.__storage[index] = value
        self.save()

    def remove(self,n):
        self.__storage.pop(n)
        self.save()

    def save(self):
        self.__file.write(jsp.encode(self.__storage))

class SchoolsStorage(Storage):
    def __init__(self):
        path = 'schools.json'
        super().__init__(path)


schools_storage = SchoolsStorage()

def print_schools():
    schools = schools_storage.get_all()
    print('{3:^5}|{0:^15}|{1:^30}|{2:^15}'.format('Название','Адрес','Кол-во учеников','#'))
    for i,line in enumerate(schools):
        #name, count, result = line
        print('{3:^5}|{0:<15}|{1:^30}|{2:^15}'.format(line.name,line.address,line.count_students, i+1))

def print_students(school):
    print('Школа {}'.format(school.name))
    print('{0:5}|{1:^15}|{2:^10}|{3:^15}'.format('#','ФИО','Класс','Возраст'))
    for i, line in enumerate(school.get_all_students()):
        #name, count, result = line
        print('{0:5}|{1:^15}|{2:^10}|{3:^15}'.format(i+1,line.name,line.class_number,line.age))

def delete_student():
    print_schools()
    while True:
        school_number = input('Введите номер школы ')
        if (school_number.isdigit() and int(school_number)<=schools_storage.count()):
            school_number_i = int(school_number)
            break
    

    print_students(schools_storage.get_all()[school_number_i-1])
    
    while True:
        student_number = input('Введите номер ученика ')
        if (student_number.isdigit() and int(student_number)<=schools_storage.get_all()[school_number_i-1].count_students):
            student_number_i = int(student_number)
            break
    schools_storage.get_all()[school_number_i-1].delete_student(student_number_i-1)

    schools_storage.save()

def add_student():
    print_schools()
    while True:
        school_number = input('Введите номер школы ')
        if (school_number.isdigit() and int(school_number)<=schools_storage.count()):
            school_number_i = int(school_number)
            break
    
    while True:
        name = input('Имя ')
        if (len(name)>3):
            break
        else:
            print('Слишком короткое имя')
            
    while True:
        input_class_number = input('Класс ')
        if (input_class_number.isdigit() and int(input_class_number) in range(1,12)):
            class_number = int(input_class_number)
            break
        else:
            print('Не верный ввод')
            
    while True:
        input_age = input('Возраст ')
        if (input_age.isdigit() and int(input_age) in range(6,20)):
            age = int(input_age)
            break
        else:
            print('Не верный ввод')

    student = Student(name, age, class_number)
    schools_storage.get_all()[school_number_i-1].add_student(student)
    schools_storage.save()

def add_school():
    while True:
        name = input('Название ')
        if (len(name)>3):
            break
        else:
            print('Слишком короткое название')
            
    while True:
        address = input('Адрес ')
        if (len(address)>3):
            break
        else:
            print('Слишком короткий адрес')
            
    school = School(name, address)
    schools_storage.add(school)
   
def edit_school():
    print_schools()
    while True:
        school_number = input('Введите номер школы ')
        if (school_number.isdigit() and school_number<schools_storage.count()):
            school_number_i = int(school_number)
            break
    old_school = schools_storage[school_number_i-1]
    
    while True:
        name = input('Название enter - оставить {} '.format(old_school.name))
        if (len(name)==0):
            name = old_school.name
        if (len(name)>3):
            break
        else:
            print('Слишком короткое название')
            
    while True:
        address = input('Адрес enter - оставить {} '.format(old_school.address))
        if (len(address)>3):
            break
        else:
            print('Слишком короткий адрес')
            
    school = School(name, address)
    schools_storage.edit(school_number_i, school)



def menu():
    print('1 - Добавить школу')
    print('2 - Получить информацию о школе')
    print('3 - Изменить информацию о школе')
    print('4 - Просмотреть учеников школы')
    print('5 - Добавить ученика в школу')
    print('6 - Исключить ученика из школы')
    print('0 - Выход')
    while True:
        user_input = input(':> ')
        if (user_input.isdigit() and int(user_input) in range(0,7)):
            return int(user_input)
        else:
            print('Команда не распознана')


while True:
    user_answer = menu()

    if (user_answer == 1):
        add_school()
    elif (user_answer == 2):
        print_schools()
    elif (user_answer == 3):
        edit_school()
    elif (user_answer == 4):
        print_schools()
        while True:
            school_number = input('Введите номер школы ')
            if (school_number.isdigit() and int(school_number)<=schools_storage.count()):
                school_number_i = int(school_number)
                break
        print_students(schools_storage.get_all()[school_number_i-1])
    elif (user_answer == 5):
        add_student()
    elif (user_answer == 6):
        delete_student()
    elif (user_answer == 0):
        print('Всего доброго!')
        break



