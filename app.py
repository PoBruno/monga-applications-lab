from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api', methods=['POST', 'GET'])
def chat():
    response = {
        'message': 'Hello, ChatGPT!'
    }
    if request.method == 'POST':
        data = request.get_json()
        # código para processar o JSON aqui
        response['message'] = chatgpt_response
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
