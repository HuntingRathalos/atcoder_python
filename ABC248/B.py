A, B, K = map(int, input().split())

cur = A
count = 0

while cur < B:
    cur *= K
    count += 1

print(count)
