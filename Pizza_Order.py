print("Thank you for choosing Python Pizza Deliveries!")
print("Prices of pizzas are as follows:")
print("Small 'S' pizza = $15")
print("Medium 'M' pizza = $20")
print("Large 'L' pizza = $25")
print("Extra pepperoni for small pizza = $2")
print("Extra pepperoni for medium and large pizza = $3")
print("Extra cheese for any size pizza = $1")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
if add_pepperoni == "Y":
# add extra pay
    if size == "S":
      bill += 2
    else:
      bill += 3
if extra_cheese == "Y":
    bill += 1
else:
    bill
print(f"Your final bill is: ${bill}")