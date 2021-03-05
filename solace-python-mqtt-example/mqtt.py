import certifi
import paho.mqtt.client as mqtt
import os
from gensim.summarization.summarizer import summarize

# Callback on connection
def on_connect(client, userdata, flags, rc):
    print(f'Connected (Result: {rc})')

    # See: https://docs.solace.com/Open-APIs-Protocols/MQTT/MQTT-Topics.htm
    client.subscribe('channels/*/chatlog')


# Callback when message is received
def on_message(client, userdata, msg):

    # publish new summary every new messages
    text = msg.chatlog
    # todo: change word count if needed
    summary = summarize(text, word_count=30)
    channelID = msg.topic.split('/')[1]
    client.publish('channels/' + channelID + '/summary', payload=summary)


# If using websockets (protocol is ws or wss), must set the transport for the client as below
# client = mqtt.Client(transport='websockets')
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

# Required if using TLS endpoint (mqtts, wss, ssl), remove if using plaintext
# Use Mozilla's CA bundle
client.tls_set(ca_certs=certifi.where())

# Enter your password here
client.username_pw_set('solace-cloud-client', 'tjn2jlk195ntk213e5idk29929')

# Use the host and port from Solace Cloud without the protocol
# ex. "ssl://yoururl.messaging.solace.cloud:8883" becomes "yoururl.messaging.solace.cloud"
client.connect('ssl://mr1rvhmgxn1b0t.messaging.solace.cloud', port=8883)

client.loop_forever()
