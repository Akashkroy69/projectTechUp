lowerNum = int(input("Enter lower number: "))
upperNum = int(input("Enter upper number: "))

for num in range(lowerNum,upperNum):
    print(f"Multiplication Table of {num}: ")
    for i in range(0,11):
        print(f"{num} * {i} = {num*i}")
# ----------------------------------------
num = int(input("Enter a number: "))

for i in range(num):
    for j in range(num):
        print("**|** ",end="  ")
    print("\n")