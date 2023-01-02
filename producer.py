import pika
from pika.exchange_type import ExchangeType
# create connection
connection_parameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_parameters)

#create channel
channel=connection.channel()

#declare queue -> wont declare queue
#channel.queue_declare(queue='letterbox')

#exchange type as fanout
channel.exchange_declare(exchange='pubsub',exchange_type=ExchangeType.fanout)

#message
message="Hello I want to broadcast this message"
channel.basic_publish(exchange='pubsub',routing_key='',body=message)

#check
print(f"sent message :{message}")

#close connection
connection.close()
