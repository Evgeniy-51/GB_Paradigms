"""
● Условие
На вход подается число n.
● Задача
Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.
"""


def show_table(n):
    for i in range(1, 10):
        for k in range(1, n + 1):
            print(f"{k} * {i} ={i * k:>2}", end='\t\t')
        print()


if __name__ == '__main__':
    MAX_VALUE = 6000
    try:
        n = int(input("Ведите число N: "))
        if n <= 0 or n > MAX_VALUE:
            raise ValueError()
    except:
        print("Вводимое значение должно быть целым и положительным числом до 6000!")
    else:
        show_table(n)

"""
Парадигмы:
  - процедурная, т.к. программа имеет линейную структуру, но ее удобно разделить на две части: ввод и верификация
  данных и непосредственно вывод таблицы
  - императивная, т.к. программа представляет собой набор простых инструкций, при последовательном выполнении которых
  достигается желаемый результат 
"""