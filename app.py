import json,datetime,time
from flask import Flask, request
app = Flask(__name__)

gColdRun = None

@app.route('/event-invoke', methods = ['POST'])
def invoke():
    # Get all the HTTP headers from the official documentation of Tencent
    request_id = request.headers.get("X-Scf-Request-Id", "")
    time.sleep(3)
    global gColdRun
    ret = 'hot||%s' % request_id
    if gColdRun is None:
        gColdRun = True
        ret = 'cold||%s' % request_id
    print(ret)
    retBody ={
              "isBase64Encoded": False,
              "statusCode":200,
              "headers":{},
              "body":ret
    }
    print(retBody)
    return json.dumps(retBody)

@app.route('/web-invoke/python-flask-http', methods = ['POST','GET'])
def web_invoke():
    # Get all the HTTP headers from the official documentation of Tencent
    request_id = request.headers.get("X-Scf-Request-Id", "")
    global gColdRun
    time.sleep(3)
    ret = 'hot||%s' % request_id
    if gColdRun is None:
        gColdRun = True
        ret = 'cold||%s' % request_id
    print(ret)
    retBody ={
              "isBase64Encoded": False,
              "statusCode":200,
              "headers":{},
              "body":ret
    }
    print(retBody)
    return json.dumps(retBody)

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
    time.sleep(3)
    return json.dumps(rep)

def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
