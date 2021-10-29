from random import randint
from pygame.color import THECOLORS

col = 10

Directions = ["up", "left", "down", "right"]
def make_pattern(n : int) -> list():

    if (n == 1) : 
        return [5]
    
    ans = [0]
    n -= 1
    blocked = -1
    while n:
        curr_dir= Directions.copy()
        length = 4
        if blocked != -1: 
            curr_dir.__delitem__(blocked)
            length -= 1

        side = curr_dir[randint(0, length-1)]

        if side == 'up':
            ans.append(ans[-1]-col)
            blocked = 2
        elif side == 'left':
            ans.append(ans[-1]+1)
            blocked = 3
        elif side == 'down':
            ans.append(ans[-1]+col)
            blocked = 0
        else:
            ans.append(ans[-1] - 1)
            blocked = 1
        
        n -= 1
    
    for i in range(len(ans)):
        ans[i] += 5
    return ans

# block = {
#     'id' : 0,
#     'width' : 40,
#     'height' : 40,
#     'color' : THECOLORS["orange"],
# }

# a = block.copy()
# a['id'] = 5
# a['color'] = THECOLORS['green']
# print(a)
# print(block)