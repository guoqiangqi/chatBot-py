from flask import Flask, request, Response
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from user_manager import authenticate, identity
from token_operator import secret_key
from chatgpt_util import chatWithGPT
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
# app.config['JWT_AUTH_URL_RULE'] = '/auth'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=30)

api = Api(app)

jwt = JWT(app, authenticate, identity)

class ChatGPT(Resource):
    @jwt_required()
    def get(self):
        return current_identity

    @jwt_required()
    def post(self):
        payload = request.get_json()
        question = payload['question']

        messageSystem = {"role": "system", "content": "You are a openEuler community assistant, your name is Xiao Zhi."}
        messageQuestion = {"role": "user", "content": question}
        messages = [messageSystem, messageQuestion]

        response = chatWithGPT(messages, model="gpt-3.5-turbo", stream=True)

        def generate():
            for chunk in response:
                yield str(chunk['choices'][0]['delta']).strip("{}\n") + "\n"

        return Response(generate(), mimetype='text/event-stream')

api.add_resource(ChatGPT, '/chatgpt')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
