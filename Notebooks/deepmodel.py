'''
This file uses the deep forest library (tree crown classification model) 
to find a set of trees in a raster image. The trees found are grouped to 
generate a binary image and with Opencv morphological transformation 
operations (erosion and opening) a mask is generated that is added to the original image.
Then, with skimage functions, the contours of the image are obtained. 
Finally, with the contours obtained, a shapefile is made of the number of polygons that exist in the image.

Author: Danny Ucho
'''

from deepforest import main
from skimage import measure
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import fiona

igpmath = "Mosaicos/bosqueed.tif"
#imgpath = "Mosaicos/openaerealmap.tif"
#imgpath = "Mosaicos/bosque1.jpg"

class DeepModel:

    def __init__(self, imagen):
        #self.imgpath = imgpath
        self.dataset = rasterio.open(imagen)
        self.mask = 255*np.ones(imagen.shape,np.uint8)
        self.imagen = imagen 
    
    
    #Function aply to box dataframe
    def function_box(self,row):
        x = int(row['xmin'])
        y = int(row['ymin'])
        X1 = int(row['xmax'])
        Y1 = int(row['ymax'])    
        self.mask[y:Y1,x:X1] = 0


    #Generate binary mask
    def morfology_trans(img,mask):
        kernel = np.ones((7, 7), 'uint8')
        erosion = cv2.erode(mask, kernel, iterations=10)
        erosion = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel, iterations=10)
        #erosion = cv2.dilate(mask, kernel,iterations=50)
        b_mask = cv2.bitwise_and(img, erosion)
        return b_mask

    def generate_polygon(contours, dataset):
        poligono = []
        for cnt in contours : 
            poligono1 = []
            for ind in cnt:
                x1,y1 = dataset.xy(ind[0], ind[1])
                poligono1.append([x1,y1,0.0])
            poligono.append([poligono1])
        fn = 'Poligonos/new.shp'
        opts = {
            'driver': 'ESRI Shapefile',
            'schema': {'geometry': '3D MultiPolygon', 'properties': {}},
            'crs' : dataset.crs
        }
        with fiona.open(fn, mode='w', **opts) as c:
            c.write({'geometry': {'type': 'MultiPolygon', 'coordinates': poligono}, 'properties': {}})

    #Model uses
    def model_deep(self):
        m = main.deepforest()
        box = m.predict_image(self.imagen, return_plot=False)    
        box.apply(lambda r : function_box(r), axis = 1)
        fg = morfology_trans(self.imagen, self.mask)
        contours = measure.find_contours(fg[:,:,1], 0.8)
        generate_polygon(contours, self.dataset)
        return "Succesfull"


