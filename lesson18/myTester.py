import random
questions = [
    'Сколько будет два плюс два умноженное на два?', 
    'Бревно нужно рааспилить на 10 частей, сколько нужно распилов?',
    'На двух руках 10 пальшев, сколько пальцев на пяти рука?',
    'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
    'Пять свечей горело, две потухли, сколько осталось?'
]

answers = [6, 9, 25, 60, 2]
results = ['Идиот', 'Кретин', 'Дурак', 'Нормальный' ,'Талант', 'Гений']

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

def quiz():
    count_right_answers = 0
    user_name = input('Как вас зовут? ')
    questions_list = generate_questions_list(len(questions))
    for i in range(len(questions)):
        question_number = questions_list[i]
        print(f'Вопрос {i+1}: {questions[question_number]}')
        user_answer = int(input('Ваш ответ: '))
        right_answer = answers[question_number]
        if (user_answer == right_answer):
            count_right_answers += 1 
    print(f'{user_name}, Ваш результат {results[count_right_answers]}')

while True:
    quiz()
    continue_game = input('Начать новый опрос? (y/n) ')
    if (continue_game.lower() == 'y'):
        continue
    else:
        break