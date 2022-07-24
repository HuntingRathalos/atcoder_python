h,w = map(int, input().split())
r,c = map(int, input().split())
count = 0
if r != 1:
  count += 1
if r < h:
  count += 1
if c != 1:
  count += 1
if c < w:
  count += 1

print(count)
