s = input()
if s[0] == s[1] == s[2]:
  print(-1)
else:
  for i in range(3):
    if(s.count(s[i]) == 1):
      print(s[i])
      break
