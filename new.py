while True:
    user=input('Enter your name:')
    print('hello '+user)
    age2=int(input("Enter your age:"))
    if age2<20:
        print('hi,young '+user)
        break
    elif age2>20:
        print('Hello,adult '+user)
        break
    else:
    	print('Unknown input')