''' Banana preferences survey '''

import tkinter as tk
from typing import Sized

## Functions used in this app (this part can be saved in a .py file apart)
# create a event the submit button
def on_submit():
  '''To be run when users submits the form'''
  name = txtline_var.get() # exemple of a tk text variable
  number = numinput_var.get()
  selected = list1_var.get()
  
  if checkbox_var.get() == False:
    check = ' do not '
  else:
    check = ' '
  
  # text = txtinput.get('1.0',tk.END) # thiw get() method require 2 items (starting location, end location)

  message = (
    f'Thanks to take que survey, {name}. \n'
    f'Thanks for{check}complain to our survey. \n'
    f'You have selected {number} {selected}!'
  )

  output_label.configure(text=message)


## Part 01 - Setting all elements of the app ##

# root is the upper instance that acept widgets
root = tk.Tk()

# window's title
root.title('Wellcome to GUI development with Tkinter')

# window size
root.geometry('640x380+300+300')
root.resizable(True,True)

survey_title = tk.Label(
  root,
  text='Please take a survey',
  font=('Arial 16 bold')
)

txtline_label = tk.Label(
  root,
  text='What is your name?'
)

# single line text input
txtline_var = tk.StringVar(root) # tk control variable
txtline = tk.Entry(root, textvariable=txtline_var) # here the bind it by 'textvariable' parameter

# check box
checkbox_var = tk.BooleanVar(root)
checkbox = tk.Checkbutton(
  root,
  text='Check this box if you complain',
  variable=checkbox_var # here the bind is by 'variable' parameter
)

numinput_label = tk.Label(
  root,
  text='How much is your number?',
  anchor='w'
)

# input number
numinput_var = tk.IntVar(value=0) # intvar can be created with a start value
numinput = tk.Spinbox(
  root,
  from_=0,
  to=100,
  increment=1,
  textvariable=numinput_var # it's odd but the bind in this widget always will use 'textvariable'
)

list1_label = tk.Label(
  root,
  text='Check one option of the list'
)

# adding choices to the list1
list1_var = tk.StringVar(value='option 1')

list1_choices = (
  'option 1',
  'option 2',
  'option 3',
  'option 4'
)

# input list
list1 = tk.OptionMenu(
  root,
  list1_var,
  *list1_choices
)


# this is a example of a frame (until now, all widgets are attached to the root instance)
frame1 = tk.Frame(root)

radioint_label = tk.Label(
  frame1,
  text='Select one of these options above:'
)

# radio button inputs
radioinput_var = tk.BooleanVar(value=True)

radioinput_yes = tk.Radiobutton(
  frame1,
  text='Yes',
  value=True,
  variable=radioinput_var
)

radioinput_no = tk.Radiobutton(
  frame1,
  text='No',
  value=False,
  variable=radioinput_var
)

txtinput_label = tk.Label(
  root,
  text='This is a open text widget'
)

# open text input
txtinput = tk.Text(
  root,
  height=3 # how many lines the box will be
)

# select button input
buttoninput = tk.Button(
  root,
  text='Submit Button'
)

# creating a output label to see how change the app's interface
output_label = tk.Label(
  root,
  text='',
  anchor='w', # wich side of the widget the text will be stuck (North, South, Weast and East)
  justify='left' # wich sithe the text will align (left, right and center)
)

## Part 02 - Setting the application layout ##
# there are 3 types of geometry methods (pack, grid and place)
# here we'll use the grid system

# 2.1 - application's interface control grid
survey_title.grid(row=0,column=0,columnspan=2)

txtline_label.grid(row=1,column=0)
txtline.grid(row=1,column=1,ipadx=10) # the 'sticky' is used to expand the widget in 4 directions

checkbox.grid(row=2,column=0,columnspan=2,sticky='we')

numinput_label.grid(row=3,column=0, sticky='we')
numinput.grid(row=3,column=1,sticky='we')

list1_label.grid(row=4,column=0,columnspan=2,sticky='w',pady=5) # padx and pady are spaces around the widget
list1.grid(row=5,column=0,columnspan=2,sticky='we',padx=25)

frame1.grid(row=6,column=0,sticky='w')
radioint_label.grid(row=7,column=0,columnspan=2)
radioinput_yes.grid(row=8,column=0)
radioinput_no.grid(row=8,column=1)

txtinput_label.grid(row=9,column=0,sticky='w')
txtinput.grid(row=10,column=0,columnspan=2,sticky='nsew')

output_label.grid(row=99,column=0,sticky='nsew',columnspan=2)
buttoninput.grid(row=100,column=0)

# 2.2 - root expand control
'''By default, Tkinter will make our window just large enough to contain 
all the widgets we place on it; but what happens if our window 
(or containing frame) becomes larger than the space required 
by our widgets? By default, the widgets will remain as they are, 
stuck to the upper-left side of the application. If we want the 
GUI to expand and fill the space available, we have to tell the 
parent widget which columns and rows of the grid will expand. 
We do this by using the parent widget's 
columnconfigure() and rowconfigure() methods.'''

root.columnconfigure(1,weight=1) #(wichcolumn, how_much_extra_space_the_column_will_get)

root.rowconfigure(99,weight=2)
root.rowconfigure(100,weight=1) # here the row 100 will get 1/3 of the extra space

# 2.3 - Building the App's responsiveness
'''Actions (button click or a keystroke) are known as events. To 
make the program respond to an event, we need to bind the event to a function,
which we call a callback

There are few ways to bind events to callback functions:
1 - using the widget's method .configure(command=some_function) # more simple
2 - using the widget's method .bind() # we'll see in chapter 06
'''
buttoninput.configure(command=on_submit)

'''For some widgets like radiobutton and checkbox we'll need more control
of the variables. To achieve this, we will see the tkinter control variables now.

4 types of variables:
1 - StringVar
2 - IntVar
3 - DoubleVar
4 - BooleanVar
'''

## application loop ##
root.mainloop()