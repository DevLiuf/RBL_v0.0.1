from random import choice

class Game:
    
    def __init__(self):
        self.outcnt = 0
        self.inning = 2
        self.result_matrix = {2:'ThreeB', 3:'BB', 4:'DoubleB', 5:'K', 6:'GO',
                       7:'OneB', 8:'FO', 9:'K', 10:'DoubleB', 11:'BB', 12:'HR'}
        
    def result(self):
        D1, D2 = choice([1,2,3,4,5,6]), choice([1,2,3,4,5,6])
        print('D1 : {}  D2 : {}'.format(D1, D2))
        print('Value : {}'.format(D1 + D2))
        return self.result_matrix.get(D1+D2)
    
    def set_out(self):
        self.outcnt += 1
        return self.check_out_cnt()
        
    def check_out_cnt(self):
        print("아웃 카운트 : {}".format(self.outcnt))
        if self.outcnt == 3:
            print("======공수교대======")
            self.outcnt = 0
            return True
        else: return False
        
    def get_inning(self):
        return self.inning//2