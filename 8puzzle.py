# 8 Puzzle problem using basic python programming 
# It can be improved by taking initial state as in input

goal_state=[[1,2,3],[4,5,6],[7,8,0]]
initial_state=[[1,2,3],[4,0,6],[7,5,8]]

def print_state(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j],end=" ")
        print()
        
def move_right(a,b):
    temp=initial_state[a][b]
    initial_state[a][b]=initial_state[a][b+1]
    initial_state[a][b+1]=temp
    print_state(initial_state)
    
def move_left(a,b):
    temp=initial_state[a][b]
    initial_state[a][b]=initial_state[a][b-1]
    initial_state[a][b-1]=temp
    print_state(initial_state)
    
def move_up(a,b):
    temp=initial_state[a][b]
    initial_state[a][b]=initial_state[a-1][b]
    initial_state[a-1][b]=temp
    print_state(initial_state)
        
    
def move_down(a,b):
    temp=initial_state[a][b]
    initial_state[a][b]=initial_state[a+1][b]
    initial_state[a+1][b]=temp
    print_state(initial_state)
    
def blank_tile(initial_state):
        for i in range(3):
             for j in range(3):
                    if initial_state[i][j]==0:
                        a=i
                        b=j
                        return a,b 
                    
def check_goal():
    if initial_state==goal_state:
        print("Successful...")
        return 1
    else:
        return 0
       
    
print_state(initial_state)
n=0
while(n!=1):
    
    i,j=blank_tile(initial_state)
    print("Enter your move:1-Up,2-down,3-right,4-left")
    temp=int(input())
    if temp==1:
        move_up(i,j)
        n=check_goal()
        
    elif temp==2:
        move_down(i,j)
        n=check_goal()
            
    elif temp==3:
        move_right(i,j)
        n=check_goal()
    else:
        move_left(i,j)
        n=check_goal()
      

