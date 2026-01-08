from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Configuration
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def index():
    """Landing page"""
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    """Prediction interface and processing"""
    if request.method == "GET":
        return render_template('home.html')
    else:
        try:
            # Collect form data
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score', 0)),
                writing_score=float(request.form.get('writing_score', 0))
            )

            # Get prediction
            pred_df = data.get_data_as_data_frame()
            print("=" * 50)
            print("Input Data:")
            print(pred_df)
            print("=" * 50)

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            print("Prediction Result:", results[0])
            print("=" * 50)

            return render_template('home.html', results=results[0])
        
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return render_template('home.html', error=str(e))


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🚀 StudyMetrics - Student Performance Predictor")
    print("=" * 60)
    print("\n📍 Application starting...")
    print("   → Local:   http://localhost:5000")
    print("   → Network: http://0.0.0.0:5000")
    print("\n📄 Available routes:")
    print("   → Home:       http://localhost:5000/")
    print("   → Predictor:  http://localhost:5000/predictdata")
    print("\n💡 Press CTRL+C to stop the server")
    print("=" * 60 + "\n")
    
    app.run(host="0.0.0.0", port=5000, debug=True)