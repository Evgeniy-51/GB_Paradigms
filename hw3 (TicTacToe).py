"""
● Контекст
Вероятнее всего, вы с детства знакомы с этой игрой. Пришло время реализовать её. Два игрока по очереди ставят крестики
и нолики на игровое поле. Игра завершается когда кто-то победил, либо наступила ничья, либо игроки отказались играть.
● Задача
Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее подходящими. Можете
реализовать доску как угодно - как одномерный массив или двумерный массив (массив массивов). Можете использовать как
правила, так и хардкод, на своё усмотрение. Главное, чтобы в игру можно было поиграть через терминал с вашего компьютера.
"""

import os
import subprocess


def clear():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)


def draw_field():
    clear()
    print()
    for i in range(0, 9, 3):
        print('-' * 13 + ' ' * 8 + '-' * 13)
        print(f"| {cells[i]} | {cells[i + 1]} | {cells[i + 2]} |        | {9 - i - 2} | {9 - i - 1} | {9 - i} |")
    print('-' * 13 + ' ' * 8 + '-' * 13 + '\n')


def check_win(gamer):
    def foo(a): return a == gamer

    return any([all(map(foo, cells[:3])),
                all(map(foo, cells[3:6])),
                all(map(foo, cells[6:])),
                all(map(foo, cells[::3])),
                all(map(foo, cells[1::3])),
                all(map(foo, cells[2::3])),
                all(map(foo, (cells[0], cells[4], cells[8]))),
                all(map(foo, (cells[2], cells[4], cells[6])))
                ])


cells = [' '] * 9
num_block_keys = [7, 8, 9, 4, 5, 6, 1, 2, 3]
gamer = 'X'
is_win = False
step = 0

while True:
    draw_field()
    print(f"Игрок  {gamer}:")
    print("введите номер поля (подсказка справа)")
    print("или Q для завершения работы программы")
    move = False

    while not move:
        move = input(" >> ")
        if move.isdigit() and 0 < int(move) < 10:
            move = num_block_keys[int(move) - 1]
        elif move in 'qQ':
            print("Игра завершена по вашему желанию!")
            input(" >> ")
            exit(0)
        else:
            print("Пожалуйста, вводите только числа от 1 до 9!")
            move = False
            continue

        if cells[move - 1] == ' ':
            cells[move - 1] = gamer
        else:
            print("Это поле уже занято, введите другое")
            move = False
            continue

    step += 1
    if step > 4:
        is_win = check_win(gamer)

    if is_win:
        draw_field()
        print(f"{gamer} победил!\n")
        input(' >> ')
        break

    if step == 9:
        draw_field()
        print("Ничья!\n")
        input(' >> ')
        break

    gamer = 'O' if gamer == 'X' else 'X'
