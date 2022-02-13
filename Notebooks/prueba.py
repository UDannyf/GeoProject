from deepmodel import DeepModel
import cv2
from PIL import Image


imgpath = "Mosaicos/bosqueed.tif"
#imgpath = "Mosaicos/openaerealmap.tif"
#imgpath = "Mosaicos/bosque1.jpg"

imagen=Image.open(imgpath)
#imagen = cv2.imread(imgpmath)
d = DeepModel(imagen)
print(d.model_deep())