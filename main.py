from model import prediction
from flask import *

app = Flask(__name__)


@app.get('/api/v1/prediction/<int:credits>')
def predict(credits):
    if credits < 4 or credits > 6:
        return jsonify({'error': 'Invalid credits'}), 400
    else:
        return jsonify({'prediction': prediction(credits)}), 200


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
