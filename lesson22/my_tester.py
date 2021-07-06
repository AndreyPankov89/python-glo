import random
import os
import jsonpickle

jsonpickle.set_encoder_options('json',indent=4, separators=(',',':'), ensure_ascii=False)

class File_IO:
    def __init__(self,filename):
        self.filename = filename


    def write(self, value):
        file = open(self.filename,'w',encoding='utf-8')
        file.write(jsonpickle.encode(value))
        file.close()
    
    def read(self):
        file = open(self.filename, 'r', encoding='utf-8')
        lines = file.read()
        print(type(lines))
        file.close()
        return jsonpickle.decode(lines)
    

class QuestionStorage:
    def __init__(self):
        self.file = File_IO('questions_list.json')
        if os.path.exists('questions_list.json'):
            self.__questions_list = self.file.read()
        else:
            self.__questions_list = [
                Question('Сколько будет два плюс два умноженное на два?', '6'),
                Question('Бревно нужно рааспилить на 10 частей, сколько нужно распилов?', '9'),
                Question('На двух руках 10 пальшев, сколько пальцев на пяти рука?', '25'),
                Question('Укол делают каждые полчаса, сколько нужно минут для трех уколов?', '60'),
                Question('Пять свечей горело, две потухли, сколько осталось?', '2')
            ]
            self.file.write(self.__questions_list)

    def get_all(self):
        count = len(self.__questions_list)
        not_using_questions = [i for i in range(count)]
        question_list = []
        for i in range(count):
            while True:
                question_number = random.randint(0, count-1)
                if (question_number in not_using_questions):
                    question_list.append(self.__questions_list[question_number])
                    not_using_questions.remove(question_number)
                    break
        return question_list

    def append(self,question, answer):
        if (len(question) == 0):
            raise Exception('Нельзя добавлять пустой вопрос')
        if (not answer.isdigit()):
            raise Exception('Ответ должен быть числом')
        new_question = Question(question,answer)
        self.__questions_list.append(new_question)
        self.file.write(self.__questions_list)
    
    def remove(self):
        for i in range(len(self.__questions_list)):
            print(f'{i+1}. {self.__questions_list[i].question}')
        while True:
            user_answer_string = input('Введите номер удаляемого вопроса: ')
            if (user_answer_string.isdigit()):
                user_answer = int(user_answer_string)
                if (user_answer in range(1, len(self.__questions_list)+1)):
                    break
                else:
                    print(f'Вопроса {user_answer} не существует')
            else:
                print('Ответ должен быть числом')
        
        
        
        print(f'Вы дествительно хотите удалить вопрос {self.__questions_list[user_answer-1].question}? (y/n) ')
        confirm = input()
        if (confirm.lower() == 'y'):
            self.__questions_list.pop(user_answer-1)
        self.file.write(self.__questions_list)

class Question:
    def __init__(self, question,answer):
        self.__question = question
        self.__answer = answer
    
    def check_answer(self, user_answer):
        if (user_answer == self.__answer):
            return True
        else:
            return False
    @property
    def question(self):
        return self.__question

class User:
    def __init__(self, user_name):
        self.__user_name = user_name
        self.__count_right_answers = 0
        self.__result = ''
        
    def inc_right_answer(self):
        self.__count_right_answers += 1
    
    def calculate_results(self, total_count):
        results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный' ,'Талант', 'Гений']
        persentage = self.__count_right_answers / total_count

        for i in range(6):
            if (persentage <= (i+1)/6):
                self.__result = results[i]
                return results[i]
    def string_results(self):
        return [self.__user_name,str(self.__count_right_answers), self.__result]
    @property
    def result(self):
        return self.__result
    @property
    def count_right_answers(self):
        return self.__count_right_answers
    @property
    def name(self):
        return self.__user_name

class UserResultStorage:
    def __init__(self):
        self.__file = File_IO('results.json')
        self.__results = self.__file.read() if os.path.exists('results.json') else []
    @property
    def results(self):
        return self.__results
    
    def append(self,result):
        self.__results.append(result)
        self.__file.write(self.__results)
    
def print_table(lines):
    
    print('{0:^15}|{1:^30}|{2:^30}'.format('Имя','Кол-во правильных ответов','Результат'))
    for line in lines:
        #name, count, result = line
        print('{0:<15}|{1:^30}|{2:^30}'.format(line.name,line.count_right_answers,line.result))
    

question_storage = QuestionStorage()
result_storage = UserResultStorage()
    
def quiz():
    questions = question_storage.get_all()
    user = User(input('Как вас зовут? '))

    for i in range(len(questions)):
        print(f'Вопрос {i+1}: {questions[i].question}')
        user_answer = input('Ваш ответ: ')
        if (questions[i].check_answer(user_answer)):
            user.inc_right_answer()     

    user.calculate_results(len(questions))
    print(f'{user.name}, Ваш результат {user.result}')
    result_storage.append(user)

while True:
    print('Приветствуем Вас в системе тестирования, что Вы хотите сделать?')
    print('1 - Пройти тесттирование')
    print('2 - Добавить вопрос')
    print('3 - Удалить вопрос')
    print('4 - Посмотреть таблицу результатов')
    print('0 - Выйти из программы')
    while True:
        user_answer_string = input('>: ')
        if (user_answer_string.isdigit()):
            user_answer = int(user_answer_string)
            if (user_answer in range(0, 5)):
                break
            else:
                print(f'Я не понял, что вы хотите сделать, повторите ввод')
        else:
            print('Ответ должен быть числом')

    if (user_answer == 1):
        quiz()
    elif (user_answer == 2):
        question = input('Введите текст вопроса: ')
        answer = input('Введите ответ на вопрос: ')
        question_storage.append(question, answer)
    elif (user_answer == 3):
        question_storage.remove()
    elif (user_answer == 4):
        print_table(result_storage.results)
    else:
        break

print('До новых встреч!')