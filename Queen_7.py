N=4
board=[]
def solve(row):
    if row==N:
        return True
    for col in range(N):
        safe=True

        for i in range(row):
            if board[i]==col or abs (board[i]-col)==row-i :
                safe= False
                break

        if safe:
            board.append(col)

            if solve(row+1):
                return True

            board.pop()
    return False

if solve(0):
    for row in range(N):
        for col in range(N):
            print("Q" if board[row]==col else "-", end=" ")
        print()
