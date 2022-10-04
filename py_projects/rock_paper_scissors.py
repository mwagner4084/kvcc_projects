"""
Name: Marissa Wagner
Date: 09/30/22
CRN: 10235
Class name: CIS 226: Advanced Python Programming
Total Time: 5 Hours

1. How will you solve the problem?
    - Import a Python GUI library.
    - Define the layout of GUI.
    - Create Window.
    - Run Event Loop
    - Perform cleanup.

2. What did you actually do to solve the problem?
    - Import PySimpleGUI as GUI library.
    - Create an array of random objects.
    - Create variables for user, cpu, and winner.
    - Create function to determine winner.
    - Define layout of GUI.
        - Menubar includes: File -> Quit, Help -> About...
        - Name input / output message
        - Prompt message
        - Button selection
        - Output text
        - Statusbar
    - Create Window with GUI title and layout.
    - Run Event Loop while updating Statusbar.
    - Display About Dialog Box and close window after leaving event loop.

3. What did you test?
    - The program displays the output message in the output field when the 'Ok' button is selected.
    - The program displays the correct response in the output field when the 'Rock', 'Paper, and 'Scissors' buttons are selected.
    - The program clears the output field when the 'Play!' button is selected.
    - The program displays the About Dialog Box and exits the program when the 'Quit' and 'Exit' buttons are selected.
    - The program displays the correct message in the statusbar field when the 'Play!', 'Ok, 'Exit', and 'Quit' buttons are selected.

4. Explain your code for your future self and others.
    - PySimpleGUI is implemented as a library to display window and define layout.
    - The GUI application is a simple program that emulates a Rock, Paper, Scissors game when ran through the event loop.

"""

import PySimpleGUI as sg
import random

# create print messages
window_title = "Rock-Paper-Scissors Game"
prompt_msg = "Choose your weapon!"
status_active = "Program Status: Active"
staus_warm = "Program Status: Warmimg Up"
status_idle = "Program Status: Idle"
status_shutdown = "Program Status: Shutting Down"
about = """\
Thank you for playing my Rock, Paper, Scissors game.\n\n
This program allows the user to engage in a computer emulated game of Rock, Paper, Scissors.\n
For more information on PySimpleGUI, visit https://www.pysimplegui.org/en/latest/ .
"""

menu_def = [
    ['&File', ['&Exit']],
    ['&Help', ['&About...']]
]

# define the layout of the GUI with a list of lists
# each inner list is another row
layout = [
    [sg.Menu(menu_def)], # menubar
    [sg.Text("What should we call you?")], # input text
    [sg.Input(key='-INPUT-'), sg.Button('Ok')], # input and button
    [sg.Text(size=(30,1), key='output')],
    [sg.Text(prompt_msg)], # prompt message
    [sg.Button('Rock', disabled=True), sg.Button('Paper', disabled=True), sg.Button('Scissors', disabled=True)], # disable until user selects 'Ok'
    [sg.Output(size=(40,10), key='-OUTPUT-')], # adjust output box size
    [sg.Button('Play!', disabled=True), sg.Button('Quit')], # play = reset / disable until user selects 'Ok', quit will exit
    [sg.StatusBar('', size=(25,1), key='-STAT-')] # statusbar
]

# create array of random objects
values = ["Rock", "Paper", "Scissors"]

# create a single window with layout
window = sg.Window(window_title, layout)

def determine_winner(user_choice, computer_choice):
    # create print messages
    win_msg = f"Nice work, {values['-INPUT-']}! The computer chose {computer_choice}, and you absolutely destroyed it with {user_choice}. Press play for a re-match.\n"
    lose_msg = f"Sorry, {values['-INPUT-']}. You made the unfortunate choice of {user_choice} as your weapon. The computer crushed you with {computer_choice}. Too bad. Press play for a re-match.\n"
    tie_msg = f"Ah, sorry, {values['-INPUT-']} - it's a tie. You chose {user_choice}, and the computer also chose {computer_choice}. Press play for a re-match.\n"

    # function to determine winner
    if user_choice == computer_choice:
        return tie_msg
    if user_choice == "Scissors":
        if computer_choice == "Paper":
            return win_msg
        return lose_msg # for every chance for user to win, chance for cpu to win
    if user_choice == "Paper":
        if computer_choice == "Rock":
            return win_msg
        return lose_msg
    if user_choice == "Rock":
        if computer_choice == "Scissors":
            return win_msg
        return lose_msg


while True:
    # pause until an event in the GUI happens
    event, values = window.read()
    # check if user has closed the window or clicked the 'Quit' or 'Exit' button
    if event == sg.WIN_CLOSED or event == 'Quit' or event == 'Exit':
        # statusbar with program update
        window['-STAT-'].update(status_shutdown)
        break
    elif event == 'About...':
        # display about dialog box
        sg.popup("About Dialog", about)
        # statusbar with program update
        window['-STAT-'].update(status_idle)
        continue
    # check if user has clicked the 'Ok' button
    elif event == 'Ok':
        window['-OUTPUT-'].update(f"Hey, { (values['-INPUT-']) }! \nWelcome to my Rock, Paper, Scissors game! \nSelect your weapon of choice to begin.\n")
        # enable buttons
        window['Play!'].update(disabled=False)
        window['Rock'].update(disabled=False)
        window['Paper'].update(disabled=False)
        window['Scissors'].update(disabled=False)
        # statusbar with program update
        window['-STAT-'].update(staus_warm)
        continue
    # check if user has clicked the 'Play!' button
    elif event == 'Play!':
    # enable buttons
        window['Rock'].update(disabled=False)
        window['Paper'].update(disabled=False)
        window['Scissors'].update(disabled=False)
        # reset window
        user_choice = ''
        computer_choice = ''
        window['-OUTPUT-'].update('')
        # statusbar with program update
        window['-STAT-'].update(status_active)
        continue
    # statusbar with program update
    else:
        # disable buttons
        window['Rock'].update(disabled=True)
        window['Paper'].update(disabled=True)
        window['Scissors'].update(disabled=True)
        window['-STAT-'].update(status_active)

    # check if user selected a choice
    user_choice = event
    # inside the event loop so it gets changed everytime. could also be put inside the determine_winner function.
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    # determine who won the game
    winning_choice = determine_winner(user_choice, computer_choice)
    # print message
    print(winning_choice)

# display about dialog box
sg.popup("About Dialog", about)

# close the window when leaving event loop
window.close()
