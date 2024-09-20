#!/bin/python3
#
# this is based on reading pixel values from gifs (containing a color-table!)
# if you have a png/jpeg try to 'convert image.png image.gif' first.
#
# original code:
# https://github.com/robole/fetching
#

W = 24
H = 24
X = 2
Y = 2
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument('-x', "--startx", help="start x position", type=int, default=X)
parser.add_argument('-y', "--starty", help="start y position", type=int, default=Y)
parser.add_argument('-W', "--width", help="sprite width", type=int, default=W)
parser.add_argument('-H', "--height", help="sprite height", type=int, default=H)
parser.add_argument('-u', "--indexx", help="sprite x index", type=int, default=0)
parser.add_argument('-v', "--indexy", help="sprite y index", type=int, default=0)
parser.add_argument('-c', "--color", help="use color palette (0,1,..)", type=int, default=0)
parser.add_argument('-f', "--fatness", help="stretch x", type=int, default=0)
parser.add_argument('-m', "--mirror", action=argparse.BooleanOptionalAction)
parser.add_argument('-p', "--print", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

# Importing Image from PIL package
from PIL import Image

# creating a image object
im = Image.open(r"".join(args.filename))
px = im.load()
ncol = []
for col in im.palette.colors:
 ncol.append(col)
xs = args.startx
ys = args.starty
xm = args.width
ym = args.height
xi = args.indexx*(xm+1)
yi = args.indexy*(ym+1)

xs += xi
ys += yi

print("""#!/usr/bin/env bash
f=3 b=4
for j in f b; do
        for i in {0..7}; do
                printf -v $j$i %b "\e[${!j}${i}m"
        done
done
for i in {0..7}; do
                printf -v g$i %b "\e[9${i}m"
done
bd=$'\e[1m'
rt=$'\e[0m'
iv=$'\e[7m'
cat << EOF""")
### COLORS ###
# foreground:
# f0=black, f1=red, f2=green, f3=yellow, f4=blue, f5=magenta, f6=cyan, f7=white
#
# g0=bright black, g1=bright red, g2=bright green, g3=bright yellow, g4=bright blue, g5=bright magneta, g6=bright cyan, g7=bright white
#
# background:
# b0=black, b1=red, b2=green, b3=yellow, b4=blue, b5=magenta, b6=cyan, b7=white

#kolingoriginal =
#     ["$f0","$f1","$f2","$f3","$f4","$f5","$f6","$f7","$g0","$g1","$g2","$g3","$g4","$g5","$g6","$g7"]
col0 =["$f0","$f1","$f2","$f3","$f2","$f5","$g0","$f7","$g0","$f7","$f3","$f7","$f1","$f3","$g7","$f7"] #for 'smbenemies.gif'
col1 =["$f0","$f4","$f3","$f1","$f7","$f2","$g3","$f5","$g5","$g1","$g2","$f1","$g4","$g5","$g6","$f7"] #for 'smb2players.gif'
col2 =["$f0","$f1","$f2","$f3","$f4","$f4","$f6","$f6","$g0","$f3","$g2","$g3","$f7","$g5","$g6","$g7"] #for 'megaman.gif' (megaman)

# if you have a new gif with a new color palette, first uncomment the line starting with 'col3='
# then insert 'col3' into the list 'palette' below [col0,col1,col2,col3] 
# then use color palette 3 by changing mfetch.py argument '-c2' (or whatever) to '-c3'
# now it's time to adjust the colors

#col3=["$f0","$f1","$f2","$f3","$f4","$f5","$f6","$f7","$g0","$g1","$g2","$g3","$g4","$g5","$g6","$g7"]

palette = [col0, col1, col2]

dot = "█"
odot= dot
if(args.fatness):
 fat = args.fatness
 while(fat):
  dot+=odot
  fat-=1

for y in range(0,ym):
 for x in range(0,xm):
  if(args.mirror):
   p = px[xs+xm-x,ys+y] #r2l
  else:
   p = px[xs+x,ys+y] #l2r
  print( palette[args.color][p]+dot, end="")
  if(args.print):
   print( f"{p},", end="") #debug print color index
 print("")

print("")
print("EOF")
