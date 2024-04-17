l=[0,1,1,2,3,4,5]
for i in range(len(l)):
    print(l[i])
d={"pippo":2,"pluto":1,"topolino":5}
for key in d:
    print(f"Chiave = {key} --> {d[key]}")
keys=list(d.keys())
print(keys)
values=list(d.values())
print(values)
i=0
while i < len(keys):
     print(f"Chiave = {keys[i]} --> {[values[i]]}")
     i += 1
     