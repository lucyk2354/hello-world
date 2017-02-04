import random
import tkinter

alist = []
estring = ''
tcheck = True
x = ''

def ans():
    while tcheck == True:
        print("What's your question?")
        q = input("")
        if q[len(q) - 1] == '?':
            #rand = random.randint(0, len(alist) - 1)
            print(random.choice(alist))

        else:
            print(estring)

        print("")
        print("")
        print("")
        print("")


print('Welcome to my magic 8 ball!')
print('Current options:')
print("1- Write your own 8-ball")
print("2- Use preset 8-balls")
mode = input("What nember item would you like to use?  ")
            
if mode == '1':
    alist = []
    print('')
    print("Type in 'done' when you have no more answers to add.")
    while not x == 'done':
        x = input(' - ')
        if not x == 'done':
            alist.append(x)
    estring = "That's not a question."
    print('')
    print('Would you like to run your 8-ball in a new window or by command line?')
    gui = input("Type 'new' or 'command'.  ")
    if gui == 'command':
        ans()

    ## Tkinter code!!
    elif gui == 'new':
        root = tkinter.Tk()
        root.title("Magic 8 ball")
        root.geometry("800x400")
        def runmain():
            Label1.configure(text=random.choice(alist))

        Button1 = tkinter.Button(text="Ask", command=runmain)
        Button1.pack()

        Label1 = tkinter.Label(root, text="Welcome to the magic 8 ball!", font=('Fixedsys', 20))
        Label1.pack()

        root.mainloop()

    
elif mode == '2':
    m2 = input("Would you like to speak to the normal ball or the sassy one? (type 'normal' or 'sassy'.)  ")
    
    if m2 == 'normal':
        alist = ['Yes.', 'No.', 'Ask again later.', 'Probably.', 'I doubt it.', 'Purple!', 'The future is cloudy...', 'It has yet to be determined...', 'Sheep. Sheeeep.']
        estring = "I'm sorry, I can't answer that."

    elif m2 == 'sassy':
        alist = ["Don't know, don't care.", "Yes... no... maybe so...", "Talk to the hand cause the screen don't care!", "I don't know, go ask the wedgie- uh, ouija board!", "Oh sorry, were you talking? I wasn't paying attention.", "Whatever.", "Why're you asking me?", "Eh... who cares?", "And the answer is... you're a butthead.", "Go away.", "pthbththpth"]
        estring = "That's not even a question! What do you expect of me?"

    else:
        tcheck = False

    ans()


if not gui == 'new':
    print("Invalid input.")
