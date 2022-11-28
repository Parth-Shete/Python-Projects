from tkinter import *  #* means we are importing everything that is present in the given module
from tkinter.filedialog import asksaveasfilename, askopenfilename  #This will save the file name
import subprocess
compiler = Tk()  #named the compiler as compiler
compiler.title('My IDE')
file_path = ''  #Here we are storing the file path

def set_file_path(path):
    global file_path  #Calling file_path as global variable
    file_path = path

def open_file():  #This function will open the file
    path = askopenfilename(filetypes = [('Python Files', '*.py')])  #This will open up the dialog and ask the user to save it
    with open(path, 'r') as file:  #This will read the file
        code = file.read()  #This will read the file
        editor.delete('1.0', END)  #This will delete everything
        editor.insert('1.0', code)  #This will replace the code that we have deleted
        set_file_path(path)

def save_as():  #This function will save as the code/file
    if file_path == '':
        path = asksaveasfilename(filetypes = [('Python Files', '*.py')])  #This will open up the dialog and ask the user to save it
    else:
        path = file_path  #This will save the path as a file_path
    with open(path, 'w') as file:  #This will write the file
        code = editor.get('1.0', END)  #This will get everything
        file.write(code)  #This will write everything that has been written on the editor
        set_file_path(path)  #This will save the file path

def run():
    if file_path == '':
        save_promt = Toplevel()
        text = Label(save_promt, text = 'Please save your code before execution')  #This is a message for saving the code first before execution
        text.pack()
        return
    command = f'Python {file_path}'  #This will make the file_path
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)  #Python will open and will do some work and this is also used to communicate with the compiler
    output, error = process.communicate()  #This will get the output and error while compiling the code
    code_output.insert('1.0', output)  #This will make the output one line below the other
    code_output.insert('1.0', error)  #If the code has some error, then it would be displayed in the output box

menu_bar = Menu(compiler)  #menu for the compiler

file_menu = Menu(menu_bar, tearoff = 0)  #to tear the dashed line above the run option
file_menu.add_command(label='Open', command = open_file)  #Creating the button for the option run
file_menu.add_command(label='Save', command = save_as)  #This will save the code
file_menu.add_command(label='Save As', command = save_as)  #This will save as the code
file_menu.add_command(label='Exit', command = exit)  #This will exit the command
menu_bar.add_cascade(label='File', menu=file_menu)  #for styling

run_bar = Menu(menu_bar, tearoff = 0)  #to tear the dashed line above the run option
run_bar.add_command(label='Run', command = run)  #Creating the button for the option run
menu_bar.add_cascade(label='Run', menu=run_bar)  #for styling

compiler.config(menu = menu_bar)  #to configure the menu_bar

editor = Text()  #names the editor as editor
editor.pack()

code_output = Text(height = 10)  #This is to generate the compiled code in the compiler itself
code_output.pack()

compiler.mainloop()  #this is the mainframe .i.e. the start
