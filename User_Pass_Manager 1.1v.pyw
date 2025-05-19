"""
                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                +                                                                                                            +
                +                                                                                                            +
                +   Author  :    PRINCE OFORI                                                                                +
                +   Program :    User-Pass_Manager                                                                           +
                +   Version :    1.1v                                                                                        +
                +   About   :    Generates usernames and passwords and writes the output to a text file                      +
                +   Date and Time Created :    July 2, 2019    10:46:34:02 AM				                     +
                +   Target System :  Windows, Mac OS X, GNU/Linux					                     +               
                +   Maintainer :  princeofori3050@gmail.com                                                                  +
                +                                                                                                            +
                +                                                                                                            +
                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""



#1. Import all modules
from tkinter import *
from tkinter import messagebox
import random


#2. Create the main window application 
win = Tk()
win.title("User_Pass_Manager 1.1v")       
win.geometry("700x400")
win.resizable(0,0) 



#9. Create a Button callback function
def butt_call():
    global screen1
    global tpl_fname_entry
    global tpl_lname_entry
    global entry_box_1
    global entry_box_2

    

    #11. Create 2 variables to hold the user's inputs
    fname_entered = firstname_entry.get().title()
    lname_entered = lastname_entry.get().title()


    if messagebox.askyesno("Name verification","Is there any name error?") == True:
         firstname_entry.delete(0, END)
         lastname_entry.delete(0, END)
         firstname_entry.focus()
    else:
        #16. Create all 4 variables needed
        numbers = "0123456789"
        sp = "~!@#$*()_+{}|:<>?/;\]%^&[="
        letters1 = "MNBVCXZLKJHGFDSAQWERTYUIP"
        letters2 = "zxcvbnmlkjhgfdsaqwertyuiop"
        
        #17. Generate a random choice(using random module) of 7 lower,upper,integers, and special characters from step 16
        L1 = random.choice(letters1)
        L2 = random.choice(letters1)
        L3 = random.choice(letters1)
        L4 = random.choice(letters1)
        L5 = random.choice(letters1)
        L6 = random.choice(letters1)
        L7 = random.choice(letters1)

        l1 = random.choice(letters2)
        l2 = random.choice(letters2)
        l3 = random.choice(letters2)
        l4 = random.choice(letters2)
        l5 = random.choice(letters2)
        l6 = random.choice(letters2)
        l7 = random.choice(letters2)

        N1 = random.choice(numbers)
        N2 = random.choice(numbers)
        N3 = random.choice(numbers)
        N4 = random.choice(numbers)
        N5 = random.choice(numbers)
        N6 = random.choice(numbers)
        N7 = random.choice(numbers)

        sp1 = random.choice(sp)
        sp2 = random.choice(sp)
        sp3 = random.choice(sp)
        sp4 = random.choice(sp)
        sp5 = random.choice(sp)
        sp6 = random.choice(sp)
        sp7 = random.choice(sp)


        #18. Generate a random choice of 4 integers
        n1 = random.choice(numbers)
        n2 = random.choice(numbers)
        n3 = random.choice(numbers)
        n4 = random.choice(numbers)


        #19. Create a variable called user_code to stored all the 4 generated random choice of integers from step 18
        user_code = n1+n2+n3+n4


        #20. Create a variable called password to hold a maximum of 50 all the random choice of 7 lower,upper,integers, and special characters, and shuffle
        password = sp1+L1+l2+L3+L4+l5+l6+sp2+l7+sp3+L5+N4+L6+N2+L7+l1+l3+l4+N7+l5+l6+sp2+l7+sp3+sp6+sp7+N1+N3+sp5+L2+N5+N6+sp4+L5+L6+N2+L7+l1+l3+l4+N7+sp6+sp7+N3+sp5+sp1+L1+L3+L4+l5


        #21. Create a variable called username_info to hold the (firstname [indexed].title(), + lastname.lower() + user_code)
        username_info = fname_entered[0].title() + lname_entered[:5].lower() + user_code


        #22. Write the final informations into a text file
        file = open(username_info+".txt", "w")
        file.write("\nYour username is:   ")
        file.write(username_info)
        file.write("\n\nAnd your password is:   ")
        file.write(password)
        file.close()

            
        #23. Print a successful message to the user and clear all entry fields
        info = messagebox.showinfo("CONGRATULATIONS !!!","\t\tCongratulations,\nYour username and password has been processed to a text file successfully !!!")
        firstname_entry.delete(0, END)
        lastname_entry.delete(0, END)
        firstname_entry.focus()


#3. Create the intro label
intro_label = Label (win, text = "Drop The Hustle ! \n Let User_Pass_Manager create your Username and Password under seconds.", \
                     font = ("Arial", 15), bg = "turquoise", relief = "groove", width = "700", height = "3", bd = "5").pack()


#4. Create a prompt
prompt = Label (win, text = "Please enter your details below:", font = ("Arial", 12)).place(x = 15, y = 120)


#5. Create the first and lastname labels
firstname_label = Label (win, text = "Firstname : ", font = ("Arial", 12)).place(x = 40 , y = 170)
lastname_label = Label (win, text = "Lastname : ", font = ("Arial", 12)).place (x = 40 , y = 230 )


#6. Assign the firstname and lastname entries to StringVar()
firstname = StringVar()
lastname = StringVar()


#7. Create the first and lastname entries and set the cursor focus into the fisrt entry
firstname_entry = Entry (win, width = 30, textvariable = firstname, font = ("Arial", 12))
firstname_entry.place(x = 150, y = 170)
firstname_entry.focus()

lastname_entry = Entry (win, width = 30, textvariable = lastname, font = ("Arial", 12))
lastname_entry.place(x = 150, y = 230)


#8. Create the Proceed Button
button = Button(win, text = "Proceed", font = ("Arial", 10), bg = "yellow", width = "12", command = butt_call).place(x = 550, y = 300)



win.mainloop()
