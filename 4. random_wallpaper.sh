#! /bin/bash

DIR=''
PIC=$(find $DIR -type f | shuf -n1)
gsettings set org.gnome.desktop.background picture-uri "file://$PIC"
