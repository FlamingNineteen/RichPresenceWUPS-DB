from ftplib import FTP
import json as JSON
import xml.etree.ElementTree as ET
import os as OS

print('''
Thank you for contributing to the Wii U Rich Presence Plugin.

Before starting, please check that you have ftpiiu installed and enabled, and that you toggled "Allow access to system files." on.
''')

x=0
add = False
if not OS.path.exists("downloads"):
    OS.makedirs("downloads")
else:
    curtgas = OS.listdir("downloads")
    for i in curtgas:
        if ".tga" in i:
            try:
                if int(i[7-len(i):-4]) > x:
                    x = int(i[7-len(i):-4])
                    add = True
            except:
                pass
if add:
    x+=1
print(f"Starting at index {x}")

with open("titles.json", "r", encoding='utf-8') as local_file:
    titles = JSON.loads(local_file.read())
print("Loaded titles.json")

doLogin = True
while doLogin:
    try:
        ftp = FTP(input('Type the IP address of your Wii U: '))
        print("Logging in...")
        ftp.login()
        print("Successfully logged into ftpiiu server.")
        doLogin = False
    except:
        if input(f"Login failed. Try again? (Y/n): ").lower() == "n":
            exit()
        print("")

def list_dirs():
    global ftp
    d = []
    ftp.retrlines('LIST', d.append)
    for i in range(0,len(d)):
        d[i] = d[i][-8:]
    return d

lookupDirs = ["storage_mlc","storage_usb"]

ftp.cwd(f"/storage_mlc/usr/title")
print("In MLC")
maindirs = list_dirs()
print(maindirs)

for curdir in lookupDirs:
    try:
        ftp.cwd(f"/{curdir}/usr/title")
        print(f"In {curdir}")
        maindirs = list_dirs()
        print(maindirs)

        for subdir in maindirs:
            try:
                ftp.cwd(f"/{curdir}/usr/title/{subdir}")
                gamedirs = list_dirs()

                for dir in gamedirs:
                    try:
                        metaxml = []
                        ftp.retrlines(f'RETR /{curdir}/usr/title/{subdir}/{dir}/meta/meta.xml', metaxml.append)
                        metaxml = " ".join(metaxml)
                        root = ET.fromstring(metaxml)
                        name = root.find("longname_en").text
                        if name == "":
                            print("longname_en is blank. Skipping.")
                        else:
                            name.replace("\n"," ")
                            if name in titles:
                                print(f"\"{name}\" is already in titles.json. Skipping")
                            else:
                                print(f"Adding \"{name}\" to titles.json and downloading iconTex{x}.tga")
                                titles[name] = f'iconTex{x}.jpg'
                                try:
                                    with open(f'downloads/iconTex{x}.tga', 'wb') as local_file:
                                        ftp.retrbinary(f'RETR /{curdir}/usr/title/{subdir}/{dir}/meta/iconTex.tga', local_file.write)
                                    x+=1
                                except:
                                    print("Image download failed")
                                    del titles[name]
                    except:
                        print(f"Failed {dir}")
            except:
                print(f"Failed {subdir}")
    except:
        print(f"Failed {curdir}")
with open("titles.json", "w", encoding="utf-8") as local_file:
    JSON.dump(titles, local_file, ensure_ascii=False)
print("Updated titles.json")