print("Welcome to our TastyDine")
menu={
'pasta':60,
'noddles':40,
'fried chickhen':150,
'coffee':100

}
print("'pasta':60tk\nnoddles:40tk\nfried chickhen:150tk\ncoffee:100tk")
orderfood=input("order your food: ")
itempayment=0
if orderfood in menu:
    print(f"your food {orderfood} added")
    itempayment+=menu[orderfood]
else:
    print(f"your order {orderfood}is not available.Please order something else")
    

item=input("do you want to order anything else?")
item2=input("what do you want to order?")
if item =="yes":
    if item2 in menu:
     itempayment+=menu[item2]
    print(f"your food{item2}added")
    print(f"your total payment is {itempayment}")
else:
    print(f"your order {item2}is not available.Please order something else")
     

print("Thank you for ordering food")