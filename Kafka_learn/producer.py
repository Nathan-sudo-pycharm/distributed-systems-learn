from kafka import KafkaProducer
import json
import time

# Create producer instance
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send 10 messages
for i in range(10):
    message = {
        'message_id': i,
        'content': f'Message number {i}',
        'timestamp': time.time()
    }

    # Send to test-topic
    future = producer.send('test-topic', value=message)

    # Block until message is sent
    result = future.get(timeout=10)

    print(f"Sent message {i} to partition {result.partition} at offset {result.offset}")

    time.sleep(1)

producer.close()
print("\nAll messages sent successfully!")