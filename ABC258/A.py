k = int(input())

if k < 60:
  hh = 21
  mm = k
else:
  hh = 22
  mm = k - 60

print('{}:{:02}'.format(hh, mm))
