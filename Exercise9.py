input_num = int(input("Please enter a number: "))

num = input_num
while num > 0:
    i = 0 
    while i < num:
        print(i + 1, end=" ")
        i += 1
    print() 
    num -= 1