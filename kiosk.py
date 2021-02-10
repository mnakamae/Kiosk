from guizero import App, TextBox, Text, PushButton
import webbrowser
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("MarksPi")

myMQTTClient.configureEndpoint("a1sx0mf4p4ad71-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/Downloads/AmazonRootCA1.pem", "/home/pi/Downloads/45c4e26ece-private.pem.key", "/home/pi/Downloads/45c4e26ece-certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)

myMQTTClient.connect()


app = App(title="Kiosk")

# WIDGET CODE GOES HERE

hummel_msg = Text(app, "waiting for new message...", size = 16, font="Times New Roman", color="black")


def recvMsg(self, params, packet):
    hummel_msg.value = packet.payload
	
def openCalendarLink():
	webbrowser.open("https://ee.calpoly.edu/faculty/phummel/")
	
def openSchedulerLink():
	webbrowser.open("https://phummel.youcanbook.me/")
	
	
myMQTTClient.subscribe("hummel", 1, recvMsg)

openCalendar = PushButton(app, command=openCalendarLink, text="Open Calendar")

openScheduler= PushButton(app, command = openSchedulerLink, text="Open Scheduler")

app.display()


