"""
Flask application for emotion detection
"""

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Endpoint for detecting emotions in the provided text.
    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the labels and scores from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Please try again!"

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, "
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render index.html
    """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
