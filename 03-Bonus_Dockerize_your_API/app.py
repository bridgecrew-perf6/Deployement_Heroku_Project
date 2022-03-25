import joblib
from flask import Flask, request, json, jsonify, render_template
from werkzeug.exceptions import HTTPException

MODEL_PATH = "models/regressor_model.joblib"

app = Flask(__name__)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors (which is the basic error
    response with Flask).
    """
    # Start with the correct headers and status code from the error
    response = e.get_response()
    # Replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


class MissingKeyError(HTTPException):
    # We can define our own error for the missing key
    code = 422
    name = "Missing key error"
    description = "JSON content missing key 'year'."


class MissingJSON(HTTPException):
    # We can define our own error for missing JSON
    code = 400
    name = "Missing JSON"
    description = "Missing JSON."


def make_prediction(year: float):
    """Return a prediction with our regression model.
    """
    # Load model
    regressor = joblib.load(MODEL_PATH)
    # Make prediction (the regressor expects a 2D array that is why we put year
    # in a list of list) and return it
    prediction = regressor.predict([[year]])
    return prediction[0]


@app.route("/predict", methods=["POST"])
def predict():
    # Check parameters
    if request.json:
        # Get JSON as dictionnary
        json_input = request.get_json()
        if "year" not in json_input:
            # If 'year' is not in our JSON we raise our own error
            raise MissingKeyError()
        # Call our predict function that handle loading model and making a
        # prediction
        prediction = make_prediction(float(json_input["year"]))
        if "rounded" in json_input:
            # If rounded is present in the request and is True then we round
            # the prediction
            if json_input["rounded"] in ["True", "true", "T", "t"]:
                prediction = round(prediction)
        # Return prediction
        response = {
            # Since prediction is a float and jsonify function can't handle
            # floats we need to convert it to string
            "prediction": str(prediction),
        }
        return jsonify(response), 200
    raise MissingJSON()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # We change debug mode to False for production
    # We add host="0.0.0.0" so Flask will listen to all IP connection not only
    # localhost (default behaviour)
    app.run(host="0.0.0.0", debug=False)
