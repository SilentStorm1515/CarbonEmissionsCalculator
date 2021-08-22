#To create our GUI, we used the PySimpleGUI library
import PySimpleGUI as psg

#This sets the color theme of the GUI
#We chose a dark green color scheme to keep with our ecological theme
psg.theme('DarkGreen1')

#This is the initial prompt
#This gives the user a bit of information regarding the program, as well as how to use it
#It also takes in the information required for the calculation by the user
#We have also added in a submit and cancel button for ease of use
layout = [[psg.Text("Welcome to the carbon emissions calculator!")],
          [psg.Text("This is a system to help you figure out your personal CO2 emissions and the environmental impact you have in a year.")],
          [psg.Text("Just input some of your information (like monthly electrical usage) and we'll help you figure it all out.")],
          [psg.Text("What is your monthly electrical usage in kWh?\n", size = (45, 1))],
          [psg.InputText()],
          [psg.Text("How many hours do you spend flying in a plane per year?", size = (45, 1))],
          [psg.InputText()],
          [psg.Text("Do you drive an electric/hybrid car?\n", size = (45, 1))],
          [psg.InputText()],
          [psg.Submit(), psg.Cancel()]]

#This sets up the window for use
window = psg.Window("Carbon Emissions Calculator", layout)
event, values = window.read()

#This stores the information given by the user into several variables after the user submits their entry
#It also closes the window after the entry is submitted
if event == 'Submit':
    userElectrical = int(values[0])
    userPlane = int(values[1])
    userDrive = str(values[2])
    window.Close()

#If the user chooses to exit the program, they can select the cancel button and the program will quit
if event == 'Cancel':
    window.Close()

#This tells the program whether or not the user drives an electric car, and initializes the varible based on this
if userDrive == "yes":
  userDrive = 0
else:
#The average gasoline-powered car produces around 5 tonnes of CO2 per year
  userDrive = 5

#This is the final calculation that determines the number of tonnes of CO2 that the user creates per year
total = str((userElectrical*0.23314)+userDrive+(userPlane*0.09))

#The average person on Earth produces around 4 tonnes of CO2 per year
#We can determine how much more or less CO2 the user creates per year compared to the average person
difference = float(total) - 4
difference = round(difference, 3)

higherLower = ""

#If the user's CO2 output is greater than that of the average person, we can notify them and tell them how much more they emit
if (float(total) > 4.000):
   higherLower = "Your total CO2 output per year is " + str(difference) + " tonnes greater than the average person on Earth. To reduce your CO2 emissions, you can ride a bike to work/school, buy local produce, and conserve as much water as possible. For more information, head to this link: https://www.futurelearn.com/info/blog/how-to-reduce-your-carbon-footprint-tips"
#If the user's CO2 output is less than that of the average person, we can tell them how much less they use
elif (float(total) < 4.000):
#Taking the absolute value of the difference will prevent any negative numbers from appearing
  difference = abs(difference)
  higherLower = "Your total CO2 output is " + str(difference) + " tonnes less than the average person on Earth. Great job! Are there any other ways that you can reduce your output to bring it down even more?"

#This creates a second GUI box with all of the calculation outputs and where they can find more information
layout1 = [[psg.Text("Your yearly CO2 ouput is: " + total + " tonnes", size = (45, 1))],
           [psg.Text(higherLower, size = (65, 6))]]

newWindow = psg.Window("Carbon Emissions Calculator", layout1)

event, values = newWindow.read()
