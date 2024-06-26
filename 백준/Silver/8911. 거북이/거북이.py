import sys
t = int(sys.stdin.readline())
dx = [0,-1,0,1]
dy = [1,0,-1,0]

for _ in range(t):
    order = list(map(str, sys.stdin.readline().strip()))
    direction = 0
    min_x, min_y, max_x, max_y = 0,0,0,0
    x,y = 0,0
    
    for i in order:
        if i == 'F':
            x += dx[direction]
            y += dy[direction]
        elif i == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif i == 'L':
            if direction == 3: # 동쪽이면 북으로
                direction = 0
            else:
                direction += 1
        elif i == 'R':
            if direction == 0: # 북이라면 동쪽으로
                direction = 3
            else:
                direction -= 1
        min_x = min(min_x,x)
        min_y = min(min_y,y)
        max_x = max(max_x,x)
        max_y = max(max_y,y)
        
    print(abs(max_x - min_x) * abs(max_y - min_y))