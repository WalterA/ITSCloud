# # def area_rettangolo():
# #     print("questa")
# # area_rettangolo()

# def area_rettangolo(x:float,y:float) -> float:
#     #print(f"x={x} e y={y}")
#     area=x*y
#     #print(f"l'area {area}")
#     return area

# #lato1, lato2=2,3

# aut:float=(area_rettangolo(2,5))
# print("latoè  "\
#       +"ciao" aut)
# #area_rettangolo(lato1,lato2) #--> (y=lato1, x=lato2)
d1:dict={"pippo":2,"pluto":1,"topolino":5}

def rewrite_dict(d:dict[str, int]) -> dict[str,int]:
    somma=sum (list(d1.values()))
    print(f"la somma dei valori è:",somma)
    for k, v in d.items():
     d[k]=v/somma #-> float
    return d, somma
    
d1,somma= rewrite_dict(d1)
print(d1, somma)

def change_keys_with_sum(d:dict[str,int], sum:float) -> dict[str,int]:
    out={}
    for key in d:
      out[key] =d[key] / sum 
    return out

out:dict[str, float]=change_keys_with_sum(d1,somma)