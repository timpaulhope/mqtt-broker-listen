import paho.mqtt.client as mqtt
import time
import json
import yaml
import os

def load_mqtt_config(config_file_path):
    """Load MQTT configuration from YAML file."""
    with open(config_file_path, "r") as file:
        config = yaml.safe_load(file)
    return config["mqtt_broker"]

def load_topics(config_file_path):
    """Load topics from YAML file."""
    with open(config_file_path, "r") as file:
        config = yaml.safe_load(file)
    print(config["topics"])
    return config["topics"]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        for topic in topics:
            client.subscribe(topic["topic"])
    else:
        print("Connection failed with code", rc)

def on_message(client, userdata, msg):
    global received_messages
    received_messages[msg.topic] = msg.payload.decode()
   
    for key, value in received_messages.items():
        print(f"Topic: {key}")
        try:
            # Attempt to parse the JSON value
            json_value = json.loads(value)
            print("Value (parsed JSON):")
            print(json.dumps(json_value, indent=4))
        except json.JSONDecodeError as e:
            # Handle the case where the value is not valid JSON
            print(f"Value (not valid JSON): {value}")
        print("=" * 50)  # Separation line


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection")

def main(config_file_path):
    global topics
    global received_messages
    received_messages = {}

    # Load MQTT configuration
    mqtt_config = load_mqtt_config(config_file_path)
    broker_address = mqtt_config["broker_address"]
    port = mqtt_config["port"]
    username = mqtt_config["username"]
    password = mqtt_config["password"]
    keepalive = mqtt_config["keepalive"]

    # Load topics
    topics = load_topics(config_file_path)

    # Create an MQTT client instance
    client = mqtt.Client()
    # Set credentials
    client.username_pw_set(username, password)
    
    # Set up callback functions
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    # Connect to the MQTT broker
    client.connect(broker_address, port, keepalive)

    # Start the MQTT client loop
    client.loop_start()

    # Keep the script running
    try:
        while True:
            time.sleep(1)  # You can adjust the sleep time as needed
    except KeyboardInterrupt:
        pass

    # Disconnect from the MQTT broker
    client.disconnect()

if __name__ == "__main__":
# Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    config_file = "mqtt_config.yaml"
    
    # Define the relative path to the YAML configuration file
    config_file_path = os.path.join(script_dir, config_file)
    
    main(config_file_path)
