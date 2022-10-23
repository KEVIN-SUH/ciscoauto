test1={"a":{"ab":1},"b":{"bb":2},"c":{"cc":3}}
print(list(test1.items()))

#for i in list(test1.items()):
print(list(dict(test1.items())["a"].keys()))
print(test1.keys())
