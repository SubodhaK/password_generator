'''
Exploring the Logic of the Password Generator 

1. Choose Your Preferences:
   - The script lets you decide the length of your password.
   - You can include uppercase letters, lowercase letters, numbers, and symbols in your password.

2. Mix and Match:
   - The script then generates a password by mixing these character types based on your preferences.
   - For example, if you choose a length of 12 characters, it divides the characters into four groups of equal length (capital letters, simple letters, numbers, symbols) if possible. Any remainder characters are distributed evenly among these groups.

3. Shuffling for Randomness:
   - The script shuffles the characters within each group to ensure randomness.
   - This step enhances the security of your password.

4. Assembling Your Password:
   - Finally, the script assembles the characters from each group to create your secure password.
   - The characters are arranged in a random order to further enhance security.

5. Saving Your Password:
   - You have the option to save your generated password to a text file.
   - This way, you can easily access your password later.

Try it out yourself and take control of your online security!
'''

# Your actual code starts here

import random as rm

print("")
print("###   GET_YOUR_PASSWORD_NOW!   ###")
print("")

# that section for ony first round other rounds in the loop
need = input("do you wont a password ? \"yes\" Or \"no\" -  ")
if need == "yes":
    name = input("plese give a name for your password - ")
else:
    print("okay, let's start again!")

TIME = 1  # time take for count how many round going that loop.


while need == "yes":
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    simple_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    natural_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ['!', '@', '#', '$', '%','&', '*']

    password_list = []
    length = int(input("how many charactors do you wont ? "))
    len_of_one = length/4
    mode_value = length%4
    pw_length = int(len_of_one)

    while pw_length > 0:
        a = rm.choice(capital_letters)
        b = rm.choice(simple_letters)
        c = rm.choice(natural_numbers)
        d = rm.choice(symbols)
        pw_length -= 1
        password_list.append(a)
        password_list.append(b)
        password_list.append(c)
        password_list.append(d)

    if mode_value == 3 :
        a = rm.choice(capital_letters)
        b = rm.choice(simple_letters)
        c = rm.choice(natural_numbers)
        password_list.append(a)
        password_list.append(b)
        password_list.append(c)
    
    elif mode_value == 2 :
        a = rm.choice(capital_letters)
        b = rm.choice(simple_letters)
        password_list.append(a)
        password_list.append(b)
    
    else:
        a = rm.choice(capital_letters)
        password_list.append(a)

    rm.shuffle(password_list)
    ELEMENT_COUNT = len(password_list)
    ELEMENT = 0
    PW_LEN = 0
    PASSWORD = ""

    while PW_LEN < ELEMENT_COUNT :
        PASSWORD += password_list[ELEMENT]
        ELEMENT+= 1
        PW_LEN += 1
    print("")
    print("--------------------------------------------------")
    print("This Is Your " + str(name) + " Password - ", str(PASSWORD))
    print("--------------------------------------------------")
    print("")
    SAVE = str(input("Do You wont save that Password ? \"yes\" Or \"no\" -  "))
    
    if SAVE == "yes" and TIME == 1:

        PATH_INPUT = str(input("plese input path you wont (don't use last slash(\) mark) -  "))
        FILE_NAME = str(input("file name please -  "))
        FULL_PATH = str(PATH_INPUT) + "\\" + str(FILE_NAME)+".txt"
        PATH = "{}".format(FULL_PATH,)
        file = open(PATH, 'x')
        file = open(PATH, 'w')
        file.write(str(name) + " - " + PASSWORD )
        file.close()
        TIME += 1
       print("")
       print("your password was saved.")
       print("###################################")
       print("")
    
    elif SAVE == "yes" and TIME > 1:
        file = open(PATH,"a")
        file.write("\n" + str(name)+" - "+str(PASSWORD))
        file.close()
        print("")
        print("your password was saved.")
        print("###################################")
        print("")
    need = input("Do You Wont Another ? \"yes\" Or \"no\" - ")
    
    if need == "yes":
        name = input("plese give a name for your password - ")
    print("")
    

print("BEST OF LUCK")
print("###################################")
print("")
