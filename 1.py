def main():
    # Ввод списка от пользователя
    user_input = input("Введите элементы списка через пробел: ")


    try:                                                                            # Преобразуем строку в список
        input_list = [float(x) if '.' in x else int(x) for x in user_input.split()]
    except ValueError:
        print("Ошибка: список должен содержать только числа.")
        return


    plusovoe = any(x > 0 for x in input_list)                                    # Проверка: содержит ли список хотя бы одно положительное число
    print("Список содержит хотя бы одно положительное число:" , plusovoe)

    all_numbers = all(isinstance(x, (int, float)) for x in input_list)                         # из чисел или нет только
    print("Список состоит только из чисел:", all_numbers)

    sorted_list = sorted(input_list)                                                   # Сортировка списка
    print("Отсортированный список:", sorted_list)

if __name__ == "__main__":
    main()
