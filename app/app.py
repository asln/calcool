'''
As of now, the only topic that is supplied and tested is Trigonometry.

We do not own any of the images used.

Nov 2014, Ally Kan
'''



### The code begins here ###



from Tkinter import *
import tkMessageBox
import Pmw
from PIL import Image, ImageTk


def Main():


# this try and except is for the purpose of reusing the Main function:
# This function can be called by both the Landing page and the Lesson window
# And so to prevent TclError from occuring (in case called from the Lesson window
# where landing has already long been destroyed), this condition is used.

    try:
        landing.destroy()
    except TclError:
        pass
    main = Tk()
    main.title("CalCool")
    main.geometry("730x385")
    #main.config(bg='royal blue')



#-------------------------
# begin the lesson windows
#-------------------------


    def lessonWindow1(event):
        
        print "test1"


    def lessonWindow2(event):
            
        try:
            main.destroy()
        except TclError:
            pass
        root = Tk()
        root.title("CalCool")
        
            
        def goToMain():  # go back to Main page
            root.destroy()
            Main()

        def goToPlayground2():
            root.destroy()
            playground2(None)
            
        def selectionText(fileName):  # open different files for different topics from the list
            with open(fileName,'r') as f: #importtext
                displayedText = f.read()
            msgBox = Message(root, text=displayedText, bg='royalblue', fg='ivory', relief='groove', width=400, anchor=NW)
            msgBox.grid(row=0, column=2, rowspan=2, columnspan=40, padx=5, pady=5, sticky=NSEW)
                

        def selectionCommand():

            # when an item from the ScrolledListbox widget is selected,
            # this function is called to display different text files
            
            sel = box.curselection()
            if sel[0] == 0:
                selectionText("trig1.txt")

            elif sel[0] == 1:
                img2 = Image.open("trig2.png") # open img file
                trig2 = ImageTk.PhotoImage(img2)
                img = Label(root, image=trig2, width=400, justify=CENTER, bg='royalblue', relief='groove')
                img.image = trig2
                img.grid(row=0, column=2, rowspan=2, columnspan=40, padx=5, pady=5, sticky=NSEW)

            elif sel[0] == 2:
                selectionText("trig2.txt")

            elif sel[0] == 3:
                img3= Image.open("trig3pic.gif")
                trig3 = ImageTk.PhotoImage(img3)
                img = Label(root, image=trig3, width=400, justify=CENTER, bg='royalblue', relief='groove')
                img.image = trig3
                img.grid(row=0, column=2, rowspan=2, columnspan=40, padx=5, pady=5, sticky=NSEW)


            elif sel[0] == 4:
                selectionText("trig4.txt")
                
            elif sel[0] == 5:
                selectionText("trig5.txt")
                
            elif sel[0] == 6:
                selectionText("trig6.txt")
                

        with open("trig1.txt",'r') as f: #importtext
            introText = f.read()

        # ScrolledListBox widget from Pmw module
 
        items=('Introduction', 'A Triangle', 'A Triangle (Cont.)', 'Soh Cah Toa', 'Sine Rule', 'Cosine Rule', 'Finding Area')
        box = Pmw.ScrolledListBox(root,listbox_selectmode=SINGLE, 
            items=(items), label_text='Trigonometry', labelpos=NW,
            selectioncommand=selectionCommand)
        box.grid(sticky=W, row=0, column=0, padx=5, pady=5)


        #this area displays the main content

        msgBox = Message(root, text=introText, bg='royalblue', fg='ivory', relief=GROOVE, width=400, anchor=NW)
        msgBox.grid(row=0, column=2, rowspan=2, columnspan=40, padx=5, pady=5, sticky=NSEW)


        # this infoBox is for highlighted information
        
        infoBox = Message(root, text=
            "It is important when solving trig problems that you determine first whether the given\n"
            "triangle is a right angle triangle. Keep in mind that Soh Cah Toa only works with right triangles.",
            bg='firebrick1', fg='ivory', relief=GROOVE, width=500, anchor=NW)
        infoBox.grid(row=2, column=0,rowspan=1, columnspan=42, padx=5, pady=1, sticky=NSEW)

        Button(root, text="Main Menu", command=goToMain).grid(row=5, column=0, rowspan=10, sticky=SW, padx=5, pady=5)
        #Button(root, text="Calculator", command=None).grid(row=5, column=39, rowspan=10, sticky=SE, padx=0, pady=5)
        Button(root, text="Playground", command=goToPlayground2).grid(row=5, column=40, rowspan=10, sticky=SE, padx=0, pady=5)

        root.mainloop()


    def lessonWindow3(event):
        print "test3"


    def playground1(event):
        print "playground1"

    def playground2(event):  # Playground area for Trigonometry
        try:
            main.destroy()
        except TclError:
            pass


        def playgroundProb2():  # Page 2 of Playground Trigonometry
            
            def goMainFromPlayground2():   # Command that will allow user to go back to Main Page from Page 2 of Playground
                playgroundProb2.destroy()
                Main()

            def goLearnFromPlayground2():   # Command that will allow user to return to the lesson window from Page 2 of Playground
                playgroundProb2.destroy()
                lessonWindow2(None)

            def check2():  # Command for checking the answer for the 2nd problem
                if question2Entry.get() == str(77):
                    tkMessageBox.showinfo('Correct!', "Congratulations, you've mastered this unit!")
                    playgroundProb2.destroy()
                    Main()
                else:
                    tkMessageBox.showinfo('Incorrect', "Oh no you didn't get it right! Try again, okay?")

            def hint2():  # hint for the 2nd question
                tkMessageBox.showinfo('Hint', "Hint: What do you do when you're given an angle and its adjacent side, and you want to find the opposite side?")

            ## Code for Page 2
            playgroundProb2 = Tk()
            playgroundProb2.title("CalCool")
            playgroundProb2.geometry("720x360")
        

            trigproblem2 = Image.open("trigproblem2.jpg")
            prob2 = ImageTk.PhotoImage(trigproblem2)

            prob2pic = Label(playgroundProb2, image=prob2)
            prob2pic.image = prob2
            prob2pic.grid(row=1, padx=10, pady=5, columnspan=3)
            Button(playgroundProb2, text="Learn", command=goLearnFromPlayground2).place(x=560,y=3)
            Button(playgroundProb2, text="Main Menu", command=goMainFromPlayground2).place(x=622,y=3)
            question2 = Message(playgroundProb2, text="How far is the rescue boat from the base of the lighthouse? *Round to whole number and ignore unit when entering answer.",
                bg="SeaGreen1", fg="midnight blue",
                font=("Sans Serif",13), relief='groove', width=455, anchor=NW)
            question2.grid(row=2, rowspan=2, padx=10, pady=1, sticky=NSEW)
            question2Entry = Entry(playgroundProb2, justify=CENTER)
            question2Entry.grid(row=2, column=1, rowspan=2, pady=1, padx=0, sticky=NSEW)
            Button(playgroundProb2, text="Next", command=check2).grid(row=2, column=2, padx=5, sticky=SW)
            Button(playgroundProb2, text="Hint", command=hint2).grid(row=3, column=2, padx=5, sticky=NW)

        ## Exact same thing as Page 2 but this is the 1st page
        def goMainFromPlayground1():
            playgroundProb1.destroy()
            Main()

        def goLearnFromPlayground1():
            playgroundProb1.destroy()
            lessonWindow2(None)

        def check1():
            if question1Entry.get() == str(74):
                tkMessageBox.showinfo('Correct!', "Good job, Buddy!")
                playgroundProb1.destroy()
                playgroundProb2()
            else:
                tkMessageBox.showinfo('Incorrect', "Oh no you didn't get it right! Try again, okay?")

        def hint1():
            tkMessageBox.showinfo('Hint', "Hint: Try using the Sine Rule.")


        playgroundProb1 = Tk()
        playgroundProb1.title("CalCool")
        playgroundProb1.geometry("720x360")
        

        trigproblem1 = Image.open("trigproblem1.jpg")
        prob1 = ImageTk.PhotoImage(trigproblem1)

        prob1pic = Label(playgroundProb1, image=prob1)
        prob1pic.image = prob1
        prob1pic.grid(row=1, padx=10, pady=5, columnspan=3)
        Button(playgroundProb1, text="Learn", command=goLearnFromPlayground1).place(x=560,y=3)
        Button(playgroundProb1, text="Main Menu", command=goMainFromPlayground1).place(x=622,y=3)
        question1 = Message(playgroundProb1, text="Here's your first challenge: can you figure out how far apart the 2 ships are in feet? *Round to whole number and ignore unit when entering answer.",
            bg="SeaGreen1", fg="midnight blue",
            font=("Sans Serif",13), relief='groove', width=455, anchor=NW)
        question1.grid(row=2, rowspan=2, padx=10, pady=1, sticky=NSEW)
        question1Entry = Entry(playgroundProb1, justify=CENTER)
        question1Entry.grid(row=2, column=1, rowspan=2, pady=1, padx=0, sticky=NSEW)
        Button(playgroundProb1, text="Next", command=check1).grid(row=2, column=2, padx=5, sticky=SW)
        Button(playgroundProb1, text="Hint", command=hint1).grid(row=3, column=2, padx=5, sticky=NW)



    def playground3(event):
        print "playground3"

        



#-------------------------------------------
#end the lesson window and back to main page
#-------------------------------------------




    # importing all the images

    img1 = Image.open("img1.jpeg")
    photo1= ImageTk.PhotoImage(img1)

    img2 = Image.open("img2.jpeg")
    photo2 = ImageTk.PhotoImage(img2)

    img3 = Image.open("img3.png")
    photo3 = ImageTk.PhotoImage(img3)

    photo = [photo1, photo2, photo3]

    ## end importing + creating tuple to use in the For loop


    blankLine=Label(main, text="Choose Your Topic", font=("Sans Serif",24),
                    height=1, bg='royal blue', fg='ivory')
    blankLine.grid(row=0,column=0, columnspan=3, pady=20, sticky=NSEW)



# This loop is to tidy up the whole process of placing pictures and lesson menus

    topics = ["Set Theory", "Trigonemetry", "Quadratics"]
    command = [lessonWindow1, lessonWindow2, lessonWindow3]
    command2 = [playground1, playground2, playground3]

    col = 0
    i = 0

    for col in range(3):
        topic = Label(main, text=topics[i], justify=CENTER)
        topic.grid(row=1, column=col, padx=20, pady=2)
        
        img = Label(main, image=photo[i], justify=CENTER)
        img.grid(row=2, column=col, padx=20, pady=2)

        learn = Message(main, text="LEARN",
            bg="SeaGreen1", fg="midnight blue",
            font=("Sans Serif",13), relief=RAISED,
            width=200, cursor="hand2")
        learn.bind('<Button-1>', command[i])
        learn.grid(row=3, column=col, padx=20, pady=1, sticky=NSEW)

        playground = Message(main, text="PLAYGROUND",
                bg="gold", fg="midnight blue",
                font=("Sans Serif",13), relief=RAISED,
                width=200, cursor="hand2")
        playground.bind('<Button-1>', command2[i])
        playground.grid(row=4, column=col, padx=20, pady=1, sticky=NSEW)

        
        i += 1


    #page = Message(main, text="Page", highlightbackground="royal blue", bg="white", fg="royal blue")
    #page.grid(row=5, column=2, padx=20, pady=10)
    #pageButton = Message(main, text="1",
                #bg="royal blue", fg="ivory", relief=GROOVE)
    #pageButton.grid(row=5, column=2, padx=20, pady=10)
    #pageButton2 = Message(main, text="2",
                #bg="royal blue", fg="ivory", relief=GROOVE)
    #pageButton2.grid(row=5, column=2, padx=20, pady=10, sticky=E)


    main.mainloop()


#------------------------------
# start landing page (1st page)
#------------------------------



landing = Tk()
landing.title("CalCool")
landing.geometry("400x400")
landing.configure(bg = "firebrick1")

#import img to use as a button
goButton = Image.open("gobutton.png")
goIcon = ImageTk.PhotoImage(goButton)

blankLine=Label(landing, text="", bg="firebrick1").pack(pady=8)

title=Label(landing, text="CalCool", font=("Sans Serif", 50), justify=CENTER)
title['bg'] = "firebrick1"
title['fg'] = "light cyan"
title.pack()

subtitle = Label(landing, text="Survive high school math like a cool dude.",
                font=("Sans Serif", 13), justify=CENTER)
subtitle['bg'] = "firebrick1"
subtitle['fg'] = "azure"
subtitle.pack()

go = Button(landing, image = goIcon, bg = "firebrick1",
            borderwidth = 0, justify = CENTER, command=Main)
go.pack(padx = 0, pady = 45)

landing.mainloop()
