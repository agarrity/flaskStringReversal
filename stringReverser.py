from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<string:forwardString>', methods=['GET'])
def getReversedString(forwardString):
    return jsonify({'ReversedString' : forwardString[::-1]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80)