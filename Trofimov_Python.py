number = int(input()) #10
name = input() #John
numbers = list(map(int, input().split())) #3 4 6 8 9 12

if number > 7:
    print("Hello") #Hello

if name == "John":
    print("Hello, John") #Hello, John
else:
    print("There is no such name")

for num in numbers:
    if num % 3 == 0:
        print(num) #3, 6, 9, 12