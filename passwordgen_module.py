

def passwordgen(password):
    import random
    password = []
    password_length = random.choice(range(8, 30))
    for i in range(password_length):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        signs = "!@#$%^&*()_+=-[]{}|\:;<>,.?/"
        random_number = str(random.choice(range(10)))
        random_letter = random.choice(list(letters))
        random_sign = random.choice(list(signs))
        list_of_choices = [random_number, random_letter, random_sign]
        random_character = random.choice(list_of_choices)
        password.append(random_character)
    return password


