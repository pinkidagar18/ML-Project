# 📊 Student Performance Predictor

> An end-to-end machine learning application that predicts student mathematics scores based on demographic and academic variables using regression models.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-endpoints)

</div>

---

## 🎯 Overview

This project implements a **machine learning regression model** to predict student mathematics performance based on various socioeconomic and academic factors. The model analyzes demographic variables, parental education levels, test preparation, and other academic scores to provide accurate predictions.

### Key Highlights
- 🎨 **Modern UI/UX**: Beautiful, responsive web interface with editorial-style design
- 🤖 **ML Pipeline**: End-to-end automated pipeline for data ingestion, transformation, and prediction
- 📈 **High Accuracy**: Optimized model selection with 92%+ accuracy
- 🚀 **Production Ready**: Flask-based REST API with error handling and logging
- 📊 **Data Visualization**: Interactive insights and feature importance analysis

---

## 🖼️ Demo

### Landing Page
Clean, modern landing page with feature highlights and impact analysis.

![Landing Page](screenshots/Landing_Page.png)

### Prediction Interface
Interactive form with real-time score prediction and confidence intervals.

![Prediction Interface](screenshots/Prediction_Interface.png)

---

## ✨ Features

### Machine Learning
- ✅ Multiple regression model comparison (Linear, Ridge, Lasso, XGBoost, CatBoost)
- ✅ Automated hyperparameter tuning
- ✅ Data preprocessing pipeline with encoding and scaling
- ✅ Feature engineering and selection
- ✅ Model persistence and versioning

### Web Application
- ✅ RESTful API with Flask
- ✅ Real-time predictions
- ✅ Input validation and error handling
- ✅ Beautiful, responsive UI
- ✅ Animated visualizations

### Analysis Variables
- 📌 **Gender**: Male/Female
- 📌 **Race/Ethnicity**: Groups A-E
- 📌 **Parental Education**: From some high school to master's degree
- 📌 **Lunch Type**: Standard or Free/Reduced
- 📌 **Test Preparation**: None or Completed
- 📌 **Reading Score**: 0-100
- 📌 **Writing Score**: 0-100

---

## 🏗️ Project Structure

```
ML-Project/
├── artifacts/                      # Trained models and preprocessors
│   ├── model.pkl                   # Trained ML model
│   ├── preprocessor.pkl            # Data preprocessing pipeline
│   ├── data.csv                    # Original dataset
│   ├── train.csv                   # Training data
│   └── test.csv                    # Test data
│
├── notebook/                       # Jupyter notebooks for EDA
│   ├── 1_EDA_STUDENT_PERFORMANCE.ipynb
│   └── 2_MODEL_TRAINING.ipynb
│
├── src/                           # Source code
│   ├── components/                # ML pipeline components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py     # Data loading and splitting
│   │   ├── data_transformation.py # Feature engineering
│   │   └── model_trainer.py       # Model training and evaluation
│   │
│   ├── pipeline/                  # Prediction pipelines
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py   # Inference pipeline
│   │   └── train_pipeline.py     # Training pipeline
│   │
│   ├── exception.py              # Custom exception handling
│   ├── logger.py                 # Logging configuration
│   └── utils.py                  # Helper functions
│
├── templates/                     # HTML templates
│   ├── index.html                # Landing page
│   └── home.html                 # Prediction interface
│
├── screenshots/                   # Application screenshots
│   ├── Landing_Page.png          # Landing page screenshot
│   └── Prediction_Interface.png  # Prediction page screenshot
│
├── app.py                        # Flask application
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
├── .gitignore                    # Git ignore file
└── README.md                     # Documentation
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/pinkidagar18/ML-Project.git
cd ML-Project
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Verify artifacts folder**
```bash
# Ensure these files exist:
artifacts/
├── model.pkl
└── preprocessor.pkl
```

5. **Run the application**
```bash
python app.py
```

6. **Access the application**
Open your browser and navigate to:
```
http://localhost:5000
```

---

## 📖 Usage

### Web Interface

1. **Navigate to the homepage**
   - View project overview and feature analysis
   - Understand the impact of different variables

2. **Click "Launch Prediction Engine"**
   - Fill in the student profile form
   - Adjust reading and writing scores using sliders

3. **Generate Prediction**
   - Click submit to get math score prediction
   - View confidence level and percentile ranking

### Example Input
```
Gender: Male
Race/Ethnicity: Group B
Parental Education: Bachelor's Degree
Lunch: Standard
Test Preparation: Completed
Reading Score: 72
Writing Score: 74
```

### Example Output
```
Predicted Math Score: 68.5
Confidence Level: High (92%)
Score Range: 63.5 - 73.5
Percentile: 50th-75th
```

---

## 🔌 API Endpoints

### `GET /`
**Landing Page**
- Returns: HTML landing page with project information

### `GET /predictdata`
**Prediction Form**
- Returns: HTML form for input data

### `POST /predictdata`
**Generate Prediction**
- Content-Type: `application/x-www-form-urlencoded`
- Body Parameters:
  ```
  gender: string
  race_ethnicity: string
  parental_level_of_education: string
  lunch: string
  test_preparation_course: string
  reading_score: float
  writing_score: float
  ```
- Returns: HTML page with prediction result

### Example cURL Request
```bash
curl -X POST http://localhost:5000/predictdata \
  -d "gender=male" \
  -d "race_ethnicity=group B" \
  -d "parental_level_of_education=bachelor's degree" \
  -d "lunch=standard" \
  -d "test_preparation_course=completed" \
  -d "reading_score=72" \
  -d "writing_score=74"
```

---

## 🧪 Model Details

### Algorithms Evaluated
- Linear Regression
- Ridge Regression
- Lasso Regression
- K-Neighbors Regressor
- Decision Tree
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

### Best Model
**Random Forest Regressor** with optimized hyperparameters:
- R² Score: 0.92+
- RMSE: ~5.2
- MAE: ~4.1

### Feature Importance
1. **Reading & Writing Proficiency** (+12.4 avg influence)
2. **Test Preparation Course** (+8.2 avg influence)
3. **Parental Education Level** (+7.5 avg influence)
4. **Lunch Type** (+5.1 avg influence)
5. **Gender & Ethnicity** (baseline factors)

---

## 📊 Dataset

### Source
Student Performance Dataset with 1,000 student records

### Features (8)
- Gender (categorical)
- Race/Ethnicity (categorical)
- Parental Education Level (ordinal)
- Lunch Type (categorical)
- Test Preparation Course (categorical)
- Reading Score (numerical)
- Writing Score (numerical)
- Math Score (target - numerical)

### Data Split
- Training: 80% (800 records)
- Testing: 20% (200 records)

---

## 🛠️ Technologies Used

### Backend
- **Python 3.8+**: Core programming language
- **Flask**: Web framework
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **XGBoost**: Gradient boosting
- **CatBoost**: Categorical boosting

### Frontend
- **HTML5**: Markup
- **CSS3**: Styling with custom animations
- **Google Fonts**: Typography (Archivo, Fraunces)
- **Responsive Design**: Mobile-first approach

### Development Tools
- **Jupyter Notebook**: EDA and experimentation
- **VS Code**: IDE
- **Git**: Version control

---

## 📈 Performance Metrics

| Model | R² Score | RMSE | MAE | Training Time |
|-------|----------|------|-----|---------------|
| Linear Regression | 0.88 | 6.2 | 4.9 | 0.02s |
| Ridge Regression | 0.88 | 6.1 | 4.8 | 0.02s |
| Random Forest | **0.92** | **5.2** | **4.1** | 1.2s |
| XGBoost | 0.91 | 5.4 | 4.3 | 0.8s |
| CatBoost | 0.90 | 5.6 | 4.5 | 2.1s |

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
PORT=5000
```

### Debug Mode
```python
# In app.py
app.run(host="0.0.0.0", port=5000, debug=True)  # Development
app.run(host="0.0.0.0", port=5000, debug=False) # Production
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `FileNotFoundError: artifacts/model.pkl`
```bash
# Solution: Ensure model files are in artifacts folder
mkdir artifacts
# Place model.pkl and preprocessor.pkl in artifacts/
```

**Issue**: `ModuleNotFoundError: No module named 'src'`
```bash
# Solution: Install the package in editable mode
pip install -e .
```

**Issue**: Port 5000 already in use
```bash
# Solution: Use a different port
# Edit app.py: app.run(port=5001)
```
---


## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Add docstrings to functions and classes
- Write unit tests for new features
- Update documentation as needed

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Pinki**
- Email: pinkidagar18@gmail.com
- GitHub: [@pinkidagar18](https://github.com/pinkidagar18)
- Project Link: [https://github.com/pinkidagar18/ML-Project](https://github.com/pinkidagar18/ML-Project)

---

## 🙏 Acknowledgments

- Dataset source: Student Performance Dataset
- Inspiration: End-to-end ML project implementation
- UI Design: Modern editorial-style web aesthetics
- Icons: Emoji icons for visual appeal

---

## 📞 Support

For support, email pinkidagar18@gmail.com or open an issue on GitHub.

### Quick Links
- [Report Bug](https://github.com/pinkidagar18/ML-Project/issues)
- [Request Feature](https://github.com/pinkidagar18/ML-Project/issues)
- [View Documentation](https://github.com/pinkidagar18/ML-Project)

---

<div align="center">

### ⭐ Star this repo if you found it helpful!

Made with ❤️ by [Pinki](https://github.com/pinkidagar18)

</div>
