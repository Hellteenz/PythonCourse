# TODO Напишите функцию find_common_participants

def find_common_participants(first_group_str, second_group_str, split_symb=","):
    first_group_list = set(first_group_str.split(split_symb))
    second_group_list = set(second_group_str.split(split_symb))
    return list(first_group_list.intersection(second_group_list))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))
