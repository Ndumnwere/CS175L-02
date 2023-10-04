#CS501A
#Ezinne Ndumnwere
#Restaurantloopassignment

Repeat="yes"
while Repeat=="yes":
 vegetarian = input("Is anyone in your party vegetarian? ").lower()

 vegan = input("Is anyone in your party vegan? ").lower()   

 gluten_free = input("Is anyone in your party gluten-free? ").lower()

 print("Here are your restaurant choices: ")

 if vegetarian == "no" and vegan == "no" and gluten_free== "no":
    options = ["Joe's Gourmet Burgers","Mama's Fine Italian","Main Street Pizza Company","Corner Cafe","The Chef's Kitchen"]
   
 if vegetarian == "yes" and vegan == "no" and gluten_free == "no":
    options = ["Mama's Fine Italian","Main Street Pizza Company","Corner Café","The Chef's Kitchen"]

 if vegetarian == "no" and vegan == "no" and gluten_free == "yes":
    options = ["Main Street Pizza Company","Corner Café", "The Chef's Kitchen"]
   
 if vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
    options = ["Main Street Pizza Company","Corner Café", "The Chef's Kitchen"]

 if vegetarian == "no" and vegan == "yes" and gluten_free == "no":
    options = ["Corner Café", "The Chef's Kitchen"]
   
 if vegetarian == "no" and vegan == "yes" and gluten_free == "yes":
    options = ["Corner Café", "The Chef's Kitchen"]
   
 if vegetarian == "yes" and vegan == "yes" and gluten_free =="no":
    options = ["Corner Café", "The Chef's Kitchen"]

 if vegetarian == "yes" and vegan == "yes" and gluten_free =="yes":
    options = ["Corner Café", "The Chef's Kitchen"]
    
 for restaurant in options:
    print(restaurant)
 Repeat=input("Enter 'yes' to do another restaurant search, 'no' to end: ")
 if Repeat.lower() != "yes":
   print("This search has ended")

