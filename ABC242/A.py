a,b,c,x = map(int, input().split())

if x <= a:
  print(1.0)
elif x > b:
  print(0)
else:
  p = c/(b - a)
  print(p)
