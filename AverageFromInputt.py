#CS501A
#Ndumnwere Ezinne
#AverageFromInput

# numbers.txt 
numbers_str = '''
22
14
-99
'''

def main():

  total = 0
  count = 0

  for line in numbers_str.split('\n'):
    
    if line.strip() == '':
      continue
    
    number = float(line)   
    total += number
    count += 1

    print(f"I read in {count} number(s) Current number is: {number:.2f} Total is: {total:.2f}")

  average = total / count
  print(f"\nAverage: {average:.1f}")

if __name__ == '__main__':
  main()
