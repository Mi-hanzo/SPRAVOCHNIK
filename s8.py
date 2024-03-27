from logger import input_data, print_data, change_data, del_data

def interface():
    print("Приветствую! Вы попали в специальный бот от Миханзо! \n 1 - Запись данных \n 2 - Вывод данных \n 3 - Изменение данных \n 4 - Удаление данных")
    command=int(input("Выберите вариант: "))

    while command!=1 and command!=2 and command!=3 and command!=4:
        print("Неправильный ввод")
        command=int(input("Выберите вариант: "))

    if command==1:
     input_data()
    elif command==2:
        print_data()
    elif command==3:
       change_data()
    elif command==4:
       del_data()