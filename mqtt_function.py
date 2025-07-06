import paho.mqtt.client as mqtt
import time

# --- Configuration ---
MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = "TEMPERATURE"
CLIENT_ID = "Smartphone" # Unique ID for your client

# --- Callback Functions ---
def on_connect(client, userdata, flags, rc, properties):
    """
    Called when the client connects to the MQTT broker.
    """
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
        print(f"Subscribed to topic: {MQTT_TOPIC}")
    else:
        print(f"Failed to connect, return code {rc}\n")

def on_message(client, userdata, msg):
    """
    Called when a message is received from the broker.
    """
    print(f"Received message on topic '{msg.topic}': {msg.payload.decode('utf-8')}")

# --- Main Program ---
if __name__ == "__main__":
    # Create a new MQTT client instance
    # Using CallbackAPIVersion.VERSION2 for newer paho-mqtt versions
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)

    # Assign callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT broker
    try:
        client.connect(MQTT_BROKER)
    except Exception as e:
        print(f"Error connecting to broker: {e}")
        exit(1)

    # Start the non-blocking loop for network traffic
    # This runs in a separate thread and handles reconnections automatically
    client.loop_start()

    print("MQTT client started. Listening for messages...")
    print("Press Ctrl+C to exit.")

    try:
        # Keep the main thread alive indefinitely to allow the background loop to run
        while True:
            time.sleep(1) # Small delay to prevent busy-waiting
    except KeyboardInterrupt:
        print("\nExiting program.")
        client.loop_stop() # Stop the background loop
        client.disconnect() # Disconnect from the broker