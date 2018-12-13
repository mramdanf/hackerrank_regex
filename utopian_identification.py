import re

pattern = '^[a-z]{0,3}\d{2,8}[A-Z]{3,}'
p = re.compile(pattern)

N = int(input())
for n in range(0, N):
  text = input()
  m = re.search(pattern, text)
  if m != None:
    if len(text) == m.end():
      print('VALID')
    else:
      print('INVALID')
  else:
    print('INVALID')