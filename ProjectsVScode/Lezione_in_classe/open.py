
# reader = open("ok.txt", encoding="utf-8")
reader = open("ok.txt")
# print(reader)
# reader.readline()
# reader.close()

# try:
#     reader.readline
#     print("try")
    
    
#     raise Exception("Eccezione")
# except Exception:
#     print("ex")
# finally:
#     print("fi")
#     reader.close()S
    
# with open("ok.txt","r") as reader: #whith chiude connessioni o letture di file
#     #print(reader.read("""size""" )) size sono bit
#     #print(reader.readline(2)) #caratteri
#     line = reader.readline()
#     line_counter = 0
#     while line != '':
#         print(f"{line} -number:{line_counter}")
#         line = reader.readline()
#         line_counter += 1

    
# with open("ok.txt","w") as reader: #whith chiude connessioni o letture di file
#     reader.write(f"Ciao sono fabio")
    
# with open("ok.txt", "a") as reader: #whith chiude connessioni o letture di file
#     l = ["ciao \n ugo \n fabio"]
#     reader.writelines(l)



# class Context_manager:
    
#     def __enter__(self):
#         print("Rescource")
#         return self
    
#     def __exit__(self, exc_type, exc_valure, traceback):
#         if exc_type is not None:
#             pass
#         print("risolsa rilasciata") 
#         return False
# try:
#     with Context_manager() as manager:

#         print("sono dentro whith")
# except Exception:
#     print()

try:
    n1 = 1
    n2 = 2
    risu = 1
    if risu > 0:
        risu = n1 - n2
        print(risu)
        
    raise Exception(f"{risu}")
except Exception as a:
    print(f"non deve andare sotto lo 0 il tuo valore è {a}")
    
else:
    print("els")
finally:
    print("fina")
    
