# mfetch.py
# pixel2colored ascii (4shell)

# examples

#### In image from 'sm2players.gif', at position (2,0) [-x,-y]  get pixels wide 24 , high 40 [-W24, -H40] from color table 1 [-c1]


`./mfetch.py -x2 -y0 -W24 -H40 -c1 ./smb2players.gif > my;chmod +x my; ./my` -> Mario (looking left)

#### The same but with the '-m' (mirror) flag

`./mfetch.py -x2 -y0 -W24 -H40 -c1 -m ./smb2players.gif > my;chmod +x my; ./my` -> Mario (looking right)

#### u/v are like x/y coordinates but for tiles (of width / height [-W/-H] )

`./mfetch.py -u7 -v1 -y14 -x2 -W23 -H32 -c1 ./smb2players.gif > my;chmod +x my; ./my`

`./mfetch.py -u2 -v0 -x0 -y7 -W31 -H34 -c2 ./megaman.gif > my;chmod +x my; ./my`

`./mfetch.py -x6 -y159 -W36 -H34 -c0 ./smbenemies.gif > my;chmod +x my; ./my` -> Bowser (left)

`./mfetch.py -x6 -y159 -W36 -H34 -c0 -m ./smbenemies.gif > my;chmod +x my; ./my` -> Bowser (right)

`./mfetch.py -x51 -y96 -W22 -H26 -c0 ./smbenemies.gif > my;chmod +x my; ./my` -> Bloober


#### Those sprite rips are not pixel aligned! You have to adjust (the exact position) on your own.  

#### Debug Mario2 / adding different images with different palettes

`./mfetch.py -y0 -x2 -W24 -H40 -c1 -m -f0 -p ./smb2players.gif > my;chmod +x my; ./my`

'-p' makes mfetch.py print the 'color index' (of the color used in the palette)

For any GIF you use which has NOT the same color palette as 
in the examples you have to add a new one yourself:

- `nano mfetch.py`

- 'Ctrl + w' (search for) `col3`

- remove the leading '#' to uncomment that line 

- the palette two lines below: 

  `palette = [col0, col1, col2]`

  has to be extended like:

  `palette = [col0, col1, col2, col3]`

  so palette 'col3' is now available via '-c3' shell argument to 'mfetch.py'

- now substitute the colors 
  the meaning of the colors is in the code (as comments)

# f0=black, f1=red, f2=green, f3=yellow, f4=blue, f5=magenta, f6=cyan, f7=white
# g0=bright black, g1=bright red, g2=bright green, g3=bright yellow, g4=bright blue, g5=bright magneta, g6=bright cyan, g7=bright white
`col3=["$f0","$f1","$f2","$f3","$f4","$f5","$f6","$f7","$g0","$g1","$g2","$g3","$g4","$g5","$g6","$g7"]`

- now, IF 'Marios pants' were 'bright red' instead of 'blue' what would we do?
  we'd search for the index of 'bright red' and put there the index of 'blue'
                                 /->------------------------->-\
`col3=["$f0","$f1","$f2","$f3","$f4","$f5","$f6","$f7","$g0","$g1","$g2","$g3","$g4","$g5","$g6","$g7"]`

- so it looks like that

`col3=["$f0","$f1","$f2","$f3","$f4","$f5","$f6","$f7","$g0","$f4","$g2","$g3","$g4","$g5","$g6","$g7"]`

- save (ctrl+o)

- now you test your 'change' in another shell to see if 'Marios pants' changed (in color)

- then you continue with the next 'wrong' color.


