import re

N = int(input())
pattern = '^[_\.]\d+[a-zA-Z]*[_]?'
for n in range(0, N):
  text = input()
  m = re.search(pattern, text)
  if m != None:
    if m.end() == len(text):
      print('VALID')
    else:
      print('INVALID')
  else:
    print('INVALID')
