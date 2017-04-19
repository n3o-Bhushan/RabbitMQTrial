import pika 

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = conn.channel()
channel.queue_declare(queue="hey")

channel.basic_publish(exchange='',
	routing_key='hey',
	body ='Hey there!')
print "[x] sent 'Hey there!'"
conn.close()