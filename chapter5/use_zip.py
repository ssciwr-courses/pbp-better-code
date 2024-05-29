days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
lunch = ["Pizza", "Salad", "Pasta", "Sushi", "Sandwich"]

# change the below to use zip

for index, day in enumerate(days):
    print("On {} we offer {} for lunch.".format(day, lunch[index]))

# also works for more than two lists

# if you use lists of different lengths, zip will stop after shortest list is exhausted
# for more details check the itertools library