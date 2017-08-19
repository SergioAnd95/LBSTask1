def count_str(lst1, lst2):
    return [(i, lst1.count(i)) for i in lst2]


if __name__ == '__main__':
    num1 = int(input('Введите количество элементов контрольного списка\n'))
    lst1 = [input('Введите строку\n') for i in range(num1)]

    num2 = int(input('Введите количество элементов списка который вы хотите проверить\n'))
    lst2 = [input('Введите строку\n') for i in range(num2)]

    for s, count in count_str(lst1, lst2):
        print(count)