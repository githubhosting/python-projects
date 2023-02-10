ask = int(input('Want to be in loop? type 1 else 2 to break: '))
if ask == 1:
    a = int(input("Enter Start Point: "))
    b = int(input("Enter end Point: "))
    if b > a:
        low = a
        up = b
    else:
        low = b
        up = a
    print("The Prime Numbers in the range of", low, "to", up, "are: ")
    # loop runs from lower term to upper term
    for number in range(low, up + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number, end=" ")
elif ask == 2:
    print("ThankYou")
