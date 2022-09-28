class Action:
    
    def __init__(self, game, playground, team):
        self.name_dict = {'K':'삼진', 'GO':'그라운드 아웃', 'FO':'플라이 아웃', 'BB':'볼넷',
                          'OneB':'안타', 'DoubleB':'2루타', 'ThreeB':'3루타', 'HR':'홈런'}
        self.game = game
        self.playground = playground
        self.team = team
        
    def get_action(self, name):
        if name in ['K','GO','FO']:
            print(self.name_dict.get(name))
            return self.game.set_out()
        else:
            print(self.name_dict.get(name))
            self.get_on_base(name)
            return self.game.check_out_cnt()
        
    def _rotate_base(self):
        if self.playground.base.pop(-1):
            self.team.score[-1] += 1
        self.playground.base.insert(0,1)
            
    def get_on_base(self, name):
        if name == 'BB' or name == 'OneB': self._rotate_base()
        elif name == 'DoubleB':
            for _ in range(2): self._rotate_base()
        elif name == 'ThreeB':
            for _ in range(3): self._rotate_base()
        elif name == 'HR':
            self.team.score[-1] += (sum(self.playground.base)+1)
            self.playground.base = [0,0,0]