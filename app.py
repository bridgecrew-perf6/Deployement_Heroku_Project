import joblib
from flask import Flask, request, json, jsonify
from werkzeug.exceptions import HTTPException

MODEL_PATH = "models/model.joblib"

app = Flask(__name__)

def make_prediction(fixed_acidity, volatile_acidit ,citric_acid,*
                    residual_sugar ,chlorides, free_sulfur_dioxide,	
                    total_sulfur_dioxide, density ,pH ,sulphates ,alcohol):
    """Return a prediction with our regression model.
    """
    # Load model
    regressor = joblib.load(MODEL_PATH)
    # Make prediction (the regressor expects a 2D array that is why we put year
    # in a list of list) and return it
    prediction = regressor.predict([[fixed_acidity, volatile_acidit ,citric_acid,*
                    residual_sugar ,chlorides, free_sulfur_dioxide,	
                    total_sulfur_dioxide, density ,pH ,sulphates ,alcohol]])
    return prediction[0]


@app.route("/predict", methods=["POST"])
def predict():
    # Check parameters
    if request.json:
        # Get JSON as dictionnary
        json_input = request.get_json()
        # Call our predict function that handle loading model and making a
        # prediction
        prediction = make_prediction(float(json_input[['fixed_acidity', 'volatile_acidit' ,'citric_acid',*
                    'residual_sugar' ,'chlorides', 'free_sulfur_dioxide',	
                    'total_sulfur_dioxide', 'density' ,'pH' ,'sulphates' ,'alcohol']]))
        # Return prediction
        response = {
            # Since prediction is a float and jsonify function can't handle
            # floats we need to convert it to string
            "prediction": str(prediction),
        }
        return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)