import random
class QuestionStorage:
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
    @property
    def name(self):
        return self.__user_name

class UserResultStorage:
    def __init__(self, user):
        self.__count_right_answers = 0
        self.__user_name = user.name
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

class File_IO:
    def __init__(self,filename,sep):
        self.filename = filename
        self.sep = sep

    def __form_output_string(self, *args):
        return self.sep.join(args)

    def write(self, *args):
        file = open(self.filename,'a',encoding='utf-8')
        file.write(self.__form_output_string(*args))
        file.close()
    
    def read(self):
        file = open(self.filename, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()
        return [line.strip('\n').split(self.sep) for line in lines]
    

questions = [
    QuestionStorage('Сколько будет два плюс два умноженное на два?', 6),
    QuestionStorage('Бревно нужно рааспилить на 10 частей, сколько нужно распилов?', 9),
    QuestionStorage('На двух руках 10 пальшев, сколько пальцев на пяти рука?', 25),
    QuestionStorage('Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 60),
    QuestionStorage('Пять свечей горело, две потухли, сколько осталось?', 2)
]
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


def print_table(lines):
    
    print('{0:^15}|{1:^30}|{2:^30}'.format('Имя','Кол-во правильных ответов','Результат'))
    for line in lines:
        name, count, result = line
        print('{0:<15}|{1:^30}|{2:^30}'.format(name,count,result))

def quiz():
    questions_count = len(questions)
    questions_list = generate_questions_list(questions_count)
    result_storage = UserResultStorage(user)
    
    for i in range(questions_count):
        question_number = questions_list[i]
        print(f'Вопрос {i+1}: {questions[question_number].question}')

        while True:
            user_answer_string = input('Ваш ответ: ')
            if (user_answer_string.isdigit()):
                user_answer = int(user_answer_string)
                break
            else:
                print('Ответ должен быть числом')
        
        if (questions[question_number].check_answer(user_answer)):
            result_storage.inc_right_answer()
    result_storage.calculate_results(questions_count)
    print(f'{user.name}, Ваш результат {result_storage.result}')
    file.write(*result_storage.string_results())
    

while True:
    user = User(input('Как вас зовут? '))
    file = File_IO('results.txt',':')
    quiz()
    continue_game = input('Начать новый опрос? (y/n) ')
    if (continue_game.lower() == 'y'):
        continue
    else:
        print_table(file.read())
        break