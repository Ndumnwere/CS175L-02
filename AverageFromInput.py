#CS501A
#Ndumnwere Ezinne
#AverageFromInput


# Program to calculate average of numbers in a file

total = 0 
count = 0

# Open file for reading
with open('numbers.txt') as f:
  
  # Loop through lines
  for line in f:
    
    # Convert each line to a float
    number = float(line)
    
    # Add number to running total
    total += number
    
    # Increment count
    count += 1

    # Print output for current number and total 
    print(f"I read in {count} number(s) Current number is: {number:.2f} Total is: {total:.2f}")

# After loop, calculate average as total / count
average = total / count

# Print result rounded to 1 decimal place  
print(f"\nAverage: {average:.1f}")
