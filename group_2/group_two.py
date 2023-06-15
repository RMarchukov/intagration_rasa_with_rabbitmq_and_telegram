import json
import pika
import requests


def callback(ch, method, properties, body):
    if body is not None:
        data = json.loads(body)
        if data['event'] == 'user':
            mes = f"Your message from another service - {data['text']}"
            sender_id = data['sender_id']
            rp = requests.post('https://api.telegram.org/bot6121312355:AAEe-mdQTDNFmVw4MfQeCnNkz-kGRfhCKgg/sendMessage',
                               params={'chat_id': sender_id, 'text': mes})
            print(rp.json())

            # channel.queue_declare(queue='3', durable=True)
            # channel.basic_publish(exchange='', routing_key='3', body=mes)
            # print(f'sent {mes}')
            # connection.close()


credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", credentials=credentials)
)

channel = connection.channel()
channel.queue_declare(queue='all', durable=True)
channel.basic_consume(queue="all", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
