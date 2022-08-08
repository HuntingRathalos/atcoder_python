x, y = map(int, input().split())
ans = 0
if x < y:
    # 一般に、X を Y で割って小数点以下を切り上げた値は(X + Y - 1) // Y
    ans = (y - x + 10 - 1) //10
print(ans)
