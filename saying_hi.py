import re

N = int(input())
pattern = '^[Hh][Ii][\s][^D|^d]'
for n in range(0, N):
  text = input()
  if re.search(pattern, text) != None:
    print(text)