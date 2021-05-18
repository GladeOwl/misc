#!/usr/bin/python3

import os
import random

# The Wallpaper Folder
folder = ''

def run():
    # Scan
    files = os.listdir(folder)

    # Select a random wallpaper
    random_wallpaper = files[random.randrange(0, len(files))]

    # Set wallpaper
    path = os.path.join(folder, random_wallpaper)
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:" + path)

if __name__ == '__main__':
    run()
