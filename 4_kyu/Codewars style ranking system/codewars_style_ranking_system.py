# https://www.codewars.com/kata/51fda2d95d6efda45e00004e

class User:
    RANKS = (-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8)
    i = 0
    rank = RANKS[i]
    progress = 0
         
    def inc_progress(self, activity):
        if activity not in self.RANKS:
            raise ValueError
        
        delta = self.RANKS.index(activity) - self.RANKS.index(self.rank)
        if delta == 0:
            self.progress += 3
        elif delta == -1:
            self.progress += 1
        elif delta > 0:
            self.progress += delta * delta * 10
                    
        while self.progress >= 100 and self.i < 15:
            self.i += 1
            self.progress -= 100
            self.rank = self.RANKS[self.i]
            
        if self.i == 15:
            self.progress = 0
