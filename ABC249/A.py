def calc(a,b,c,x):
  period = x // (a + c)
  r = x % (a + c)
  return (period * a + min(a, r)) * b

a,b,c,d,e,f,x = map(int, input().split())

takahashi = calc(a,b,c,x)
aoki = calc(d,e,f,x)

if takahashi > aoki:
  print("Takahashi")
elif takahashi < aoki:
  print("Aoki")
else:
  print("Draw")
