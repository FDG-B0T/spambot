############################################
#
#               SpamBot
#             By: FDG_B0T
#
# Support:
# Discord- FDG_B0T#2348
# GitHub- https://github.com/FDG-B0T 
#
############################################


from keyboard import press
from time import sleep
import pyautogui, os

def end(): #Exit function with a message
    print('\nThanks for using this tool\nif you have any issues, contact me on GitHub')
    exit(0)

def main(): #main function
    os.system('cls')
    print('''
   _____                       ____        _   
  / ____|                     |  _ \      | |  
 | (___  _ __   __ _ _ __ ___ | |_) | ___ | |_ 
  \___ \| '_ \ / _` | '_ ` _ \|  _ < / _ \| __|
  ____) | |_) | (_| | | | | | | |_) | (_) | |_ 
 |_____/| .__/ \__,_|_| |_| |_|____/ \___/ \__|
        | |                                    
        |_|                                    
    \nThis is a very simple spam bot.
Instructions: Just type your spam text and number of time to spam, hit enter and point your cursor to the input box, the spam will begin in 10 seconds.

NOTE: THIS TOOL CAN CAUSE A CHAOS IF NOT USED IN THE RIGHT WAY. IN SIMPLE WORDS IT WILL SPAM ANYWHERE YOUR CURSOR IS AT, SO MAKE SURE YOUR CURSOR IS IN THE RIGHT INPUT BOX

Support:
GitHub - https://github.com/FDG-B0T
''')#Tool banner with instructions and contact info

    spam = input("Enter your spam text:\n-> ") #Gets the input from the user and stores it as the spam text 
    num = input("\nNumber of times to spam (Leave it if you want it to spam forever):\n-> ") #sets number of time to spam
    if num == "": #if num is blank sets num to 999999... you won't let this loop that many times would you ?
        num = 999999
    delay = float(input("\nEnter spam delay (For miliseconds use '.'):\n-> "))#sets delay to time given in the input

    print('\nThe spam will begin in 5 seconds\n')#prepare
    print("Return to this window and press 'ctrl/cmd + c' to stop the spam anytime\n\n")#how to stop the chaos
    sleep(5)#gives time for lazy users to point towards the input box

    for _ in range(int(num)):
        sleep(delay)#stop the spam for dealy time given in 'delay' variable every loop
        pyautogui.typewrite(spam) #types the spam text in the input box
        press('enter') # hits enter
    
    end()#calls the end function

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping the script')
        end()


