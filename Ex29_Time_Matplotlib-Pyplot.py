# Create a program to help the user type faster.
# Give him a word and ask him to write to five times. Check how many seconds it took him to type the word each round.
# In the end,Tell the user how many mistakes were made and show a chart with the typing speed evolution during the five rounds.

import time as t
import matplotlib.pyplot as plt

cont = 0
mistakes_count = 0
type_speed = []

while cont < 5:
    initial_time = t.time()
    tried_word = input("Write the word 'Computer': ")
    final_time = t.time()

    time_took = round((final_time - initial_time), 2)
    print("it took " + str(time_took) + " to write the word")

    type_speed.append(time_took)

    if(tried_word.lower() != "computer"):
        mistakes_count += 1

    cont += 1

print("Total number of mistakes: " + str(mistakes_count))
print(type_speed)

x = list(range(1, 6))
x_legend = ["Try 1", "Try 2", "Try 3", "Try 4", "Try 5"]
plt.xticks(x, x_legend)
plt.ylabel("Time in seconds to typewrite the word")
plt.title("Evolution of typewriting 'Computer' word")

plt.plot(x, type_speed)
plt.show()
