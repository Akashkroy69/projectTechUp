# functions
def greet():
    print("Hello, World!")
greet()

# parameterized functions
def greet1(name):
    print(f"Hello {name}")
greet1("John")

def greet2(name,message):
    print(f"Hello {name}, {message}")

greet2("John", "Good morning!")


def makingHotMilkRobot(time):
    print("Pour milk into glass")
    print("Open the door to the microwave")
    print("Put glass into microwave")
    print("Close door to the microwave")
    print("Turn microwave on")
    print(f"Set on warm for {time} seconds")
    print("Turn off the microwave")
    print(f"Open the door  to microwave")
    print("Put gloves on")
    print("Take the glass out of the microwave carefully")
    print("Put it on the counter carefully")
    print("Drink the hot glass of milk carefully without spilling clsit hot on your body")
    print("----------work done----------")

for i in range (10):
    time = int(input("Set time for how long to warm milk: "))
    makingHotMilkRobot(time)
    


