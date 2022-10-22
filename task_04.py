# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

# lst1=[i for i in range(100)]
# lst2=[i fir i in lst1 if i%10==0]

spisok_koef = []
k_stepen = int(input('Введите степень многочлена: '))
for i in (range(k_stepen + 1)):
    rand_num = randint(0, 2)
    spisok_koef.append(rand_num)

# spisok_koef=[randint(-10,10) for _ in range(k+1)]

print(spisok_koef)
polynomial = ''
for i in range(len(spisok_koef)):
    # for i,koef in enumerate(spisok_koef):
    print(len(spisok_koef),' ',i)
    if len(polynomial) > 0 and spisok_koef[i] > 0:
        polynomial = polynomial + '+'
    if spisok_koef[i] == 0:
        continue
    if k_stepen-i == 1 and spisok_koef[i] > 1:
        polynomial = polynomial + str(spisok_koef[i]) + 'x'
        continue
    else:
        if k_stepen-i == 1:
            polynomial = polynomial + 'x'
            continue
    
    if spisok_koef[i] == 1 and k_stepen-i>0:
        polynomial = polynomial + 'x^' + str(k_stepen-i)
        continue

    polynomial = polynomial + str(spisok_koef[i]) + 'x^' + str(k_stepen-i)
if spisok_koef[-1] != 0:
    polynomial = polynomial[:len(polynomial)-3]
polynomial = polynomial + '=0'

print('Полученный многочлен : ', polynomial)
filename = "polinomial.txt"
with open(filename, 'w') as file:
    file.write(f'\n{polynomial}')
