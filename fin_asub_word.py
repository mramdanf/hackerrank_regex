import re

setences = []
N = int(input())
for i in range(0, N):
  setences.append(input())

checkWord = []
Q = int(input())
for i in range(0, Q):
  checkWord.append(input())

total = 0
for i in range(0, N):
  for j in range(0, Q):
    p = re.compile('\w+('+checkWord[j]+')\w+')
    groups = re.findall(p, setences[i])
    total += len(groups)

print (total)