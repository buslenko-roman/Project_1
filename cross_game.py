print('Добро пожаловать в игру!')
gamer1 = input('Введите имя первого игрока - ')
gamer2 = input('Введите имя второго игрока - ')
print()

cross_game = [['A1', '|', 'A2', '|', 'A3'],
               ['-', ' |', '-', ' |', '-'],
               ['B1', '|', 'B2', '|', 'B3'],
               ['-', ' |', '-', ' |', '-'],
               ['C1', '|', 'C2', '|', 'C3']
               ]

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('Уважаемые игроки -', gamer1, ',',  gamer2, '!\n'
      'Перед Вами поле для игры в крестики-нолики.\n'
      'Для того, чтобы поставить крестик или нолик в нужной клетке введите ее обозначение.')
print()
print('Обращаем Ваше внимание на то, что игроки ходят в порядке указанных имён.\n'
      'Обозначения клеток записываются только латиницей.\n'
      'Удачного поединка!')
print()

round1 = input('Ход первого игрока!\n'
               'Где вы хотите поставить крестик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round1:
           row[i] = 'X '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('Отличный ход!')
print()
print('_________________________')

round2 = input('Ход второго игрока!\n'
               'Где вы хотите поставить нолик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round2:
           row[i] = 'O '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('Ваша битва будет легендарной!')
print()
print('_________________________')

round3 = input('Снова ход первого игрока!\n'
               'Где вы хотите поставить крестик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round3:
           row[i] = 'X '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('На один ход ближе к победе!')
print()
print('_________________________')

round4 = input('Снова ход второго игрока!\n'
               'Где вы хотите поставить нолик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round4:
           row[i] = 'O '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('Первому игроку грозит опасность!')
print()
print('_________________________')

round5 = input('Снова ход первого игрока!\n'
               'Где вы хотите поставить крестик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round5:
           row[i] = 'X '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('Это становится похоже на Agni Kai!')
print()

def checking_winner(a):
    a_1 = a[0][0]
    a_2 = a[0][2]
    a_3 = a[0][4]
    b_1 = a[2][0]
    b_2 = a[2][2]
    b_3 = a[2][4]
    c_1 = a[4][0]
    c_2 = a[4][2]
    c_3 = a[4][4]
    x_1 = [a_1, a_2, a_3]
    x_2 = [a_1, b_2, c_3]
    x_3 = [a_3, b_2, c_1]
    x_4 = [a_1, b_1, c_1]
    x_5 = [a_2, b_2, c_2]
    x_6 = [a_3, b_3, c_3]
    x_7 = [b_1, b_2, b_3]
    x_8 = [c_1, c_2, c_3]
    o_1 = [a_1, a_2, a_3]
    o_2 = [a_1, b_2, c_3]
    o_3 = [a_3, b_2, c_1]
    o_4 = [a_1, b_1, c_1]
    o_5 = [a_2, b_2, c_2]
    o_6 = [a_3, b_3, c_3]
    o_7 = [b_1, b_2, b_3]
    o_8 = [c_1, c_2, c_3]
    if all(element == 'X ' for element in x_1):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_2):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_3):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_4):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_5):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_6):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_7):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_8):
        print('Первый игрок победил')
        quit()
    if all(element == 'O ' for element in o_1):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_2):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_3):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_4):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_5):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_6):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_7):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_8):
        print('Второй игрок победил')
        quit()
    else:
        print('_________________________')

checking_winner(cross_game)

round6 = input('Снова ход второго игрока!\n'
               'Где вы хотите поставить нолик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round6:
           row[i] = 'O '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('Напряжение растет!')
print()

checking_winner(cross_game)

round7 = input('Снова ход первого игрока!\n'
               'Где вы хотите поставить крестик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round7:
           row[i] = 'X '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('Развязка близится!')
print()

checking_winner(cross_game)

round8 = input('Снова ход второго игрока!\n'
               'Где вы хотите поставить нолик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round8:
           row[i] = 'O '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()
print('Битва до победного конца!')
print()

checking_winner(cross_game)

def checking_winner_drow(a):
    a_1 = a[0][0]
    a_2 = a[0][2]
    a_3 = a[0][4]
    b_1 = a[2][0]
    b_2 = a[2][2]
    b_3 = a[2][4]
    c_1 = a[4][0]
    c_2 = a[4][2]
    c_3 = a[4][4]
    x_1 = [a_1, a_2, a_3]
    x_2 = [a_1, b_2, c_3]
    x_3 = [a_3, b_2, c_1]
    x_4 = [a_1, b_1, c_1]
    x_5 = [a_2, b_2, c_2]
    x_6 = [a_3, b_3, c_3]
    x_7 = [b_1, b_2, b_3]
    x_8 = [c_1, c_2, c_3]
    o_1 = [a_1, a_2, a_3]
    o_2 = [a_1, b_2, c_3]
    o_3 = [a_3, b_2, c_1]
    o_4 = [a_1, b_1, c_1]
    o_5 = [a_2, b_2, c_2]
    o_6 = [a_3, b_3, c_3]
    o_7 = [b_1, b_2, b_3]
    o_8 = [c_1, c_2, c_3]
    if all(element == 'X ' for element in x_1):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_2):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_3):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_4):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_5):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_6):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_7):
        print('Первый игрок победил')
        quit()
    if all(element == 'X ' for element in x_8):
        print('Первый игрок победил')
        quit()
    if all(element == 'O ' for element in o_1):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_2):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_3):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_4):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_5):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_6):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_7):
        print('Второй игрок победил')
        quit()
    if all(element == 'O ' for element in o_8):
        print('Второй игрок победил')
        quit()
    else:
        print('Увы, ничья :(')

round9 = input('Снова ход первого игрока!\n'
               'Где вы хотите поставить крестик?\n'
               'Введите обозначение клетки - ')
print()

for row in cross_game:
   for i, x in enumerate(row):
       if x == round9:
           row[i] = 'X '

for i in range(len(cross_game)):
    for j in range(len(cross_game[i])):
        print(cross_game[i][j], end = ' ')
    print()

print()

checking_winner_drow(cross_game)