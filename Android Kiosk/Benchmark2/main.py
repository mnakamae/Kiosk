from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json

def connect_mqtt(msg):
    # Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
    ENDPOINT = "a1sx0mf4p4ad71-ats.iot.us-east-1.amazonaws.com"
    CLIENT_ID = "testAndroid"
    PATH_TO_CERT = "certs/phone_certificate.pem.crt"
    PATH_TO_KEY = "certs/phone_private.pem.key"
    PATH_TO_ROOT = "certs/root.pem"
    MESSAGE = "Hello World"
    TOPIC = "hummel"
    RANGE = 20

    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=PATH_TO_CERT,
        pri_key_filepath=PATH_TO_KEY,
        client_bootstrap=client_bootstrap,
        ca_filepath=PATH_TO_ROOT,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=6
    )
    print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
    # Make the connect() call
    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    print("Connected!")
    # Publish message to server desired number of times.
    print('Begin Publish')
    mqtt_connection.publish(topic=TOPIC, payload=msg, qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '" + msg + "' to the topic: " + TOPIC)
    print('Publish End')
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()


class MainApp(App):

    def build(self):
        # b = BoxLayout(orientation='vertical')
        # self.client.loop.start()
        layout = BoxLayout(orientation="vertical")
        self.input = TextInput(text="Enter Message Here")
        butt = Button(text="Submit", on_press=self.publish)

        layout.add_widget(self.input)
        layout.add_widget(butt)

        return layout

    def publish(self, obj):
        print("Publishing data to AWS: ", self.input.text)
        connect_mqtt(self.input.text)

if __name__ == '__main__':
    app = MainApp()
    app.run()