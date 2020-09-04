"""
На бесконечной координатной сетке находится муравей. Муравей может перемещаться на 1 клетку вверх (x,y+1),
вниз (x,y-1), влево (x-1,y), вправо (x+1,y), по одной клетке за шаг.
Клетки, в которых сумма цифр в координате X плюс сумма цифр в координате Y больше чем 25 недоступны муравью.
Например, клетка с координатами (59, 79) недоступна, т.к. 5+9+7+9=30, что больше 25.
Сколько клеток может посетить муравей, если его начальная позиция (1000,1000), (включая начальную клетку).

Прислать ответ в виде числа клеток, решения на языке Python и скрипта на языке JavaScript, отрисовывающего
на canvas площадь доступную муравью."""

import sys


def point():
    sys.stdout.write('')
    sys.stdout.flush()


def forward_and_up(in_x, in_y, sums=0):
    print('forward_and_up')
    x = in_x
    y = in_y
    c = 0
    while sums <= 25:
        c += 1
        if c % 500 == 0:
            point()
        xs = list(map(int, str(x)))
        ys = list(map(int, str(y)))
        sums = sum(xs) + sum(ys)
        if sums <= 25 and (x, y) not in points:
            points.append((x, y))
            x += 1
        else:
            x = in_x
            y += 1
            xs = list(map(int, str(x)))
            ys = list(map(int, str(y)))
            sums = sum(xs) + sum(ys)
            continue
    print()


def forward_and_down(in_x, in_y, sums=0):
    print('forward_and_down')
    x = in_x
    y = in_y
    c = 0
    while sums <= 25:
        c += 1
        if c % 10 == 0:
            point()
        xs = list(map(int, str(x)))
        ys = list(map(int, str(y)))
        sums = sum(xs) + sum(ys)
        if sums <= 25 and (x, y) not in points:
            points.append((x, y))
            x += 1
        else:
            x = in_x
            y -= 1
            xs = list(map(int, str(x)))
            ys = list(map(int, str(y)))
            sums = sum(xs) + sum(ys)
            continue
    print()


def backward_and_up(in_x, in_y, sums=0):
    print('backward_and_up')
    x = in_x
    y = in_y
    c = 0
    while sums <= 25:
        c += 1
        if c % 10 == 0:
            point()
        xs = list(map(int, str(x)))
        ys = list(map(int, str(y)))
        sums = sum(xs) + sum(ys)
        if sums <= 25 and (x, y) not in points:
            points.append((x, y))
            x -= 1
        else:
            x = in_x
            y += 1
            xs = list(map(int, str(x)))
            ys = list(map(int, str(y)))
            sums = sum(xs) + sum(ys)
            continue
    print()


def backward_and_down(in_x, in_y, sums=0):
    print('backward_and_down')
    x = in_x
    y = in_y
    c = 0
    while sums <= 25:
        c += 1
        if c % 10 == 0:
            point()
        xs = list(map(int, str(x)))
        ys = list(map(int, str(y)))
        sums = sum(xs) + sum(ys)
        if sums <= 25 and (x, y) not in points:
            print((x, y))
            points.append((x, y))
            x -= 1
        else:
            x = in_x
            y -= 1
            xs = list(map(int, str(x)))
            ys = list(map(int, str(y)))
            sums = sum(xs) + sum(ys)
            continue
    print()


if __name__ == '__main__':
    x, y = 1000, 1000
    points = []

    forward_and_up(x, y)
    forward_and_down(x, y)
    backward_and_up(x, y)
    backward_and_down(x, y)

    # print(sorted(points))
    print(len(points))
