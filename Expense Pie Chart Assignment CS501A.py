#CS501A
#Ndumnwere Ezinne
#Expense Pie Chart 

import matplotlib.pyplot as plt

def main():
# Declare expenses dictionary
    expenses = {}
    
    try:
# Open file for reading
        infile = open("expenses.txt", "r")
        
# Read lines from file 
        for line in infile:
            try:
# Split line into category and amount
                category, amount = line.strip().split('\t')
                
# Convert amount to float    
                amount = float(amount)
                
# Put into expenses dictionary
                expenses[category] = amount
            except:
# Print error message 
                print("Could not parse line:", line)
                
# Close file
        infile.close()
            
    except IOError:
        print("Could not open file expenses.txt")
        
# Create pie chart    
    plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
    
# Set chart title
    plt.title("Expense Pie Chart")
    
    # Display pie chart
    plt.show()
    
if __name__ == "__main__":
    main()
