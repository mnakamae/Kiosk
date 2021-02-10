from guizero import App, TextBox, Text, PushButton
import webbrowser

app = App(title="Kiosk")

# WIDGET CODE GOES HERE

input_msg = TextBox(app)
display_msg = Text(app, "TEACHER'S MESSAGE", size = 16, font="Times New Roman", color="black")

def printMsg():
	display_msg.value = input_msg.value
	
def openCalendarLink():
	webbrowser.open("https://ee.calpoly.edu/faculty/phummel/")
	
def openSchedulerLink():
	webbrowser.open("https://phummel.youcanbook.me/")
	
		
update_text = PushButton(app, command=printMsg, text="Input a message")

openCalendar = PushButton(app, command=openCalendarLink, text="Open Calendar")

openScheduler= PushButton(app, command = openSchedulerLink, text="Open Scheduler")

app.display()