import random
import os

class FileProvider:
    def get(self, path):
        file = open(path, 'r')
        data = file.read()
        file.close()
        return data

    def append(self, path, data):
        file = open(path, 'a')
        data = file.write(data)
        file.close()

    def exists(self, path):
        return os.path.exists(path)

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionStrorage:
    def __init__(self):
        file_name = 'question.txt'
        file_provider = FileProvider()
        if file_provider.exists(file_name):
            self.question = []
            file_data = file_provider.get(file_name).strip('\n')
            file_data = file_data.split('\n')
            for data in file_data:
                data_line = data.split('#')
                question = data_line[0]
                answer = data_line[1]
                new_question = Question(question, int(answer))
                self.question.append(new_question)
        else:
            data = [
                Question('Сколько будет 2 + 2 * 2', 6),
                Question('Бревно надо распелить на 10 частей, сколько нужно пилов', 9),
                Question('На 2х руках 10 пальце, сколько на 5', 25),
                Question('укол делают каждые пол часа, сколько нужно минут для 3х уколов', 60),
                Question('5 свечей горело, 2 потухли. Сколько свечей осталось', 2)
            ]
            self.question = data
            for char in data:
                info = char.text+'#'+str(char.answer)+'\n'
                file_provider.append(file_name, info)
                
    def get_all(self):
        return self.question
    def add_question(self, question):
        file_name = 'question.txt'
        file_provider = FileProvider()
        data = f'{question.text}#{question.answer}\n'
        file_provider.append(file_name, data)

qs = QuestionStrorage()

class User:
    def __init__(self, name, count_right_answers=0, result='Неизвестно'):
        self.name = name
        self.count_right_answers = count_right_answers
        self.result = result
    def inc_righta_answer(self):
        self.count_right_answers +=1
    def calculate_result(self, count_questions):
        right_answers_percents = self.count_right_answers * 100 // count_questions
        results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']
        self.result = results[right_answers_percents // 20]
        return self.result

class UsersResultStorage:
    def safe(self, user):
        file_name = 'result.txt'
        data = f'{user.name} {user.count_right_answers} {user.result}\n'
        file_provider = FileProvider()
        file_provider.append(file_name, data)

    def get_all(self):
        file_name = 'result.txt'
        file_provider = FileProvider()
        data = file_provider.get(file_name).strip('\n')
        data = data.split('\n')
        users = []
        for string in data:
            string_line = string.split(' ')
            player = User(string_line[0], string_line[1], string_line[2])
            users.append(player)
        return users


def show_user_results(table_result):
    if table_result.lower() == 'y':
        name = 'Имя'
        count_right_answers = 'Кол-во правильных ответов'
        result = 'Результат'
        print(f'{name:15}{count_right_answers:30}{result:15}')

        users = user_result.get_all()
        for player in users:
            print(f'{player.name:15}{player.count_right_answers:30}{player.result:15}')

def add_new_question():
    text = input('Введите текст вопроса \n')
    answer = int(input('Введите ответ \n'))
    new_question = Question(text, answer)
    qs.add_question(new_question)


user_result = UsersResultStorage()
while True:
    questions = qs.get_all()
    user = User(input('Как вас зовут? '))

    count_questions = len(questions)
    for i in range(len(questions)):
        print(f'Вопрос №{i + 1}')
        random_index = random.randint(0, len(questions) - 1)
        print(questions[random_index].text)
        while True:
            user_answer = input()
            if user_answer.isdigit():
                pass
            else:
                print('Пожалуйста введите число')
                continue
            break
        right_answer = questions[random_index].answer
        if int(user_answer) == right_answer:
            user.inc_righta_answer()
        questions.pop(random_index)

    user.calculate_result(count_questions)

    print('Количество правильных ответов =', user.count_right_answers)
    print(f'{user.name}, -колличество правильных ответов: , {user.result}')
    user_result.safe(user)

    user_question = input('Хотите добавить новый вопрос? y/n ')
    if user_question.lower() == 'y':
        add_new_question()

    continue_game = input('Повторим? y/n ')
    if (continue_game.lower() == 'y'):
        continue
    else:
        break

table_result = input('Вывести таблицу результатов? да или нет')
show_user_results(table_result)