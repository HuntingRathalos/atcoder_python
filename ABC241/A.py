a = list(map(int, input().split()))

for i in range(3):
  first = a[0]
  second = a[first]
  third = a[second]
print(third)
