"""Restaurant rating lister."""


# put your code here
import random
import os
import sys

# Empty dictionary to fill in later with all the ratings.
rating_dict = {}

# Open the file, creates a local copy, and closes the file.
scores = open('scores.txt')
score_lines = scores.readlines()

for line in score_lines:
    line = line.split(":")
    rating_dict[line[0]] = line[1].strip("\n")

scores.close()


# Greets user upon opening program.
def greeting():
    print("Welcome to the Restaurant Rater 8000!!!")


# Gives selections for program.
def menu():
    print("Please select from the following options, and type the corresponding number to choose.")
    print("1 - See all the restaurant ratings. \n2 - Add a new restaurant rating. \n3 - Update a restaurants rating. \n4 - See all directory files\n0 - Quit")
    choice = input('Type selection here: ')

    if choice == "1":
        read_ratings(True)
    elif choice == "2":
        ask_to_add(False)
    elif choice == "3":
        update_res(True)
    elif choice == "4":
        dir_list = os.listdir()
        print("Files and directories")
        for i in dir_list:
            print(i)
    elif choice == "0":
        print("Thank you! Have a great day!")
        sys.exit()


# Function reads out all of the ratings to the screen.
def read_ratings(is_alphbetical):
    
    if is_alphbetical:
        print("Here are the restaurants and their ratings, in alphabetical order.")

        for k, v in sorted(rating_dict.items()):
            print(f"{k} is rated at {v}.")
    
    menu()

# Allows the user to add a new restaurant to the ratings list.
def ask_to_add(is_repeat):

    def add_res():
        r_name = input("Please type the restaurant name - ")

        if r_name not in rating_dict:
            r_rating = input("Please type the restaurant rating - ")
            rating_dict[r_name] = r_rating
            print("Restaurant updated.")
            ask_to_add(True)
        else:
            print("Sorry that restaurant already exists.")
            ask_to_add(True)


        rating_dict[r_name] = r_rating

        ask_to_add(True)

    if is_repeat == False:
        add_res()
    else:    
        print("Would you like to add a new restaurant to rate?")
        ans = input("Yes/No - ")
        
        if ans == "Yes":
            add_res()
        elif ans == "No":
            print("\nHeading back to menu.")
            menu()
        else:
            print("Please type in 'Yes' or 'No'.\n")
            ask_to_add(True)


def update_res(give_intro):

    if give_intro == True:
        print("Please press 1 to update a random restaurant. Press 2 to choose the restaurant by name. Press 3 to see all the ratings. Press 4 to head back to the menu.")
    elif give_intro == False:
        print("Would you like to update another restaurant?")
        ans = input("Yes/No - ")
        if ans == "Yes":
            update_res(True)
        elif ans == "No":
            print("Heading back to the menu.")
            menu()


    choice = input("Type here - ")


    if choice == "1":
        restaurant = random.choice(list(rating_dict))
        print("What rating would you give " + restaurant)
        new_rating = input("Type rating here - ")
        rating_dict[restaurant] = new_rating
        update_res(False)
    elif choice == "2":
        print("What is the name of the restaurant you would like to update?")
        restaurant = input("Please type here - ")
        if restaurant in rating_dict:
            rating_dict[restaurant] = input("Please type new rating here - ")
            print("Restaurant updated.")
            update_res(False)
        else:
            print("Sorry that doesn't exist.")
            update_res(False)
    elif choice == "3":
        read_ratings()
        update_res(False)
    elif choice == "4":
        menu()
    else:
        print("Please select from 1 and 2")


# Function calls // Runs the program.
greeting()
menu()