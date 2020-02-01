class FileReader:
    def __init__(self,path_to_file):
        self._path_to_file = path_to_file 
    

    def read(self):
        try:
            with open(self._path_to_file) as f:
                return f.read()
        except FileNotFoundError:
            return ""

a = FileReader("fdskf;s")
print(a.read())
