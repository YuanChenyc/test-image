import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/event-invoke', methods = ['POST'])
def invoke():
    # Get all the HTTP headers from the official documentation of Tencent
    request_id = request.headers.get("X-Scf-Request-Id", "")
    print("SCF Invoke RequestId: " + request_id)

    event = request.get_data()
    event_str = event.decode("utf-8")

    print ("Hello from SCF event function, your input: ")
    rep = {
        "isBase64Encoded": "false",
        "statusCode": "200",
        "headers": {
            "x-custom-header": "no"
        },
        "body": "Hello"
    }
    print ("Hello,World")
    return json.dumps(rep)

@app.route('/web-invoke/python-flask-http', methods = ['POST','GET'])
def web_invoke():
    # Get all the HTTP headers from the official documentation of Tencent
    request_id = request.headers.get("X-Scf-Request-Id", "")
    print("SCF Invoke RequestId: " + request_id)
    
    event = request.get_data()
    event_str = event.decode("utf-8")
    
    print ("Hello from SCF HTTP function, your input: ")
    rep = {
        "isBase64Encoded": "false",
        "statusCode": "200",
        "headers": {
            "x-custom-header": "no"
        },
        "body": "Hello"
    }
    print ("Hello,World")
    return json.dumps(rep)

@app.route('/invoke', methods = ['POST','GET'])
def handler():
    rep = {
        "isBase64Encoded": "false",
        "statusCode": "200",
        "headers": {
            "x-custom-header": "no"
        },
        "body": "hello"
    }
    return json.dumps(rep)

def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
