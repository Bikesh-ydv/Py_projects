#Banking program

def show_balance():
    print(f"Balance Amount :Rs {balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit:"));
    if amount <= 0:
       print("Amount should not be less than or equal to 0");
    return amount;

def withdraw():
    amount = float(input("Enter amount to be withdrawn :"));
    if amount > balance :
        print("Insufficient balance");
        return 0;
    elif amount <= 0:
        print("Amount should not be less than or equal to 0");
        return amount;
    else:
        return amount;


balance = 0;
is_running = True;

while is_running:
    print("1.Show Balance");
    print("2.Deposit");
    print("3.Withdraw");
    print("4.Exit");
    choice = int(input("Enter choice (1-4): "));
    if choice==1:
        show_balance();
    elif choice==2:
        balance += deposit();
    elif choice ==3:
        balance -= withdraw();
    elif choice==4:
        is_running = False;
    else :
        print("Invalid choice !");
print("Thank you . Have a nice day !");