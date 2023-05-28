from model import prediction
from flask import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.get('/api/v1/prediction/<int:credits>')
@cross_origin('http://localhost:3000')
def predict(credits):
    if credits < 4 or credits > 6:
        return jsonify({'error': 'Invalid credits'}), 400
    else:
        return jsonify({'prediction': prediction(credits)}), 200


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
