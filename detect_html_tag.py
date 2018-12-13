import re

N = int(input())

result = set()
for n in range(0,N):
  text = str(input())
  p = re.compile('<\s?([\w]+)')
  groups = re.findall(p, text)
  if groups != None:
    for g in groups:
      result.add(g)

resultList = list(result)
resultList.sort()
print(";".join(resultList))
    
 
