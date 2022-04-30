import os
import json
import aiml
from flask import Flask, request

kernel = aiml.Kernel()
kernel.loadBrain('./brain/aiml-core.aar')

print(kernel.respond('Fuck you'))

app = Flask(__name__)

@app.route('/aiml')
def aiml_response():
    return json.dumps(kernel.respond(request.args['text']))

@app.route('/')
def status():
    return 'OK'

if __name__ == '__main__':
    app.run(port=4002)
