def gender_address(func):
    gender_dict = {'М': 'Г-н', 'Ж': 'Г-жа'}

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return ['%s %s %s' % (gender_dict[i[2]], i[0], i[1]) for i in res]
    return wrapper


@gender_address
def sort_by_age(lst):
    return sorted([i.split(' ') for i in lst[:-1]], key=lambda l: int(l[3]))


if __name__ == '__main__':
    num = int(input('Введите количество персонажей\n'))
    txt = 'Введите персонажа согласно такому правилу: Имя Фамилия Пол( М или Ж ) Возраст\n'
    lst = [input(txt) for i in range(4)]
    print('\n')
    for i in sort_by_age(lst):
        print(i)
