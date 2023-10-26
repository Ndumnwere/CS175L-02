#CS501A
#Ndumnwere Ezinne
#CalculateAverage2

import random

def my_random(low, high):
    # Generate a random integer between 'low' and 'high'.
    return random.randint(low, high)

def calc_average():
    total = 0
    scores = []

    # Generate random scores, calculate the total, and display them.
    for i in range(5):
        score = my_random(1, 100)
        scores.append(score)
        total += score
        print(f"score {i + 1}:\t{score:.1f}\t{determine_grade(score)}")

    # Calculate the average and display it with its letter grade.
    average = total / 5
    print(f"Average score:\t{average:.1f}\t{determine_grade(average)}")

def determine_grade(score):
    # Determine the letter grade based on the score.
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def repeat():
    while True:
        calc_average()
        user_input = input("Enter 'yes' if you would like to do another calculation: ")
        if user_input.lower() != 'yes':
            break

if __name__ == "__main__":
    repeat()
