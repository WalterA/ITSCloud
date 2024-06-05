


# file = open("ok.txt")
# try:
    
#     print(file)
# finally:
#     file.close()
    
with open("ok.txt") as file: #whith chiude connessioni o letture di file
    
    pass


class Context_manager:
    
    def __enter__(self):
        print("Rescource")
        return self
    
    def __exit__(self, exc_type, exc_valure, traceback):
        if exc_type is not None:
            pass
        print("risolsa rilasciata") 
        return False

with Context_manager() as manager:

    print("sono dentro whith")