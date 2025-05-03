#shopping cart program
items = [];
prices = [];
total = 0;
while True :
    item =input("Enter the item you want to buy(q for quit) :");
    if item.lower() == 'q':
        break;
    else :
           price = float(input(f"Enter the price of {item} : Rs "));
           items.append(item);
           prices.append(price);

print("------shopping cart------");
for item in items :
     print(item,end=" ");

print();

for price in prices :
     print(price,end=" ");
     total += price;

print();
print(f"Total amount : Rs {total}");