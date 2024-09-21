#!/bin/python3
#
# this is based on reading pixel values from gifs (containing a color-table!)
# if you have a png/jpeg try to 'convert image.png image.gif' first.
#
# original code:
# https://github.com/robole/fetching
#

# default values
W = 24
H = 24
X = 2
Y = 2

#shell arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument('-x', "--startx", help="start x position", type=int, default=X)
parser.add_argument('-y', "--starty", help="start y position", type=int, default=Y)
parser.add_argument('-W', "--width", help="sprite width", type=int, default=W)
parser.add_argument('-H', "--height", help="sprite height", type=int, default=H)
parser.add_argument('-u', "--indexx", help="sprite x index", type=int, default=0)
parser.add_argument('-v', "--indexy", help="sprite y index", type=int, default=0)
parser.add_argument('-f', "--fatness", help="stretch x", type=int, default=0)
parser.add_argument('-m', "--mirror", action=argparse.BooleanOptionalAction)
parser.add_argument('-p', "--print", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

# Importing Image from PIL package
from PIL import Image

# creating a image object
im = Image.open(r"".join(args.filename))
px = im.load()
colors = []
for col in im.palette.colors:
 colors.append(col)
xs = args.startx
ys = args.starty
xm = args.width
ym = args.height
xi = args.indexx*(xm)
yi = args.indexy*(ym)

xs += xi
ys += yi

print("#!/usr/bin/env bash")
print("colors=(", end="")
for i in range(0,len(colors)):
 col = colors[i]
 print(f"\"{col[0]};{col[1]};{col[2]}\" ", end="")
print(")")

head = """
for c in ${!colors[@]}; do
 cl=${colors[$c]}
 printf -v c$c %b "\033[38;2;${cl}m"
done
bd=$'\e[1m'
rt=$'\e[0m'
iv=$'\e[7m'
cat << EOF"""

print(head)

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

#  if(p == 6):p=0
  print(f'$c{p}'+dot, end="")
  if(args.print):
   print( f"{p},", end="") #debug print color index
 print("")

print("")
print("EOF")
