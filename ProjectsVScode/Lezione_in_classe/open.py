
# reader = open("ok.txt", encoding="utf-8")
reader = open("ok.txt")
# print(reader)
# reader.readline()
# reader.close()

try:
    reader.readline
    print("try")
    
    
    raise Exception("Eccezione")
except Exception:
    print("ex")
finally:
    print("fi")
    reader.close()
    
with open("ok.txt") as reader: #whith chiude connessioni o letture di file
    reader.readline()
#     print()




class Context_manager:
    
    def __enter__(self):
        print("Rescource")
        return self
    
    def __exit__(self, exc_type, exc_valure, traceback):
        if exc_type is not None:
            pass
        print("risolsa rilasciata") 
        return False
try:
    with Context_manager() as manager:

        print("sono dentro whith")
except Exception:
    print()