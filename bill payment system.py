import random

name_string = input("Give me everybody's names, seperated by commas.\n")
names = name_string.split(", ")

num_items = len(names)  #to get the length i.e., number of names entered

random_choice = random.randint(0, num_items - 1)  #minus 1 is done as we are started counting from 0
person_who_will_pay = names[random_choice]
print(str(person_who_will_pay) + " is going to buy the meal today.")
