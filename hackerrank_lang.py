import re

langs = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'
pattern = '([A-Z]+)'
p = re.compile(pattern)
langsList = re.findall(p, langs)

patInput = '(\d+) ([A-Z]+)'
regInput = re.compile(patInput)

N = int(input())
for n in range(0, N):
  text = input()
  inputList = list(re.findall(regInput, text)[0])
  if inputList != None:
    lang = inputList[1]
    if lang in langsList:
      print('VALID')
    else:
      print('INVALID')
  else:
    print('INVALID')