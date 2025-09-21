from flask import Flask, request, render_template
from src.exception import CustomException
from src.logger import logging

from src.pipeline.predict_pipeline import CustomData, PredictionPipeline

application = Flask(__name__)
app = application

# Setup logging
logging.basicConfig(level=logging.INFO)


## Route for home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Collect user input from form
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            logging.info(f"Input Data: \n{pred_df}")

            # Run prediction
            predict_pipeline = PredictionPipeline()
            results = predict_pipeline.predict(pred_df)
            logging.info(f"Prediction Results: {results}")

            # Send results back to template
            return render_template('home.html', results=results[0])

        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            return render_template('home.html', results="Error occurred during prediction.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
