from tkinter import Tk

run = True
print("Enter decoration string:")
decorString = input()

# main cycle
while run:
    print("Enter string to process:")
    myStroke = input()
    if myStroke == "stop":
        run = False
    elif myStroke == "change":
        print("Enter decoration string:")
        decorString = input()
        continue
    newString = decorString+myStroke.upper()+decorString

    # copy to clipboadr
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(newString)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()
    
    print(newString)
    print("type 'stop' to stop, type 'change' to change decoration string")

print ("STOPPED")
input()