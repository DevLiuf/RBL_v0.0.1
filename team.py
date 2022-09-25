class Team:
    
    def __init__(self, ond=0):
        self.ond = ond
        self.score = [0]
        
    def get_ond(self):
        return "공격" if self.ond == 0 else "수비"
    
    def set_ond(self):
        if self.ond == 0: self.ond = 1
        else:
            self.ond = 0
            self.score.append(0)