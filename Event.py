import DiceTumble

# 삼진, 그라운드 아웃, 플라이 아웃
# 볼넷, 안타, 2루타, 3루타, 홈런

# 아웃카운트
global OutCount
OutCount = 0

# 이닝
global inning
inning = 1

# 베이스
global base
base = [0, 0, 0, 0]
# 공격 수비
global ond
ond = 0

#팀 점수
global aScore
aScore = [0]
global bScore
bScore = [0]

offense = '공격'
defence = '수비'

# ========================================

# 공수교대
def OND():
    global OutCount
    global base
    global ond
    if OutCount == 3:
        print("======공수교대======")
        OutCount = 0
        base = [0, 0, 0, 0]



def Inning():
    print(f"{inning} 이닝")


# ===============================================

# 공격 아웃카운트
def OutCountTotal():
    global inning
    global ond
    if OutCount == 3:
        if ond == 1:
            ond = 0
            inning += 1
        elif ond == 0:
            ond = 1
    return OutCount


# 수비 아웃카운트
def OutCountPlus():
    global OutCount
    global inning
    global ond
    OutCount += 1
    if OutCount == 3:
        if ond == 1:
            ond = 0
            inning += 1
        elif ond == 0:
            ond = 1
    return OutCount


# ======================================================

def OffenseBase(x):
    global base
    global aScore
    global bScore
    global ond
    if x == 'H':
        for i in range(4):
            base[3] = base[3] + base[2]
            base[2] = base[1]
            base[1] = base[0]
            base[0] = 0
        base[3] = base[3] + 1

        if ond == 0:
            aScore[0] = aScore[0] + base[3]
        else:
            bScore[0] = bScore[0] + base[3]

    #볼
    elif x == 0:
        if base[0] == 1:
            if base[1] == 1:
                if base[2] == 1:
                    base[3] = base[3] + base[2]
                    base[2] = base[1]
                    base[1] = base[0]
                    base[0] = 1
                elif base[2] == 0:
                    base[2] = base[1]
            elif base[1] == 0:
                base[2] = base[2]
                base[1] = base[0]
                base[0] = 1
        elif base[0] == 0:
            base[0] = 1

        if ond == 0:
            aScore[0] = aScore[0] + base[3]
        else:
            bScore[0] = bScore[0] + base[3]



    else:
        for i in range(x):
            base[3] = base[3] + base[2]
            base[2] = base[1]
            base[1] = base[0]
            base[0] = 0
        base[x-1] = 1
        # aScore[0] = aScore[0] + base[3] 홈플레이트 밟은걸 카운팅
        if ond == 0:
            aScore[0] = aScore[0] + base[3]
        else:
            bScore[0] = bScore[0] + base[3]

    # print(base)

    #
    # if x == 1:
    #     if base == [0, 0, 0, 0]:
    #         base = [1, 0, 0, 0]
    #     elif base == [1, 0, 0, 0]:
    #         base = [1, 1, 0, 0]
    #     elif base == [1, 1, 0, 0]:
    #         base = [1, 1, 1, 0]
    #     elif base == [1, 1, 1, 0]:
    #         base = [1, 1, 1, 1]
    #     elif base == [0, 1, 1, 0]:
    #         base = [1, 0, 1, 1]
    #     elif base == [0, 1, 0, 0]:
    #         base = [1, 0, 1, 0]
    #     elif base == [0, 0, 1, 0]:
    #         base = [1, 0, 0, 1]
    #     print(base)
    # elif x == 2:
    #     if base == [1, 0, 0, 0]:
    #         base = [0, 1, 0, 1]
    #     elif base == [0, 1, 0, 0]:
    #         base = [0, 1, 0, 1]
    #     elif base == [0, 0, 1, 0]:
    #         base = [0, 1, 0, 1]
    #     elif base == [1, 1, 0, 0]:
    #         base = [0, 1, 1, 1]
    #     elif base == [1, 1, 1, 0]:
    #         base = [0, 1, 1, 2]
    #     elif base == [0, 1, 1, 0]:
    #         base = [0, 1, 0, 2]
    #     elif base == [0, 1, 0, 0]:
    #         base = [0, 1, 0, 1]
    #     elif base == [0, 0, 1, 0]:
    #         base = [0, 1, 0, 1]
    #     elif base == []
    #     print(base)
    # elif x == 3:
    #     if base == [0, 0, 0, 0]:
    #         base[0] = 1
    #         print(base)
    # elif x == 'H':
    #     base[3]=[1]
    #     print(base)

#
# def ScorePlus():
#


# ======================================================

# ===================================================

def Team():
    global ond
    if ond == 0:
        print(f"{offense} A팀  {aScore}")
        print(f"{defence} B팀  {bScore}")
    else:
        print(f"{defence} A팀  {aScore}")
        print(f"{offense} B팀  {bScore}")


def asd(x):
    global base
    if x == 'O':
        print("아웃 카운트 : ", OutCountTotal())
    elif x == 'D':
        print("아웃 카운트 : ", OutCountPlus())
    print(base)
    OND()
    base[3] = 0 #홈플레이트 밟은걸 0으로 초기화



# ====================================================


def K():
    print("삼진")
    asd('D')


def GO():
    print("그라운드 아웃")
    asd('D')


def FO():
    print("플라이 아웃")
    asd('D')


# ---------------------------------

def BB():
    OffenseBase(0)
    print("볼넷")
    asd('O')


def OneB():
    OffenseBase(1)
    print("안타")
    asd('O')


def DoubleB():
    OffenseBase(2)
    print("2루타")
    asd('O')


def ThreeB():
    OffenseBase(3)
    print("3루타")
    asd('O')


def HR():
    OffenseBase('H')
    print("홈런")
    asd('O')


# ===========================================================================================

def Result():
    D1 = DiceTumble.Dice1()
    D2 = DiceTumble.Dice2()
    result = D1 + D2
    if result == 2:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        ThreeB()
    elif result == 3:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        BB()
    elif result == 4:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        DoubleB()
    elif result == 5:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        K()
    elif result == 6:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        GO()
    elif result == 7:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        OneB()
    elif result == 8:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        FO()
    elif result == 9:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        K()
    elif result == 10:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        DoubleB()
    elif result == 11:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        BB()
    elif result == 12:
        print(f"D1 : {D1}  D2 : {D2}")
        print("Value : ", D1 + D2)
        HR()




