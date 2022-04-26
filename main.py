from tabulate import tabulate

userInput = (input("Are you thirsty and want a sweet drink?" + " Answer yes or no: "))



table = [
  ["1. Caramel Milk Tea", "$5", "4. Lychee Iced Tea", "$4.75", "7. Double Boba", "$0.75"],
  ["2. Oreo Milk Tea", "$5", "5. Honey Black Tea", "$4.25", "8. Jellies", "$0.50"],
  ["3. Hokkaido Milk Tea", "$5", "6. Peach Strawberry Fruit Tea", "$4.75", "9. Popping Boba", "$0.50"]
]

headers = ["Milk Tea", " $", "Iced Tea", "  $", "Extras", " $"]
      
if userInput == "yes":
  print("Let me interest you in some boba!")
  print(tabulate(table, headers, tablefmt="fancy_grid"))

elif userInput == "no":
  print(input("Oh okay. Have a good day!"))


thirsty = (input("Would you like to buy any of these drinks?" + " Answer yes or no: "))

while thirsty == "yes":
  iWant = (input(" Write the number of the drink/drinks you want here. Do not include extras here :"))

list []

while thirsty == "no":
  print("Okay 😭 enjoy your day")
  break 