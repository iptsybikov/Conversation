import random

def oldmax(users):
    if len(users) == 0:
        return None
    else:
        max_age = users[0]['age']
        oldest_user = users[0]

        for user in users[1:]:
            if user['age'] > max_age:
                max_age = user['age']
                oldest_user = user

        return oldest_user

def generate_name():
    name_len = random.randint(1, 20)
    name = []
    for i in range(name_len):
        name.append(random.choice('1234567890йцукенгшщзхъфывапролджэячсмитьбю'))
    return ''.join(name)
