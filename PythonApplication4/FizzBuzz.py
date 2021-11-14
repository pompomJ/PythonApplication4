
for i in range(30):

    if (i ==0) or ((i % 3 == 0) and (i % 5 == 0)):
        #0は当然3でも5でも割り切れることに注意
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
