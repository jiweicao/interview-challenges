"""
  Answer by: jiweicao
  Copyright: 2013 Jiwei. All rights reserved.
  
  From: https://www.codeeval.com
  Challenge Description:
  
  There is a monkey which can walk around on a planar grid. The monkey can move one space at a time left, right, up or down. That is, from (x, y) the monkey can go to (x+1, y), (x-1, y), (x, y+1), and (x, y-1). Points where the sum of the digits of the absolute value of the x coordinate plus the sum of the digits of the absolute value of the y coordinate are lesser than or equal to 19 are accessible to the monkey. For example, the point (59, 79) is inaccessible because 5 + 9 + 7 + 9 = 30, which is greater than 19. Another example: the point (-5, -7) is accessible because abs(-5) + abs(-7) = 5 + 7 = 12, which is less than 19. How many points can the monkey access if it starts at (0, 0), including (0, 0) itself?
  
  Input sample:
  
  There is no input for this program.
  
  Output sample:
  
  Print the number of points the monkey can access. It should be printed as an integer — for example, if the number of points is 10, print "10", not "10.0" or "10.00", etc.
  
"""
from collections import deque

SUM_LIMITE = 19
visited = []
que = deque()

def digit_sum(x):
    s = str(x)
    return sum(int(c) for c in s)
    
def check_valid(x,y):
    if digit_sum(x) + digit_sum(y) <= SUM_LIMITE and x <= y:
        if not (x,y) in que:
            que.append((x,y))

def main():
    cnt_4 = 0
    cnt_8 = 0
    que.append((0,0))
    while que:
        cur = que.popleft()
        x = cur[0]
        y = cur[1]
        if not cur in visited:
            visited.append(cur)
            if x == 0 or x==y:
                cnt_4 += 1
            else:
                cnt_8 += 1
        check_valid(x+1,y)
        check_valid(x,y+1)

    print (cnt_4-1)*4+(cnt_8*8)+1
        
if __name__=="__main__":
    main()
