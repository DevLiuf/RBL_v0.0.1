import random
import DiceTumble
import os
import time
#두 개의 주사위를 던진다.

#이닝
import Event
inning = int(1)


print("--------------------")
print("경기 시작 합니다.")
print("--------------------")
while Event.inning < 10:
    time.sleep(5)
    Event.Inning()
    Event.Team()

    Event.Result()
    print("--------------------")

print("[결과]")
print(f"A팀  {Event.aScore}점")
print(f"B팀  {Event.bScore}점")
if Event.aScore > Event.bScore:
    print("A팀 승")
elif Event.aScore < Event.bScore:
    print("B팀 승")
else:
    print("무승부")

# 어떤수 나오니
# print("D1은",DiceTumble.Dice1())
# print("D2는",DiceTumble.Dice2())
# print("합은",DiceTumble.DicePlus())


# D1ranChoice = random.choice(D1)
# D2ranChoice = random.choice(D2)

###################################################################
# while inning <= 200:
#     D1ranChoice = random.choice(D1)
#     D2ranChoice = random.choice(D2)
#     if current_price == 0:
#         break
#
#     if ranChoice == 0:
#         current_price = current_price - 1
#         #print('-1p')
#         print(current_price)
#     elif ranChoice == 1:
#         current_price = current_price + 0
#         #print('0p')
#         print(current_price)
#     elif ranChoice == 2:
#         current_price = current_price + 1
#         #print('+1p')
#         print(current_price)
