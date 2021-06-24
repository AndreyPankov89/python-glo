import random
import os
questions = [
    'Сколько будет два плюс два умноженное на два?', 
    'Бревно нужно рааспилить на 10 частей, сколько нужно распилов?',
    'На двух руках 10 пальшев, сколько пальцев на пяти рука?',
    'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
    'Пять свечей горело, две потухли, сколько осталось?'
]

answers = [6, 9, 25, 60, 2]

def generate_questions_list(count):
    not_using_questions = [i for i in range(count)]
    question_list = []
    for i in range(count):
        while True:
            question_number = random.randint(0, count-1)
            if (question_number in not_using_questions):
                question_list.append(question_number)
                not_using_questions.remove(question_number)
                break
    return question_list    

def calculate_results(total_count, right_answers):
    results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный' ,'Талант', 'Гений']
    persentage = right_answers / total_count

    for i in range(6):
        if (persentage <= (i+1)/6):
            return results[i]
    
def save_resuls(name, count_right_answers, result):
    file = open('results.txt',mode='a', encoding='utf-8')

    file.write(f'{name}:{result}:{count_right_answers}\n')
    file.close()

def print_table():
    file = open('results.txt',mode='r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    print('{0:^15}|{1:^30}|{2:^30}'.format('Имя','Кол-во правильных ответов','Результат'))
    for line in lines:
        name, count, result = line.strip('\n').split(':')
        print('{0:<15}|{1:^30}|{2:^30}'.format(name,count,result))

def quiz():
    count_right_answers = 0
    user_name = input('Как вас зовут? ')
    questions_count = len(questions)
    questions_list = generate_questions_list(questions_count)
    
    for i in range(questions_count):
        question_number = questions_list[i]
        print(f'Вопрос {i+1}: {questions[question_number]}')

        while True:
            user_answer_string = input('Ваш ответ: ')
            if (user_answer_string.isdigit()):
                user_answer = int(user_answer_string)
                break
            else:
                print('Ответ должен быть числом')
        right_answer = answers[question_number]
        if (user_answer == right_answer):
            count_right_answers += 1 
    result = calculate_results(questions_count,count_right_answers)
    print(f'{user_name}, Ваш результат {result}')
    save_resuls(user_name,count_right_answers, result)
    

while True:
    quiz()
    continue_game = input('Начать новый опрос? (y/n) ')
    if (continue_game.lower() == 'y'):
        continue
    else:
        print_table()
        break