# UFC-Prediction
## Predicting Fight's Winner with Machine Learning and AI

This project consists of a number of jupyter notebooks which provide the following:

1. __Data Preprocessing and Exploratory Data Analysis (EDA):__
    - Used libraries: `pandas`, `NumPy`, `missingno`
    
2. [__Visualisations:__ ](https://nbviewer.jupyter.org/github/rezan21/UFC-Prediction/blob/master/Visualisation.ipynb)
    - `Plotly` for Interactive plots and `Seaborn`/`Matplotlib` for regular charts
    
3. __Construction of DNN with Hyper-parameters tuning:__
    - `Keras`/`keras-tuner` and `Tensorflow`
    
4. __Ensemble Method (Combining different ML models):__
    - `Tensorflow`/`Keras` and `Scikit-Learn`
    
5. __App Development and Deployment__

---

### Introduction
The aim is __Data-driven decision making (DDDM)__ approach towards discovering recurring patterns in the data to predict the outcome of a sporting event in the future.

🥊 __The Ultimate Fighting Championship (UFC)__ is currently one of the fastest-growing sports in the world (Telegraph, 2017) and organises events weekly.

### Dataset
The original dataset, `data.csv`, found on Kaggle, contains the list of all UFC fights from 1993 to 2019. Each row represents information on match details, two fighters (blue and red), and the winner.
E.g: Demographics, body attributes, player current form, match details

- __Dimensions: 5144 rows x 145 columns__
- 9 categorical, 136 numerical features
- Target (categorical: Blue/Red) specifies the winner
- High dimensions
- Baseline - 67% (Similar Features Considered)

### Data Preprocessing
Performed tasks:

- Feature Selection
- Replacing empty string with NA
- Removing 'Draw' matches (Binary classification)
- Distinguishing numeric & symbolic fields
- Removing constant columns (due to no variation in them)
- Formating data to 3 Decimal Points
- 1-hot-encoding categorical fields
- Dimensionality Reduction with PCA (Principal Component Analysis)
- __Missing Values Treatment__
  - Replacing missings with Median
  - Prediction Missings via Linear Regression
  - Dropping Remaining Missings
  
### ML Models and Ensemble Method
Trained multiple models separately and then combined them into one ensembled model to increase performance:

- __Deep Neural Network (DNN)__
- __Support Vector Machine (SVM)__
- __Dicision Tree (DT)__
- __AdaBoost__
- __Random Forest (RF)__
- __ExtraTrees__
- __GradientBoosting__
- __Multi-Layer Perceptron (MLP)__
- __K-Nearest-Neighbours (KNN)__
- __Logistic Regression__
- __Linear Discriminant Analysis (LDA)__
- __XGB__

### Backend Data API and Development
Generated the latest fighter details and used trained models to predict matches. App deployed on heroku and available on (https://ai-predicts-ufc.herokuapp.com)

__© TheDeepestLearners__



