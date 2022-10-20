def open_file(file):
    with open(f"{file}", "r") as text_in:
        str_in = text_in.readline()
    return str_in


def finder_data():
    find_str = UI.find_data()
    lst = open_file("uses.csv").split(",")
    result = 0
    for i in range(0, len(lst)):
        if find_str in lst[i]:
            print(lst[i])
            result = 1
    if result == 0:
        print(f'Yjvthf c данными "{find_str}" в базе не обнаружено!')