import pickle
import json

with open('pipe.pickle', 'rb') as f:
    pipe = pickle.load(f)

with open('testdata.json', 'r') as f:
    testdata = json.load(f)

pipe.predict([testdata])

# NOTE TO SELF: when I run python test_pickle.py , I get an error that SimpleImputer
# is expecting 23 features as input, but 24 in X
