from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os

def Gpsinfo(exif):
    if 'GPSInfo' in exif:
        geo_cordinate='{0} {1} {2:.2f} {3}, {4} {5} {6:.2f} {7}'.format(
         exif['GPSInfo'][2][0][0],
         exif['GPSInfo'][2][1][0],
         exif['GPSInfo'][2][2][0] / exif['GPSInfo'][2][2][1],
         exif['GPSInfo'][1],
         exif['GPSInfo'][4][0][0],
         exif['GPSInfo'][4][1][0],
         exif['GPSInfo'][4][2][0] / exif['GPSInfo'][4][2][1],
         exif['GPSInfo'][3]
         )
def Obt_exif(image_path):
    mi_imagen = Image.open(image_path)
    exif_datos=mi_imagen.getexif()
    inf={}
    for tag,value in exif_datos.items():
        decodificado= TAGS.get(tag,tag)
        inf[decodificado]=value
    Gpsinfo(inf)
    return inf

def ObtMeta():
    dire= input("Ingrese la ruta de imagenes:")
    os.chdir(dire)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print("A continuacion se mostrara el metadata del siguiente archivo: %s"%(name))
            input()
            try:
                exifData={}
                exif = Obt_exif(name)
                for metadata in exif:
                    print("Metadata: %s - Value: %s"%(metadata,exif[metadata]))
                print("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
ObtMeta()

