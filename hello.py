from flask import Flask, request
import pickle
app = Flask(__name__)

with open('pipe.pickle', 'rb') as f:
    pipe = pickle.load(f)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/json_test')
def json_test():
    return{'prediction':.05}

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        the_data = request.get_json(force=True)
        newdata = the_data['newdata']
        prediction = pipe.predict([newdata])
    return{'prediction':prediction.tolist()}

# GET, POST, PUT, DELETE --> Methods

# How to return JSON https://flask.palletsprojects.com/en/1.1.x/quickstart/#apis-with-json
