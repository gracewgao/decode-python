import certifi
import paho.mqtt.client as mqtt
import os
from gensim.summarization.summarizer import summarize
from google.cloud import language_v1
import numpy
import six

# Callback on connection
def on_connect(client, userdata, flags, rc):
    print(f'Connected (Result: {rc})')

    # See: https://docs.solace.com/Open-APIs-Protocols/MQTT/MQTT-Topics.htm
    client.subscribe('channels/+/chatlog')


# Callback when message is received
def on_message(client, userdata, msg):
    print(f'Got message {msg.payload}')
    # publish new summary every new messages
    text = str(msg.payload)
    # todo: change word count if needed
    summary = summarize(text)
    categories = classify(text)
    channelID = msg.topic.split('/')[1]
    client.publish('channels/' + channelID + '/summary', payload=summary)
    client.publish('channels/' + channelID + '/categories', payload=categories)


def classify(text, verbose=False):
    """Classify the input text into categories. """
    language_client = language_v1.LanguageServiceClient()

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = language_client.classify_text(request={'document': document})
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u"=" * 20)
            print(u"{:<16}: {}".format("category", category.name))
            print(u"{:<16}: {}".format("confidence", category.confidence))

    return result


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
client.connect('mr1rvhmgxn1b0t.messaging.solace.cloud', port=8883)

client.loop_forever()

