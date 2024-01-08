import pyinputplus as pyip
import time
# Sandwich Maker
breads = {"wheat": 3, "white": 2,"sourdough": 4}
proteins = {"chicken": 4, "turkey": 6, "ham": 5, "tofu": 3}
cheeses = {"cheddar": 4, "swiss": 5, "mozzarela": 3}
toppings = {"mayonaise": 2,"mustard": 3,"tomato": 2,"lettuce": 1}

price = 0

bread = pyip.inputMenu(list(breads.keys()), numbered=True)
price += breads[bread]

protein = pyip.inputMenu(list(proteins.keys()), numbered=True)
price += proteins[protein]

if pyip.inputYesNo("Do you want cheese? ") == "yes":
    cheese = pyip.inputMenu(list(cheeses.keys()), numbered=True)
    price += cheeses[cheese]
for topping in toppings:
    if pyip.inputYesNo(f"Do you want {topping}? ") == "yes":
        price += toppings[topping]

count = pyip.inputNum("How many sandwiches do you want? ", min=1)

print("...")
time.sleep(1)
print(f"Your order is ready. Pay ${count * price}")