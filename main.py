from kafka import KafkaProducer


producer = KafkaProducer(
bootstrap_servers=["localhost:29092"]
)
producer.send("my-topic", value="Hello, World!".encode("utf-8"))

# Ensure all buffered messages are sent
producer.flush()

print("Message sent.")