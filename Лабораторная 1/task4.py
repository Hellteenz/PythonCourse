users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users.sort()

dictionary = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
dictionary["Общее количество"] = len(users)
dictionary["Уникальные посещения"] = len(list(set(users)))
print(dictionary)
