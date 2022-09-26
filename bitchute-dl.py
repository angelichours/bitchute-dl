import requests
import urllib.request
import re

bitchutedl = """██████╗ ██╗████████╗ ██████╗██╗  ██╗██╗   ██╗████████╗███████╗    ██████╗ ██╗     
██╔══██╗██║╚══██╔══╝██╔════╝██║  ██║██║   ██║╚══██╔══╝██╔════╝    ██╔══██╗██║     
██████╔╝██║   ██║   ██║     ███████║██║   ██║   ██║   █████╗█████╗██║  ██║██║     
██╔══██╗██║   ██║   ██║     ██╔══██║██║   ██║   ██║   ██╔══╝╚════╝██║  ██║██║     
██████╔╝██║   ██║   ╚██████╗██║  ██║╚██████╔╝   ██║   ███████╗    ██████╔╝███████╗
╚═════╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═════╝ ╚══════╝

"""

print(bitchutedl, "\nMade by angelichours :: https://github.com/angelichours :: angelichours@protonmail.com")

url = input("[*] Enter URL : ")
r = requests.get(url)
html = r.text
src = re.search('<source src="(.*)" type="', html)
title = re.search('<title>(.*)</title>', html)
dl = src.group(1)
print("[*] Downloading video...")
urllib.request.urlretrieve(dl, f"{title.group(1)}.mp4")

print("[*] Finished! :)")
