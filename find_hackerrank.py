import re

N = int(input())
patStartWith = '^hackerrank.*'
patEndWith = '.+hackerrank$'
patStartEndWith = '^hackerrank$'
for n in range(0, N):
  text = input()
  if (re.search(patStartEndWith, text)):
    print(0)
  elif (re.search(patStartWith, text)):
    print(1)
  elif (re.search(patEndWith, text)):
    print(2)
  else:    
    print(-1)