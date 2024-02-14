#120 Final Project
#Divya Kapoor D200 (301462659) Raghad Alabdalla D200(301468593)
#April 1, 2022

#importing modules
import cmpt120colours
coloursdict={}
loop = True

#create while loop to interate through the user's inputs
while loop is True:
  #menu options
  print('''Welcome to Colour Schemes!
--------------------------''')
  print('''
1. Load Colour File
2. Print All Colours
3. Select Colour
4. Find Closest Colour
5. Display (Save) Colour Scheme
0. Quit''')
  
  userchoice = int(input("Enter Your Choice 0/1/2/3/4/5--> "))
#--------------- PART 1 ---------------
#processing file if user chooses 1
  if userchoice == 1:
    print("Loading colour file...")
    file = open("colours.csv")
    coloursdict = cmpt120colours.processingFile(file)
    print("The file has been processed and",len(coloursdict), \
          "colours were entered into the dictionary")

#printing file if user chooses 2
  elif userchoice == 2:
    print()
    colorhead = "{:<7}".format("Colour Names ")
    rhead = "{:>5}".format("Red")
    ghead = "{:>8}".format("Green")
    bhead = "{:>8}".format("Blue")
    hhead = "{:>8}".format("Hex")
    header = colorhead+rhead+ghead+bhead+hhead
    print(header)
    print("-"*len(colorhead),"-"*len(rhead),
          "-"*len(ghead),"-"*len(bhead), "-"*len(hhead))
    cmpt120colours.printdict()
      
#------------------------ PART 2 --------------------------
#seeing if color exists in file if user chooses 3
  elif userchoice == 3:
    ("Enter the RGB values of your colour.")
    userred = int(input("R: "))
    usergreen = int(input("G: "))
    userblue = int(input("B: "))
    usercolor = (userred,usergreen,userblue)
    cmpt120colours.indictionary(usercolor)
  
#--------------------- PART 3 ------------------------
#finding closest colour if user chooses 4
  elif userchoice == 4:
    print("Enter the RGB values of your colour.")
    userred = int(input("R: "))
    usergreen = int(input("G: "))
    userblue = int(input("B: "))
    usercolor = (userred,usergreen,userblue)
    cmpt120colours.closestcolor(usercolor)

#--------------------- PART 4 ----------------------------- #displaying monochromatic or complimentary colors depending on user input 
  elif userchoice == 5:
    print("Enter the RGB values of your base colour.")
    userred = int(input("R: "))
    usergreen = int(input("G: "))
    userblue = int(input("B: "))
    usercolor = (userred,usergreen,userblue)
    print('''Which colour scheme do you wish to display?
M: Monochrome
C: Complementary''')
    scheme = input("Select an option: ").upper()
    if scheme == "M":
      cmpt120colours.monochrome(usercolor,240,240)
    elif scheme == "C":
      cmpt120colours.complimentary(usercolor,480,240)

#ending loop
  elif userchoice == 0:
    print("Bye!")
    loop = False

#giving user another chance
  else:
    print("Sorry please try again! ")
    print("")
