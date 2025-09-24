# Concession stand program
# all are estimated prices in an imagiunaey cinema hall!

menu = {"pizza":350,
        "nachos":220,
        "popcorn":120,
        "fries":100,
        "chips": 50,
        "soda":40,
        "lemonade":80}
cart = []
total = 0

print("----------Menu----------------")
for key, value in menu.items():
    print(f"{key:10}: BDT {value:}")
print("------------------------------")

while True:
    food = input("Select an item (q to quit and calcualte): ")
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------your order-----------")        
for food in cart:
    price = menu.get(food)
    total +=price
    print(f"{food:10} : BDT{price}")
print("------------------------------")    
print(f"Total is: BDT {total}")
