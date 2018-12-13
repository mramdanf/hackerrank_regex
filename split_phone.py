import re

N = int(input())
for n in range(0,N):
  text = str(input())
  m = re.search('^(\d{1,3})[-|\s](\d{1,3})[-|\s](\d{4,10})$', text)  
  if m != None:
    print ('CountryCode='+m.group(1)+',LocalAreaCode='+m.group(2)+',Number='+m.group(3))
    
 
