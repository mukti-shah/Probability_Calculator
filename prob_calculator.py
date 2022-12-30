import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self,**kwargs):
        self.contents = [] 
        for keys, values in kwargs.items():
            for i in range(values):
                self.contents.append(keys)
    
    def draw(self,arg):
        removed_balls = []
        if arg>len(self.contents):
            return self.contents
        
        for i in range(arg):
            a = random.randint(0,len(self.contents)-1)
            removed_balls.append(self.contents.pop(a))
        return removed_balls

      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
    count = 0
    
    for i in range(num_experiments):
        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        outcome = hat_copy.draw(num_balls_drawn)

        for color in outcome:
          if color in expected_balls_copy:
            expected_balls_copy[color] -= 1
            
        if all(x<=0 for x in expected_balls_copy.values()) :
            count+=1
    
    return count/num_experiments