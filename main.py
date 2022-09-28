from action_module import Action
from game import Game
from playground import Playground
from team import Team

from time import sleep

A = Team()
B = Team(1)

jeonju = Playground()
first_league = Game()

print("--------------------")
print("경기 시작 합니다.")
print("--------------------")

while first_league.get_inning() < 10:
    sleep(5)
    print("{}이닝".format(first_league.get_inning()))
    print("A팀의 {}//B팀의 {}".format(A.get_ond(), B.get_ond()))
    
    result = first_league.result()
    action = Action(first_league, jeonju, A if not A.ond else B)
    change = action.get_action(result)
    if change:
        jeonju.base = [0,0,0]
        A.set_ond()
        B.set_ond()
        first_league.inning += 1
        print("A\t{}".format(A.score))
        print("B\t{}".format(B.score))
    print(jeonju.base)
    print("--------------------")
    
print("[결과]")
print("A팀  {}점\nB팀  {}점".format(sum(A.score), sum(B.score)))
if sum(A.score) == sum(B.score): print("무승부")
else: print("{}팀 승".format('A' if sum(A.score) > sum(B.score) else 'B'))