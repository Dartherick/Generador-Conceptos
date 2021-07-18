from PIL import Image
import os

class GeneradorConceptos():
    def __init__(self,Path):
        self.Path = Path
    
    def FindCategories(self):
        self.Categories = {}
        for File in os.listdir(self.Path):
            if not('.' in File):
                self.Categories[File] = {}

    def FindSubCategories(self):
        for i in self.Categories.keys():
            for File in os.listdir(os.path.join(self.Path,i)):
                if not('.' in File):
                    self.Categories[i][File] = []

    def FindPictures(self):
        for i in self.Categories.keys():
            for j in self.Categories[i].keys():
                print(j)

Maldito = GeneradorConceptos('C:/Users/darth/Downloads/Trimestre 11')
Maldito.FindCategories()
Maldito.FindSubCategories()
print(Maldito.Categories)
#Maldito.FindPictures()