P = list(map(int, input().split()))
ans = [chr(ord('a') + x - 1) for x in P]
print(''.join(ans))
