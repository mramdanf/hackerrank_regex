import re

N = int(input())
total = 0
pattern = 'hackerrank'
for n in range(0, N):
  text = input()
  p = re.compile(pattern, re.IGNORECASE)
  groups = re.findall(p, text)
  total += len(groups)
print (total)
  