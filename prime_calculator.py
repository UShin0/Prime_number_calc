# Python Prime Number Calculator

#Author UShin0 11/18/2022

run = True
while run:
    length = 0
    prime = "|"

    print("To which maximum do you want the primes?")
    try:
        length = int(input()) + 1
    except:
        print("That wasn´t a number")
    for i in range(0, length + 1):
        for x in range(2, length):
            if i % x != 0 and i - 1 == x:
                prime += str(i) + "|"
            elif i % x != 0 and x == length - 1:
                prime += str(i) + "|"
            elif i % x != 0:
                continue
            else:
                break
    print(prime)