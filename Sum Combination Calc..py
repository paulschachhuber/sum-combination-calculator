import random

bj_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
        9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11,
        11]
custom_list = []
pairs = []

count = 0
nomatch_count = 0
double_count = 0
rep_count = 0

def gen_loop():
    global count
    global nomatch_count
    global double_count
    global rep_count
    global custom_list
    global pairs

    while 1 == 1:
        random_num1 = random.randint(0, index_size - 1)
        random_num2 = random.randint(0, index_size - 1)

        if random_num1 == random_num2:
            rep_count = rep_count + 1
        else:
            ran_element1 = custom_list[random_num1]
            ran_element2 = custom_list[random_num2]
            ran_pair1 = random_num1, random_num2
            ran_pair2 = random_num2, random_num1
            found = 0

            for a in pairs:
                if a == ran_pair1 or a == ran_pair2:
                    found = 1

            if found == 0:
                pairs.append(ran_pair1)
                pairs.append(ran_pair2)
                sum_pair = ran_element1 + ran_element2

                if sum_pair == int(number):
                    count = count + 1
                    print("Count:", count)
                else:
                    nomatch_count = nomatch_count + 1
            else:
                double_count = double_count + 1

print("""\


   _____                    _____                _     _             _   _                _____      _
  / ____|                  / ____|              | |   (_)           | | (_)              / ____|    | |
 | (___  _   _ _ __ ___   | |     ___  _ __ ___ | |__  _ _ __   __ _| |_ _  ___  _ __   | |     __ _| | ___
  \___ \| | | | '_ ` _ \  | |    / _ \| '_ ` _ \| '_ \| | '_ \ / _` | __| |/ _ \| '_ \  | |    / _` | |/ __|
  ____) | |_| | | | | | | | |___| (_) | | | | | | |_) | | | | | (_| | |_| | (_) | | | | | |___| (_| | | (__ _
 |_____/ \__,_|_| |_| |_|  \_____\___/|_| |_| |_|_.__/|_|_| |_|\__,_|\__|_|\___/|_| |_|  \_____\__,_|_|\___(_)

""")

user_input = int(input("input [0] to create a custom list or [1] to use a 52 elements black jack deck:"))


if user_input == 1:
    deck_size = int(input("enter deck size (1-9):"))
    if deck_size > 1:
        print("generating deck...")
        deck_count = 1
        deck_index = 0
        while deck_count < deck_size:
            while deck_index < 52:
                bj_deck.append(bj_deck[deck_index])
                deck_index = deck_index + 1
            deck_count = deck_count + 1
            deck_index = 0
        custom_list = bj_deck
        index_size = len(bj_deck)
        print("deck size:", index_size)
        print(bj_deck)
    else:
        print("continouing with 1 deck...")
        index_size = 52
        custom_list = bj_deck

    number = input("enter sum (4-22):")
    gen_loop()


elif user_input == 0:
    n = int(input("enter number of elements in your list:"))
    n_count = 0
    print("input elements:")
    while n_count < n:
        custom_element = int(input())
        custom_list.append(custom_element)
        n_count = n_count + 1
        index_size = len(custom_list)
    print("deck length:", index_size)
    print(custom_list)
    number = int(input("enter sum:"))
    gen_loop()


else:
    print("invalid input")
