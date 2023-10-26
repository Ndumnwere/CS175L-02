#CS501A
#Ndumnwere Ezinne
#calculateAverage

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

def calc_average():
    total = 0
    scores = []

    # Input scores and calculate the total.
    for i in range(5):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)
        total += score

    # Display the header for the score table.
    print("\nScore\t\tNumeric Grade\tLetter Grade")
    print("-" * 48)

    # Calculate and display letter grades for individual scores.
    for i, score in enumerate(scores):
        grade = determine_grade(score)
        print(f"score {i + 1}:\t{score:.1f}\t\t{grade}")

    # Calculate and display the average with its letter grade.
    average = total / 5
    avg_grade = determine_grade(average)
    print(f"\nAverage score:\t{average:.1f}\t\t{avg_grade}\n")

def repeat():
    while True:
        calc_average()
        user_input = input("Enter 'yes' if you would like to do another calculation: ").lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    repeat()
