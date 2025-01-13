# coin , 100 flips, find prob of head and coin based on those 100 flips
import random
# flips = []
# for i in range(100):
#     flips.append(random.choice(['heads','tails']))

# # print(flips)
# headCount = flips.count('heads')
# tailsCount = flips.count('tails')

# probabilityForHead = headCount/100
# probabilityForTail = tailsCount/100
# print(probabilityForHead,probabilityForTail)

# roll a dice for 1000 times then find prob of 1 to 6


flips = []
for i in range(1000):
    flips.append(random.randint(1,6))

Countof1 = flips.count(1)/1000
Countof2 = flips.count(2)/1000
Countof3 = flips.count(3)/1000
Countof4 = flips.count(4)/1000
Countof5 = flips.count(5)/1000
Countof6 = flips.count(6)/1000

print(Countof1, Countof2, Countof3, Countof4, Countof5, Countof6)

#Simulate rolling two dice 1000 times and calculate the probability of the sum being 7