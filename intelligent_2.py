grid=[
    ['S', '.', '#', '.'],
    ['#', '.', '#', '.'],
    ['#', '.', '.', '.'],
    ['.', '#', '.', 'G']
]
print("Initial grid:\n ")
for row in grid:
    print(' '.join(row))
position=(0,0)
goal=(3,3)
visited=set()

print("Starting position: ",position)
print("\n Goal position: ",goal)

while position!=goal:
    r,c=position
    visited.add(position)
    moves=[(r+1,c),(r,c+1),(r-1,c),(r,c-1)]
    
    for nr,nc in moves:
        if (0<=nr<4 and 0<=nc<4 and grid[nr][nc]!='#' and nr,nc not in visited):
            position=(nr,nc)
            break;
    else:
        print("goal not reached!!")
        break;
    print("\nposition: ",position)    
if position==goal:
    print("\n goal reached!!")