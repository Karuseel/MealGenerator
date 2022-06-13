import random

first_course = ['asado', 'Wiener Schnitzel', 'multi-free', 'feijoada', 'shanghai dumplings', 'arepa', 'tamale', 'pagian cheese', 'olebrod', 'Moloheya']
second_course = ['Harira', 'Menudo', 'Banga', 'Pho bo', 'Borsch', 'Bouillabaisse', 'Caldo Verde', 'Chorba freak', 'Chupe de Camarones', 'Gazpacho']

def random_first_course():
    print(random.choice(first_course))
    print('PRESS 1 TO CHANGE DISH')
    change_selection = input()
    if change_selection == '1':
        random_first_course()

def random_second_course():
    print(random.choice(second_course))
    print('PRESS 1 TO CHANGE DISH')
    change_selection = input()
    if change_selection == '1':
        random_second_course()

def main():
    print('FIRST COURSE - 1 | SECOND COURSE - 2')
    user_choice = input()

    if user_choice == '1':
        random_first_course()
    elif user_choice == '2':
        random_second_course()
    else:
        main()

if __name__ == '__main__':
    main()
