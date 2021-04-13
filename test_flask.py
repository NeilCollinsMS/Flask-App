import requests
import json

# Load test data
with open('testdata.json', 'r') as f:
    testdata = json.load(f)


r = requests.post('http://127.0.0.1:5000/predict', json = {'newdata': testdata})
import pdb; pdb.set_trace()
data = r.json()
prediction = data['prediction']
print(prediction)
