post1 = input('Введите первый пост: ')
post2 = input('Введите второй пост: ')
post3 = input('Введите третий пост: ')

len1 = len(post1)
len2 = len(post2)
len3 = len(post3)

if (len1 >= len2 and len1 >= len3):
    print(post1)
if (len2 >= len1 and len2 >= len3):
    print(post2)
if (len3 >= len2 and len3 >= len1):
    print(post3)



