from data import name_data, sname_data, tel_data, adress_data


def input_data():
    name=name_data()
    sname=sname_data()
    tel=tel_data()
    adress=adress_data()
    with open("data.csv", 'a', encoding="utf-8") as one:
        one.write(f"{name} {sname} {tel} {adress}\n")


def print_data():
    print('Вывод данных: \n') 
    with open('data.csv', 'r', encoding='utf-8') as data:
        data=data.readlines()
        s = ''.join(str(x) for x in data)
        print(s)


def change_data():
        with open('data.csv', 'r', encoding='utf-8') as data:
            data=data.readlines()
            result = ''.join(str(x) for x in data)
            print(result)

        old=input('Введите данные, которые необходимо изменить: ')
        a=old in result
        while a!=True:
            print("Введённые данные в справочнике отсутствуют")
            old=input('Введите данные, которые необходимо изменить: ')
            a=old in result
        new=input("Введите новые данные: ")
        result2=result.replace(old,new)
    
        with open("data.csv", 'w', encoding="utf-8") as data:
            data.write(''.join(result2))


def del_data():
        with open('data.csv', 'r', encoding='utf-8') as data:
            data=data.readlines()
            result = ''.join(str(x) for x in data)
            print(result)

        old=input('Введите данные, которые необходимо удалить: ')
        a=old in result
        while a!=True:
            print("Введённые данные в справочнике отсутствуют")
            old=input('Введите данные, которые необходимо удалить: ')
            a=old in result
        result2=result.replace(old,"")
    
        with open("data.csv", 'w', encoding="utf-8") as data:
            data.write(''.join(result2))