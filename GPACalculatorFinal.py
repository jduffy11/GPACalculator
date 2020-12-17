import PySimpleGUI as sg
# arrays to take in user input
grades = []
cHours = []
# sets theme for GUI and creates first window to retrieve number of classes
sg.theme('DarkAmber')
events, values = sg.Window('GPA Calculator', [[sg.T('Enter the number of classes you are taking'),
                                               sg.In(key='numC')],
                                              [sg.B('OK')]]).read(close=True)
numClasses = values['numC']
# Class to calculate GPA based on entered information
def calculate(cHours):
    total= 0
    k = 0
    numCredits = 0
    global gpa
    gpa = 0.0
    while k < len(cHours):
        for score in grades:
            if( score >= 90 and score <= 100):
                total = total + (4.0 * cHours[k])
                k += 1
            elif( score >= 80 and score <= 89):
                total = total + (3.0 * cHours[k])
                k += 1
            elif( score >= 70 and score <= 79):
                total = total + (2.0 * cHours[k])
                k += 1
            elif( score >= 60 and score <= 69):
                total = total + (1.0 * cHours[k])
                k += 1
            elif( score < 60):
                total = total + 0.0
                k += 1
    for i in cHours:
        numCredits = numCredits + i
    gpa = total / numCredits
    round(gpa, 2)
# Creates layout for GUI window, with two text entry boxes and two buttons
layout = [[sg.T('Enter your score for a class')],
          [sg.Input(key='grades', enable_events=True)],
          [sg.T('How many credit hours is this class worth?')],
          [sg.Input(key='cHours', enable_events=True)],
          [sg.B('Enter another class')],
          [sg.B('Calculate GPA')]]
window = sg.Window('Gpa Calculator', layout)
# while loop to keep GUI updated as input is received until it loop is broken
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'grades' and values['grades'] and values['grades'][-1] not in ('0123456789'):
        window['grades'].update(values['grades'][:-1])
    if event == 'cHours' and values['cHours'] and values['cHours'][-1] not in ('0123456789'):
        window['cHours'].update(values['cHours'][:-1])
    if event == 'Enter another class':
        grades.append(int(values['grades']))
        cHours.append(int(values['cHours']))
        window['grades']('')
        window['cHours']('')
    if event == 'Calculate GPA':
        calculate(cHours)
        sg.popup('Your GPA is: ', gpa)

window.close()