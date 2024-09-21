# mfetching.py
# gif2fetching

### The script now contains the gif color palette
 
 `colors=("0;0;0" "32;43;64" "86;105;115" "121;121;121" "223;47;47" "65;97;251" "124;139;166" "97;211;227" "191;191;191" "255;186;162" "145;133;204" "217;255;255" "255;255;255" )`

 $c0 corresponds to the first color value "0;0;0"
 $c1 "32;43;64"
 .
 .
 .
 $c12 "255;255;255"

 There are (only) 13 colors in this palette. 

 Background colors are gone, there is only $c0, $c1, aso.
 
 The substitution is here:

 `printf -v c$c %b "\033[38;2;${cl}m"`

 see [https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters]

 and [https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit]

## Examples

#### 'megaman-one-up-fat'

`./mfetching.py -x176 -y88 -W16 -H16 -f1 ./megaman.gif > my;chmod +x my;./my`

#### 'megaman-one-up'

`./mfetching.py -x176 -y88 -W16 -H16 ./megaman.gif > my;chmod +x my;./my`


#### 'megaman_6' from pos x,y use W,H sized rect

`./mfetching.py -x127 -y47 -W34 -H40 ./megaman.gif > my;chmod +x my; ./my`

#### In image from 'smb2players.gif', ...

`./mfetching.py -x2 -y0 -W24 -H40 ./smb2players.gif > my;chmod +x my; ./my` -> Mario (looking left)

#### The same but with the '-m' (mirror) flag

`./mfetching.py -x2 -y0 -W24 -H40 -m ./smb2players.gif > my;chmod +x my; ./my` -> Mario (looking right)

#### u/v are like x/y coordinates but for tiles (of width / height [-W/-H] )

`./mfetching.py -u7 -v1 -y14 -x2 -W23 -H32 ./smb2players.gif > my;chmod +x my; ./my`

`./mfetching.py -u2 -v0 -x0 -y7 -W31 -H34 ./megaman.gif > my;chmod +x my; ./my`

`./mfetching.py -x6 -y159 -W36 -H34 ./smbenemies.gif > my;chmod +x my; ./my` -> Bowser (left)

`./mfetching.py -x6 -y159 -W36 -H34 -m ./smbenemies.gif > my;chmod +x my; ./my` -> Bowser (right)

`./mfetching.py -x51 -y96 -W22 -H26 ./smbenemies.gif > my;chmod +x my; ./my` -> Bloober

#### Those sprite rips are not pixel aligned! You have to adjust (the exact position) on your own.



