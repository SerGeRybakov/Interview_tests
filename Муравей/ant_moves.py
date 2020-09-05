"""
На бесконечной координатной сетке находится муравей. Муравей может перемещаться на 1 клетку вверх (x,y+1),
вниз (x,y-1), влево (x-1,y), вправо (x+1,y), по одной клетке за шаг.
Клетки, в которых сумма цифр в координате X плюс сумма цифр в координате Y больше чем 25 недоступны муравью.
Например, клетка с координатами (59, 79) недоступна, т.к. 5+9+7+9=30, что больше 25.
Сколько клеток может посетить муравей, если его начальная позиция (1000,1000), (включая начальную клетку).

Прислать ответ в виде числа клеток, решения на языке Python и скрипта на языке JavaScript, отрисовывающего
на canvas площадь доступную муравью."""


def sum_of_digits(*args: int) -> int:
    sums = 0
    for num in args:
        for digit in str(num):
            sums += int(digit)
    return sums


if __name__ == '__main__':
    points_to_visit = {(1000, 1000)}
    visited_points = {()}

    while points_to_visit:
        current_position = points_to_visit.pop()
        x, y = current_position
        visited_points.add(current_position)
        next_points = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

        available = [pos for pos in next_points
                     if sum_of_digits(*pos) <= 25
                     and pos not in visited_points
                     and pos not in points_to_visit]

        for next_pos in available:
            points_to_visit.add(next_pos)

    print('\n', len(visited_points))
