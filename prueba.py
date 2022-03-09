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

def modeloImg(path, name):
   
    original = 'original.png'
    

    img_mask = 'mask.png'

    zone = 'zone.png'
    
    return original,img_mask,zone
