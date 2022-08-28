import os
import shutil
from zipfile import ZipFile,BadZipFile


def sort(path_name, id_mb):
    unzip(f"source\\temp\\{path_name}")
    os.remove(f"source\\temp\\{path_name}")
    nm_pt = os.listdir(f"source\\temp\\{path_name.replace('.zip','')}")
    print(nm_pt)
    if ['bodys','eyes','smiles'] != nm_pt:
        return f"Forder not corect\n['bodys','eyes','smiles'] != {nm_pt}"
    else:
        print("cont")
        if os.path.exists(f"source\packs\{id_mb}"):
            print("f")
        else:
            print("fld")
            os.mkdir(f"source\packs\{id_mb}")

        shutil.move(f"source\\temp\\{path_name.replace('.zip','')}",f"source\\packs\\{id_mb}\\{path_name.replace('.zip','')}")
        if os.path.exists(f"source\\packs\\{id_mb}\\{path_name.replace('.zip','')}\\trash"):
            print("f")
        else:
            print("fld")
            os.mkdir(f"source\packs\{id_mb}\\{path_name.replace('.zip','')}\\trash")
        


def unzip(name):
    try:
        with ZipFile(name) as zip:
            zip.printdir()
            zip.extractall("source\\temp\\")
            print("Success")

    except BadZipFile as error:
        print(error)

