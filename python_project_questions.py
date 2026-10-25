#PROJECT 1: ATM Simulator
correct_pin=1234
balance=10000
attempt=1
history=[]
while True:
    pin=int(input('Enter pin: '))
    if pin!=correct_pin:
        if attempt<3:
            print('Invalid pin')
            print('Attempt left: ',3-attempt)
            attempt+=1
        else:
            print('Card Blocked')
            break
    else:
        while True:
            print('''MENU:
                1. Balance
                2. Deposit
                3. Withdraw
                4. Exit''')
            choice=int(input('enter your choice: '))
            if choice==1:
                print('Balance: ',balance)
            elif choice==2:
                deposit=int(input('enter deposit amount: '))
                if deposit>0:
                    balance+=deposit
                    print('New Balance: ',balance)
                    history.append(f'Deposit {deposit}')
                else:
                    print('Invalid amount')
            elif choice==3:
                withdraw=int(input('Enter withdraw amount: '))
                if withdraw>0:
                    if withdraw<=balance:
                        balance-=withdraw
                        print('New Balance: ',balance)
                        history.append(f'Withdraw {withdraw}')
                    else:
                        print('Insufficient balance')
                else:
                    print('Invalid amount')
            elif choice==4:
                for transaction in history:
                    print(transaction)
                print('Thank You')
                break
            else:
                print('Choice not available')
        break


#PROJECT 2 : Student Marks Manager
students = {'Aman':[85,90,78], 'Riya':[92,88,95],'Zoya':[70,65,80]}
while True:
    print('''MENU:
    1. Add student
    2. View all
    3. Show topper
    4. Exit''')
    choice=int(input('enter the choice: '))
    if choice==1:
        while True:
            name=input('enter name of the student: ')
            m1=int(input('enter marks1: '))
            m2=int(input('enter marks2: '))
            m3=int(input('enter marks3: '))
            if name in students:
                print('Student already exists.')
                continue
            elif m1<0 or m1>100 or m2<0 or m2>100 or m3<0 or m3>100:
                print('Invalid mark, try again.')
            else:
                students[name]=[m1,m2,m3]
                print('Successfully added ',name)
                break
    elif choice==2:
        for k,m in students.items():
            av=sum(m)/len(m)
            if av>=85:
                print(f'{k} {av:.2f} A')
            elif av>=70:
                print(f'{k} {av:.2f} B')
            elif av>=50:
                print(f'{k} {av:.2f} C')
            else:
                print(f'{k} {av:.2f} F')
    elif choice==3:
        highest_avg=0
        high=''
        for k,m in students.items():
            av=sum(m)/len(m)
            if av>highest_avg:
                highest_avg=av
                high=k
        print('Topper: ',high)
    elif choice==4:
        print('Goodbye!')
        break
    else:
        print('Invalid choice, Please enter a valid choice')