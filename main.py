from PIL import Image
import os

class GeneradorConceptos():
    def __init__(self,Path):
        self.Path = Path
    
    def FindFolders(self):
        self.Folders = []
        for File in os.listdir(self.Path):
            if not('.' in File):
                self.Folders.append(File)

        print(self.Folders)

        #print(os.listdir(os.path.join(self.Path,self.Folders[0])))

Maldito = GeneradorConceptos('C:/Users/darth/Downloads/Trimestre 11')
Maldito.FindFolders()