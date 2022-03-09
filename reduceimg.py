import cv2 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from deepforest import main
from skimage import measure
import rasterio
import fiona
from pprint import pprint
import zipfile
import zlib


def generateShape(path):
    #path = '/uploaded'
    try:
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED
    zf = zipfile.ZipFile(path +"/shape.zip", mode="w")
    try:
        zf.write(path+"/data.shp", compress_type=compression)
        zf.write(path+"/data.cpg", compress_type=compression)
        zf.write(path+"/data.dbf", compress_type=compression)
        zf.write(path+"/data.prj", compress_type=compression)
        zf.write(path+"/data.shx", compress_type=compression)
    finally:
        zf.close()


def modeloImg(path, name):
    m = main.deepforest()
    m.use_release()

    #load image
    imgpath = path + name
    imagen = cv2.imread(imgpath)

    #create image original to visual
    img = cv2.resize(imagen, (300, 300))
    cv2.imwrite(path+'/original.png',img)
    original = 'original.png'

    #deepforest get dataframe - mask    
    box = m.predict_image(path=imgpath, return_plot=False)
    mask = 255*np.ones(imagen.shape,np.uint8)
    def fun(row):
        x = int(row['xmin'])
        y = int(row['ymin'])
        X1 = int(row['xmax'])
        Y1 = int(row['ymax'])    
        mask[y:Y1,x:X1] = 0
    box.apply(lambda r : fun(r), axis = 1)
    
    #preprocesing with erode and open for make mask-image
    kernel = np.ones((7, 7), 'uint8')
    erosion = cv2.erode(mask, kernel, iterations=100)
    erosion = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel, iterations=50)
    er = cv2.resize(erosion, (300, 300))
    cv2.imwrite(path+'/mask.png',er)
    img_mask = 'mask.png'

    #zone not forest include
    fg = cv2.bitwise_and(imagen, erosion)
    f= cv2.resize(fg, (300, 300))
    cv2.imwrite(path+'/zone.png',f)
    zone = 'zone.png'

    #define contours    
    dataset = rasterio.open(imgpath)
    contours = measure.find_contours(fg[:,:,1], 0.8)
    poligono = []
    for cnt in contours : 
        poligono1 = []
        for ind in cnt:
            #print(ind)
            x1,y1 = dataset.xy(ind[0], ind[1])
            poligono1.append([x1,y1,0.0])
        poligono.append([poligono1])

    #generate shapefile
    fn = path+'/data.shp'
    opts = {
        'driver': 'ESRI Shapefile',
        'schema': {'geometry': '3D MultiPolygon', 'properties': {}},
        'crs' : dataset.crs
    }
    with fiona.open(fn, mode='w', **opts) as c:
        c.write({'geometry': {'type': 'MultiPolygon', 'coordinates': poligono}, 'properties': {}})

    #create zipfile
    generateShape(path)
    
    return original,img_mask,zone
