import pika
from flask import Flask, render_template, url_for, request 
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello！'

@app.route('/getCode', methods=['POST'])
def Do_editInfo():
    code = request.form["code"]
    state = request.form["state"]
    return code

@app.route('/test', methods=['POST'])
def Do_Test():    
    # push code
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=code,
        properties=pika.BasicProperties(delivery_mode=2)
    )

    connection.close()

    return "Success"

app.run(host='0.0.0.0')
