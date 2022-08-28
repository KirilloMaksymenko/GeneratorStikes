import os
import random
import cv2
from PIL import Image


def generator(name_pack):
    path_pack = f"source\\packs\\{name_pack}"

    list_smiles = []
    for item in os.listdir(path_pack +"\\"+ "smiles"):
        list_smiles.append(item)
    list_eyes = []
    for item in os.listdir(path_pack +"\\"+ "eyes"):
        list_eyes.append(item)
    list_bodys = []
    for item in os.listdir(path_pack +"\\"+ "bodys"):
        list_bodys.append(item)
    
    rn_sml = random.choice(list_smiles)
    rn_eye = random.choice(list_eyes)
    rn_bod = random.choice(list_bodys)

    print("[INFO] Generator fin")
    return rn_sml,rn_eye,rn_bod,path_pack

def stiker(name,id_mb):
    (rn_sml,rn_eye,rn_bod,path_pack) = generator(f"{name}")

    sml = Image.open(path_pack+"\\"+"smiles"+"\\"+rn_sml)
    bod = Image.open(path_pack+"\\"+"bodys"+"\\"+rn_bod)
    eye = Image.open(path_pack+"\\"+"eyes"+"\\"+rn_eye)
    
    bod.paste(eye,(0,0),eye)
    bod.paste(sml,(0,0),sml)

    bod.save(path_pack+"\\"+"trash"+"\\"+ str(id_mb) +".webp")
    print("[INFO] Creator fin")
    return path_pack+"\\"+"trash"+"\\"+str(id_mb) + ".webp"


    

