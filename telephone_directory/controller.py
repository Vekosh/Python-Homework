import reading_data
import print_all_data
import UI
import add_data
import logger
import find_data


def button_click():
    UI.print_data(
        "Вы можете выполнить следующие действия со справочником номеров: "
    )
    answer = UI.input_check_choice(
        "1. Вывод всего справочника.\n2. Добавление нового номера\n3. Поиск номера\n"
        + "4. Выход из программы\nВведите цифру: "
    )
    if answer == 1:
        list_data = reading_data.get_info("uses.csv")  # читаем
        print_all_data.print_all(list_data)  # печатаем все
        UI.print_data(f"\nСправочник номеров состоит из {len(list_data) - 1} записей")
        button_click()
    elif answer == 2:
        user_data = UI.input_name_directory()
        add_data.append_data("uses.csv", user_data)
        logger.result_loger(user_data)
        UI.print_data("\nДанные успешно добавлены в справочник номеров.")
        button_click()
    elif answer == 3:
        find_data.finder_data()
        button_click()
    elif answer == 4:
        exit()
    else:
        print("Неправильный ввод!")
        button_click()