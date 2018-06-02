from pynput import keyboard
import webbrowser
import subprocess
import os
import sys
import time
#---------------------------------------------------------------------------------
dec1 = ["****************************************************************************",
"****************************************************************************",
"****************************************************************************",
"***                                                                      ***",
"***                                                                      ***",
"***                          HOTKEY CREATED!                             ***",
"***                                                                      ***",
"***                                                                      ***",
"***                                                                      ***",
"***                                                                      ***",
"***                                                                      ***",
"****************************************************************************",
"****************************************************************************",
"****************************************************************************"]

blank = ["****************************************************************************",
"****************************************************************************" ,
"****************************************************************************" ,
"***                                                                      ***" ,
"***                                                                      ***" ,
"***                                                                      ***" ,
"***                                                                      ***" ,
"***                                                                      ***" ,
"***                                                                      ***" ,
"***                                                                      ***" ,
"***                                                                      ***" ,
"****************************************************************************" ,
"****************************************************************************" ,
"****************************************************************************" ]

real_dec1 = ""
for i in dec1:
    real_dec1 += i + "\n"

real_blank = ""
for i in blank:
    real_blank += i + "\n"

#--------------------------------------------------------------------------------
# The currently active modifiers
current = set()
#------------------------DECORATION---------------------------------------------
def blink():
    i = 0
    while(i < 6):
        print(real_dec1)
        time.sleep(0.3)
        os.system("cls")
        print(real_blank)
        time.sleep(0.3)
        i += 1


#----------------------THE IMPORTANT FUNCTION----------------------------------

#make a method that goes back to main method
def execute(key):
    a_key = '{0} pressed'.format(key).replace("pressed", "").strip().upper()

    for k in dict:
        k = "'" + k + "'"
        k = k.strip().upper()
        if a_key == k:
            a_key = a_key.replace("'", "")
            web_or_app = dict.index(a_key)
            try:
                web_or_app = dict2[web_or_app]
            except:
                print("There is nothing assigned to this character. Edit the Hotkey and add one.")
            try:
                if web_or_app[0:2] == "W=":
                    try:
                        webbrowser.open(web_or_app[2:])
                    except:
                        print("Something went wrong. Is the website's URL correct?")
                elif web_or_app[0:2] == "A=":
                    try:
                        subprocess.call(web_or_app[2:])
                    except:
                        print("Something went wrong with the hotkey for the character " + a_key + ". Edit the hotkey or try again.")
            except:
                print("Error. Please restart program and try again, or create another hotkey.\n")
#----------------------------------------------------------------------------------
def pressed(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute(key)
#-------------------------------------------------------------------------------
def released(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

line_sep = "--------------------------------------------------------"
#--------------------------------------------------------------------------------HOTKEY--------------------------------------------------------------------------
# The key combination to check

used_chars = []
COMBINATIONS = []
dict_keys = []
dict = []
dict2 = []
COMBINATIONS_str = []


#CURRENT DIRECTORY
direct = os.getcwd()
direct = direct + "\\"
print(direct)

#Open all the files
dict_file = open(direct + "hotkeys/dict.txt", "r") #gets the combinations of key and values
dict_file2 = open(direct + "hotkeys/dict2.txt", "r")
COMBINATIONS_file = open(direct + "hotkeys/COMBINATIONS.txt", "r")
used_chars_file = open(direct + "hotkeys/used_chars.txt", "r")

#Write all the contents into the lsit
line1 = dict_file.readline()
while(line1):
    dict.append(line1.rstrip("\n").strip())
    line1 = dict_file.readline()



line12 = dict_file2.readline()
while(line12):
    #print(line12)
    dict2.append(line12.rstrip("\n").strip())
    line12 = dict_file.readline()


line2 = COMBINATIONS_file.readline()
while(line2):
    COMBINATIONS.append(eval(line2))
    COMBINATIONS_str.append(line2)
    line2 = COMBINATIONS_file.readline()

line3 = used_chars_file.readline()
while(line3):
    used_chars.append(line3.rstrip("\n"))
    line3 = used_chars_file.readline()

dict_file.close()
dict_file = open("hotkeys/dict.txt", "r")
#--------------------GET INPUT-------------------------------------------------------

def createHotkey():
    input_loop = True

    while(input_loop):
        i = input("Enter a character: ").strip().upper()
        while(len(i) != 1):
            os.system('cls')
            i = input("Please enter just one character: ").strip()
            if i == "menu":
                mainn()

        if i.lower() == "menu":
            mainn()
        if i in used_chars:
            i = input("\nThat character is already used.\nPlease enter another character: ").strip()
            os.system('cls')
            if i == "menu":
                mainn()
        else:
            with open("hotkeys/used_chars.txt", "a") as used_chars_file:
                if i.upper() not in used_chars:
                    used_chars_file.write(i.upper() + "\n")
            used_chars.append(i.upper())
            input_loop = False


    print(line_sep)
    print("Assign a choice (enter the corresponding number): \n1. Website\n2. Application\n")
    choice = input("Enter choice number here: ").strip()
    if choice == "menu":
        mainn()

    loop_cont = True
    choice_str = ""


    #Get input from the user and put it into the dictionary
    while(loop_cont):
        if choice == "1":
            web = input("Enter the website link: ").strip() #key-value the character and website
            if web == "menu":
                mainn()
            choice_str = "W=" + web
            i = i.upper()
            dict.append(i)
            dict2.append(choice_str)
            loop_cont = False
        elif choice == "2":
            app = input("Enter the application's path: ").strip() #key-value the character and application
            if app == "menu":
                mainn()
            choice_str = "A=" + app
            i = i.upper()
            dict.append(i)
            dict2.append(choice_str)
            loop_cont = False
        else:
            choice = input("Please enter a valid option: ").strip()
            if choice == "menu":
                mainn()

    with open(direct + "hotkeys/dict.txt", "a") as dict_file:
        print(dict)
        if i.upper() in dict:
            dict_file.write(i + "\n")
    with open(direct + "hotkeys/dict2.txt", "a") as dict_file2:
        if choice_str in dict2:
            dict_file2.write(choice_str + "\n")



    #APPEND HOTKEY TO COMBINATIONS
    mod = "{" + "keyboard.Key.shift"
    char = "keyboard.KeyCode(char=" + "'" + i + "'" + ")" + "}"
    char2 = "keyboard.KeyCode(char=" + "'" + i.upper() + "'" + ")" + "}"
    hotkey = mod + ", " + char
    hotkey2 = mod + ", " + char2
    with open(direct + "hotkeys/COMBINATIONS.txt", "a") as COMBINATIONS_file:
        if hotkey2 not in COMBINATIONS_str:
            COMBINATIONS_file.write(hotkey + "\n")
            COMBINATIONS_file.write(hotkey2 + "\n")
    hotkey = eval(hotkey) #Changing the string into a class to be able to be used
    hotkey2 = eval(hotkey2)
    COMBINATIONS.append(hotkey)
    COMBINATIONS.append(hotkey2)

    blink()
    #print(COMBINATIONS)

    #Make a list of keys
    #for k in dict.keys():
     #   dict_keys.append(k)

    mainn()

def startHotkey():
    with keyboard.Listener(on_press=pressed, on_release=released) as listener:
        listener.join()

def editHotkey():
    print("Your current Hotkeys: ")
    acc = 0
    while(acc < len(dict)):
        try:
            string = dict2[acc]
            if(string[0:2] == "W="):
                string = string.replace("W=", "")
            elif (string[0:2] == "A="):
                string = string.replace("A=", "")

            print(str(acc + 1) + ".", dict[acc], " = ", string)
        except:
            print()
        acc += 1

    print("\n")

    choice = int(input("Which hotkey would you like to edit? Selecting the number: "))
    if choice == "menu":
        mainn()
    new_link = input("Enter the new link: ").strip()
    new_link = "W=" + new_link
    word_copy = dict2[acc-1]
    print("BEFORE")
    dict2[acc - 1] = new_link
    print("AFTER")

    f = open("hotkeys/dict2.txt", "w+")
    line = f.readline()


    print("THIS IS DICT2 ", dict2)
    while(line):
        print(line)
        if word_copy.strip() == line.strip():
            #print(dict2.index(line.strip()))
            pass

        line = f.readline()

    f.truncate()

    for i in dict2:
        f.write(i + "\n")

    f.close()


#------------------------------------------------------------MAIN--------------------------------------------------------

def main_method():
    print("*******************************HOTKEY PROGRAM*******************************")
    print("Enter an option that corresponds to a choice")
    print("1. Create a Hotkey")
    print("2. Edit a Hotkey")
    print("3. Start the Hotkey Program\n")

    option_choice = input("Enter your choice here: ").strip()
    if option_choice == "menu":
        mainn()

    main_loop = True
    while(main_loop):
        if option_choice == "1":
            os.system('cls')
            createHotkey()
        elif option_choice == "2":
            os.system('cls')
            editHotkey()
        elif option_choice == "3":
            os.system('cls')
            startHotkey()
        else:
            option_choice = input("Please enter a valid option: ").strip()
            if option_choice == "menu":
                mainn()

def mainn():
    os.system('cls')
    main_method_cont = True
    while(main_method_cont):
        main_method()
        keep_going = input("Go back to Start Menu? Enter Y to Continue or N to Quit Program: ").strip().upper()
        if keep_going == "Y":
            main_method_cont == True
        elif keep_going == "N":
            main_method_cont = False
            sys.exit()
        else:
            keep_going = input("Please enter a valid option: ").strip().upper()

print(used_chars)
print(dict)
print(dict2)
print(COMBINATIONS)

mainn()

COMBINATIONS_file.close()
used_chars_file.close()
dict_file.close()


