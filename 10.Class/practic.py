#File 實體物件的設計:包裝讀檔的程式

class File:
    def __init__(self, name):
        self.name = name
        self.file = None #尚未開啟檔案:初始化尚未開啟

    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")

    def read(self):
        return self.file.read()
    
    def close(self):
        self.file.close()
#讀取第一個檔案
f1 = File("data.txt")
f1.open()
data = f1.read() #讀取檔案
f1.close() #關閉檔案
print(data)

