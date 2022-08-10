def solve():
    def calc(x, y, x2, y2):
        return (x - x2) ** 2 + (y - y2) ** 2 == 5

    x1,y1,x2,y2=map(int,input().split())
    p=[]
    p.append([x1+2,y1+1])
    p.append([x1+2,y1-1])
    p.append([x1-2,y1+1])
    p.append([x1-2,y1-1])
    p.append([x1+1,y1+2])
    p.append([x1+1,y1-2])
    p.append([x1-1,y1+2])
    p.append([x1-1,y1-2])
    for x, y in p:
        if calc(x, y, x2, y2):
            return True
    return False
  
print("Yes" if solve() else "No")

