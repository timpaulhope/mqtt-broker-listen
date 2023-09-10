# mqtt-broker-listen

This Python script is an example of a MQTT client that subscribes to one or more MQTT topics, receives messages from a broker, and processes the messages. It is designed to be easily configurable through a YAML configuration file and can handle both JSON and non-JSON message payloads.

## Prerequisites

Before using this MQTT client, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- The `paho-mqtt` library installed. You can install it using pip:

  ```
  pip install paho-mqtt
  ```

## Installation

1. Clone or download the repository to your local machine.

2. Install the required dependencies, as mentioned in the Prerequisites section.

## Configuration

1. Create a YAML configuration file (e.g., `mqtt_config.yaml`) with the following structure:

   ```yaml
   mqtt_broker:
     broker_address: "mqtt.example.com"  # Replace with your MQTT broker address
     port: 1883  # Replace with the MQTT broker port
     username: "your_username"  # Replace with your MQTT broker username
     password: "your_password"  # Replace with your MQTT broker password
     keepalive: 60  # Adjust the keepalive interval as needed

   topics:
     - topic: "your/mqtt/topic1"  # Replace with MQTT topics you want to subscribe to
     - topic: "your/mqtt/topic2"
   ```

   Make sure to replace the placeholders with your MQTT broker details and the topics you want to subscribe to.

2. Save the YAML configuration file in the same directory as the script or provide the correct path to the configuration file in the script's `config_file` variable.

## Usage

Run the script by executing the following command:

```bash
python mqtt_listen.py
```

The MQTT client will connect to the MQTT broker, subscribe to the specified topics, and display received messages in the console. If a received message is valid JSON, it will be pretty-printed; otherwise, the raw message content will be shown.

To stop the script, press `Ctrl + C`.

## Roadmap

This code is still underdevelopent (is still a bit hacky)

## License

This MQTT client is released under the [MIT License](LICENSE). You can find the full license details in the [LICENSE](LICENSE) file.

