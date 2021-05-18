from math import ceil

task_count = int(input('Введите количество задач '))
task_per_day = int(input('Сколько задач вы решаете в день? '))

print(ceil(task_count / task_per_day))