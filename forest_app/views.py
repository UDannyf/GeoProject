from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage

from . import prueba
from . import reduceimg


def upimage(request):
    try:        
        upload = request.FILES['upload']
        fss = FileSystemStorage()        
        file = fss.save(upload.name, upload)        
        file_url = fss.base_url
        original, mask, zone = reduceimg.modeloImg(fss.location,'/'+upload.name)        
        #original, mask, zone = prueba.modeloImg(fss.location,'/'+upload.name)        
        return render(request, 'shapeimg.html', {'f1':file_url+original, 'f2':file_url+mask, 'f3':file_url+zone, 'f4':file_url+'shape.zip'})
    except:
        return render(request, 'upimage.html')