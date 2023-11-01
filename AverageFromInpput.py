#CS501A
#Ndumnwere Ezinne
#AverageFromInput


# Define main() function
def main():

  # Initialize variables
  total = 0
  count = 0

  # Open file and assign to numbers_file
  file_path = r"C:\Users\chidu\Downloads\numbers.txt"
  numbers_file = open(file_path, 'r')

  # Loop through lines
  for line in numbers_file:

    if line.strip() == '':
      continue
    
    number = float(line)

    total += number
    count += 1

    print(f"I have read in {count} number(s). Current number is: {number:.2f}. Total is: {total:.2f}")

  # Calculate and print average
  if count > 0:
      average = total / count
      print(f"\nAverage: {average:.1f}")
  else:
      print("\nNo numbers found in the file.")

  # Close file
  numbers_file.close()

if __name__ == '__main__':
    main()
