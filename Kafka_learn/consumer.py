from kafka import KafkaConsumer
import json

# Create consumer instance
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group',
    value_deserializer=lambda m: m.decode('utf-8')
)

print("Consumer started. Waiting for messages...")
print("Press Ctrl+C to stop\n")

try:
    for message in consumer:
        try:
            data = json.loads(message.value)
            print(f"Received JSON: {data['content']}")
        except json.JSONDecodeError:
            print(f"Received TEXT: {message.value}")

        print(f"  Partition: {message.partition}")
        print(f"  Offset: {message.offset}")
        print(f"  Timestamp: {message.timestamp}\n")

except KeyboardInterrupt:
    print("\nShutting down consumer...")
finally:
    consumer.close()