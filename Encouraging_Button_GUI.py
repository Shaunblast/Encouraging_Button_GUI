# Need the function for the button, need customtkinter for the GUI
text = "You are going to impact the world in a good way! Keep going!"
count = 0
def button():
    global text # Makes the variable not just local to the function
    global count
    global label
    global GUI_button
    global reset_button
    if count == 0:
        count += 1
        label = customtkinter.CTkLabel(root, text=text)
        return label.pack()  # Needs to be used instead of print() so it goes to GUI
    elif count == 1:
        count -= 1
        label.destroy()
        GUI_button.destroy()
        return reset_button.pack(padx=100, pady=100)

def reset():
    global GUI_button
    global text
    global reset_button
    GUI_button = customtkinter.CTkButton(master=root, text="Press for Surprise!!", command=button)
    label = customtkinter.CTkLabel(root, text=text)
    reset_button.destroy()
    reset_button = customtkinter.CTkButton(master=root, text="Reset", command=reset)
    return GUI_button.pack(padx=100, pady=100)


import customtkinter

customtkinter.set_appearance_mode("dark") # sets my window to be dark mode
customtkinter.set_default_color_theme("dark-blue") # sets appearance theme to dark blue

root = customtkinter.CTk() # this is the created window
root.geometry("500x350") # sets the size of the window

# Create the button and set it to the root with text on top of it
GUI_button = customtkinter.CTkButton(master=root,text="Press for Surprise!!",command=button) # command calls fxn
GUI_button.pack(padx=100, pady=100) # Need this so it shows on the root window

reset_button = customtkinter.CTkButton(master=root, text="Reset", command=reset)


root.mainloop() # This is needed at the end to show the window