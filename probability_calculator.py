import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self,**kwargs):
    self.colordict = kwargs
    self.contents = []
    self.colors =[]

    for k,v in kwargs.items():
        for x in range(v):
          self.colors.append(k)
          self.contents.append(k)


  def draw(self,num_todraw):
    drawn =[]
    
    if num_todraw > len(self.contents):
      return self.contents
    else:

      while (num_todraw > 0):
        length_list = len(self.contents)
        rando_num = random.randrange(length_list)

        drawn.append(self.contents[rando_num])
        del self.contents[rando_num]
        
        num_todraw -= 1

    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  color_list = hat.contents
  successful_draw = 0

  for x in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    
    draw_list = new_hat.draw(num_balls_drawn)
    
    draw_dict = {}
    #creating dictionary from what was drawn
    for color in draw_list:
      num_of_color = draw_list.count(color)
      draw_dict[color] = num_of_color

    
    #comparing drawn dict to given dict (expected balls)
    
    match = False

    #print("Draw")
    #print(draw_dict)
    #print(expected_balls)

    for key in expected_balls.keys():
      if key in draw_dict.keys():
        print (draw_dict[key])
        print( expected_balls[key])
        if draw_dict[key] >= expected_balls[key]:
          match = True
        else:
          match = False
          break
      else:
        match = False
        break
          
        #print("compared " + k + " to " + x)
        #print("compared " + str(y) + " to " + str(v) + " and returned " + str(match))
        
    print(match)
    if match == True:
      successful_draw += 1
    
    
    #print(draw_dict)


  print(successful_draw)
  probability = successful_draw / num_experiments
  return probability 
  
  
