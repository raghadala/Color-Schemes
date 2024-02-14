#120 Final Project
#Divya Kapoor D200 (301462659) Raghad Alabdalla D200(301468593)
#April 1, 2022

#importing modules
coloursdict = {}
import cmpt120colours
import cmpt120image

#hexadecimal conversion function
def hexa_conversion(r,g,b):
  rval = int(r)
  bval = int(b)
  gval = int(g)

  rhex = hex(rval).replace("0x","").upper()
  bhex = hex(bval).replace("0x","").upper()
  ghex = hex(gval).replace("0x","").upper()

  if len(rhex) == 1:
    rhex = "0" + rhex
  if len(bhex) == 1:
    bhex = "0" + bhex
  if len(ghex) == 1:
    ghex = "0" + ghex
  rgbhex = ("#"+rhex+ghex+bhex)
  return rgbhex

#creating tuples function
def tuples(r,g,b):
  rint = int(r)
  bint = int(b)
  gint = int(g)
  key = (rint,gint,bint)
  return key 

#dictionary function
def dictionary(key,value):
  dict = value
  coloursdict[key]=dict
  return coloursdict

#PART 1
#OPTION 1
#processing file function
def processingFile(file):
  for line in file:
    data = line.strip("\n").split(",")
    colourname = data[0].capitalize()
    r = data[1]
    g = data[2]
    b = data[3]
    rgbhex = hexa_conversion(r,g,b)
    colourkey = tuples(r,g,b)
    colourhex = [colourname, rgbhex]
    colourdict = dictionary(colourkey,colourhex)
  return colourdict

#OPTION 2
#function to print all dictionary content
def printdict():
    for i in range(len(coloursdict)):
      colourkeys = list(coloursdict.keys())
      red = colourkeys[i][0]
      green = colourkeys[i][1]
      blue = colourkeys[i][2]
      colourvalue = list(coloursdict.values())
      names = colourvalue[i][0]
      hexes = colourvalue[i][1]
      print("{:<7}".format(names) + "{:>10}".format(red) + \
            "{:>10}".format(green) + "{:>10}".format(blue)+ 
            "{:>10}".format(hexes))
#OPTION 3
#function to check if user input in dictionary
#if not, allow them to input it
def indictionary(usercolor):
  if usercolor in coloursdict.keys():
      print("Colour",usercolor,"is",coloursdict[usercolor]\
            [0],"and has the hex code",coloursdict[usercolor][1])
  else:
      print("Colour",usercolor,"has not been found. Enter your choice: ")
      print("1. Enter a name for this colour")
      print("2. Return to the main menu")
      userchoice = int(input("Enter Your Choice: "))
      if userchoice == 1:
        newcolour = str(input("What is the colour's name? "))
        newcolhex = cmpt120colours.hexa_conversion(usercolor[0], usercolor[1], usercolor[2])
        coloursdict[usercolor]=[newcolour,newcolhex]
        print("Colour",usercolor,"is",newcolour,"and has the hex code", newcolhex)
      else:
        print("")
        
#OPTION 4
#function to find closest color to user input
def closestcolor(usercolor):
  if usercolor in coloursdict:
    print("Colour",usercolor,"is",coloursdict[usercolor][0],\
          "and has the hex code",coloursdict[usercolor][1])
  else:
    absolutevalue(usercolor)

#calculating absolute value to get difference
def absolutevalue(usercolor):
  sum = 255*3     
  lowest = ()
  for key in coloursdict:
    diffsum = abs(usercolor[0]-key[0])+ abs(usercolor[1]-key[1]) + abs(usercolor[2]-key[2])
    if diffsum < sum:
      sum = diffsum
      lowest = key
      closestcolhex = cmpt120colours.hexa_conversion(lowest[0],lowest[1],lowest[2])
  print("The closest color to [",(usercolor), "] is [",(lowest),\
        "]",(coloursdict[lowest][0]),"with hex code",closestcolhex)
  print("The absolute difference between the two colours is",sum,".")

#MONOCHROME OPTION
#monochrome function
def monochrome(usercolor,width,height):
  img = [[[usercolor[0],usercolor[1],usercolor[2]]\
          for i in range(width)] for j in range(height)]
#top left corner(lightest)
  for row in range(80):
    for col in range(80):
      img[row][col] = [usercolor[0]+(255-usercolor[0])*0.8,usercolor[1]\
                       +(255-usercolor[1])*0.8,usercolor[2]+(255-usercolor[2])*0.8]

#top right corner (slightly lighter)
  for row in range(80):
    for col in range(160,240):
      img[row][col] = [usercolor[0]+(255-usercolor[0])*0.5,usercolor[1]\
                       +(255-usercolor[1])*0.5,usercolor[2]+(255-usercolor[2])*0.5]

#bottom right corner(darkest)
  for row in range(160,240):
    for col in range(80):
      img[row][col] = [usercolor[0]*0.5,usercolor[1]*0.5,usercolor[2]*0.5]

#bottom left corner(slightly darker)
  for row in range(160,240):
    for col in range(160,240):
      img[row][col] = [usercolor[0]*0.8,usercolor[1]*0.8,usercolor[2]*0.8]
  cmpt120image.showImage(img)
  cmpt120image.saveImage(img,"Monochrome.png")

#COMPLIMENTARY OPTION
#finding complimentary color function
def findcomp(usercolor):
  redd = 255-usercolor[0]
  greenn = 255-usercolor[1]
  bluee = 255-usercolor[2]
  compcolours = [redd,greenn,bluee]
  return compcolours

#complimentary color function
def complimentary(usercolor, width, height):
  img = [[[usercolor[0],usercolor[1],usercolor[2]] for \
          i in range(width)] for j in range(height)]

#top left corner(lightest)
  for row in range(80):
    for col in range(80):
      img[row][col] = [usercolor[0]+(255-usercolor[0])*0.8,usercolor[1]\
                       +(255-usercolor[1])*0.8,usercolor[2]+(255-usercolor[2])*0.8]
      
#top right corner (slightly lighter)
  for row in range(80):
    for col in range(160,240):
      img[row][col] = [usercolor[0]+(255-usercolor[0])*0.5,usercolor[1]\
                       +(255-usercolor[1])*0.5,usercolor[2]+(255-usercolor[2])*0.5]

#bottom right corner(slightly darker)
  for row in range(160,240):
    for col in range(80):
      img[row][col] = [usercolor[0]*0.5,usercolor[1]*0.5,usercolor[2]*0.5]

#bottom left corner(darkest)
  for row in range(160,240):
    for col in range(160,240):
      img[row][col] = [usercolor[0]*0.8,usercolor[1]*0.8,usercolor[2]*0.8]
      
#COMPLIMENTARY COLOR SCHEME
  compcolours = findcomp(usercolor)
  for row in range(240):
    for col in range(240,480):
      img[row][col]= compcolours
      
#complimentary top left corner(lightest)
  for row in range(80):
    for col in range(240,320):
      img[row][col] = [compcolours[0]+(255-compcolours[0])*0.8,compcolours[1]\
                       +(255-compcolours[1])*0.8,compcolours[2]+(255-compcolours[2])*0.8]

#complimentary top right corner (slightly lighter)
  for row in range(80):
    for col in range(400,480):
      img[row][col] = [compcolours[0]+(255-compcolours[0])*0.5,compcolours[1]\
                       +(255-compcolours[1])*0.5,compcolours[2]+(255-compcolours[2])*0.5]

#complimentary bottom right corner(slightly darker)
  for row in range(160,240):
    for col in range(240,320):
      img[row][col] = [compcolours[0]*0.5,compcolours[1]*0.5,compcolours[2]*0.5]

#complimentary bottom left corner(darkest)
  for row in range(160,240):
    for col in range(400,480):
      img[row][col] = [compcolours[0]*0.8,compcolours[1]*0.8,compcolours[2]*0.8]
  cmpt120image.showImage(img)
  cmpt120image.saveImage(img, "Complimentary.png")
