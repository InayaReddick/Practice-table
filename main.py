from tabulate import tabulate

userInput = (input("Are you thirsty and want a sweet drink?" + " Answer yes or no: "))



table = [
  ["1. Caramel Milk Tea", "$5", "Lychee Iced Tea", "$4.75", "Double Boba", "$0.75"],
  ["2. Oreo Milk Tea", "$5", "Honey Black Tea", "$4.25", "Jellies", "$0.50"],
  ["3. Hokkaido Milk Tea", "$5", "Peach Strawberry Fruit Tea", "$4.75", "Popping Boba", "$0.50"]
]

headers = ["Milk Tea", " $", "Iced Tea", "  $", "Extras", " $"]
      
if userInput == "yes":
  print("Let me interest you in some boba!")
  print(tabulate(table, headers, tablefmt="fancy_grid"))

if userInput == "no":
  print(input("Oh okay. Have a good day!"))


thirsty = (input("Would you like to buy any of these drinks?" + " Answer yes or no: "))

if thirsty == "yes":
  print("List your desired items here. Include any extras!")

iWant = thirsty

milkTea = ["Caramel Milk Tea" or "Oreo Milk Tea" or "Hokkaido Milk Tea"]





    