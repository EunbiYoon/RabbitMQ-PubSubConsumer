import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"secondconsumer: received new message :{body}")

# create connection
connection_parameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_parameters)

#create channel
channel=connection.channel()

#exchange type as fanout
channel.exchange_declare(exchange='pubsub',exchange_type=ExchangeType.fanout)

#declare queue -> it nees its own dedicated queue
queue=channel.queue_declare(queue='', exclusive=True)

#bind queue to exchange
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)


#consume queue
channel.basic_consume(queue=queue.method.queue ,auto_ack=True, 
    on_message_callback=on_message_received)

#check
print("Starting Consuming")

channel.start_consuming()