import json
import matplotlib.pyplot as plt
import seaborn as sns

json_one = input("Filepath to first account JSON: ")
user_one = input("User one: ")
json_two = input("Filepath to second account JSON, or 'pass': ")
if json_two != 'pass':
    user_two = input("User two: ")

with open(json_one) as data_file:    
    data_one = json.load(data_file)


ratings_count = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
for i in data_one:
    rating = int(i['yourrating'])
    if rating == 1:
        ones += 1
    elif rating == 2:
        twos += 1
    elif rating == 3:
        threes += 1
    elif rating == 4:
        fours += 1
    elif rating == 5:
        fives += 1
    if rating in [1,2,3,4,5]:
        ratings_count += 1

one_percent = float(ones) / ratings_count
two_percent = float(twos) / ratings_count
three_percent = float(threes) / ratings_count
four_percent = float(fours) / ratings_count
five_percent = float(fives) / ratings_count


x = [1, 2, 3, 4, 5]
y = [one_percent, two_percent, three_percent, four_percent, five_percent]


plt.style.use('ggplot')
plt.plot(x, y, label = user_one)
plt.title('Comparative Netflix Ratings')
plt.ylabel('Percentage of Ratings')
plt.xlabel('Rating')


if json_two == 'pass':
    pass
else:
    with open(json_two) as data_file:    
        data_two = json.load(data_file)


    ratings_count = 0
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    for i in data_two:
        rating = int(i['yourrating'])
        if rating == 1:
            ones += 1
        elif rating == 2:
            twos += 1
        elif rating == 3:
            threes += 1
        elif rating == 4:
            fours += 1
        elif rating == 5:
            fives += 1
        if rating in [1,2,3,4,5]:
            ratings_count += 1

    one_percent = float(ones) / ratings_count
    two_percent = float(twos) / ratings_count
    three_percent = float(threes) / ratings_count
    four_percent = float(fours) / ratings_count
    five_percent = float(fives) / ratings_count


    x = [1, 2, 3, 4, 5]
    y = [one_percent, two_percent, three_percent, four_percent, five_percent]


    plt.plot(x, y, c = 'b', label = user_two)

plt.legend(loc = 'upper right')
plt.show()
plt.clf()