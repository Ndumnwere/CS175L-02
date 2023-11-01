#CS501A
#Ndumnwere Ezinne
#AverageFromInput

# numbers.txt
numbers_str = '''
22  
14
-99
'''

# Define main() function
def main():
  
  # Initialize variables total and count
  total = 0
  count = 0

  # Read file data from string
  for line in numbers_str.split('\n'):

    # Skip blank lines
    if line.strip() == '':
      continue
    
    # Convert line to float
    number = float(line)

    # Add number to total
    total += number

    # Increment count
    count += 1

    # Print current number and total
    print(f"I read in {count} number(s) Current number is: {number:.2f} Total is: {total:.2f}")
  
  # After loop, calculate average
  average = total / count
  
  # Print average 
  print(f"\nAverage: {average:.1f}")

# Call main() if run directly
if __name__ == '__main__':
  main()
