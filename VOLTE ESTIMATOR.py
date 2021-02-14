devices = {'Geaser':240,'AC':360,'TV':15,'Washing Machine':30,'Refrigerator':130}
unit_price = eval(input("Price of a unit in your area: "))
bill = []
for device,unit in devices.items():
    print(f"Do you have {device} y or n??")
    choice = input()
    if choice == 'y':
        a=int(input("Enter how many device do you have: "))
        bill.append(unit)

hidden_charges = 69.6
total_bill =int(sum(bill)*unit_price + hidden_charges)
print(f"₹{total_bill} for a month")
