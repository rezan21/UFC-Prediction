# UFC-Prediction
## Predicting Fight's Winner with Machine Learning and AI

[ai-predicts-ufc](https://ai-predicts-ufc.herokuapp.com)

This project consists of a number of jupyter notebooks which provide the following:

1. __Data Preprocessing and Exploratory Data Analysis (EDA):__
    - Used libraries: `pandas`, `NumPy`, `missingno`
    
2. __Visualisations:__
    - `Plotly` for Interactive plots and `Seaborn`/`Matplotlib` for regular charts
    
3. __Construction of DNN with Hyper-parameters tuning:__
    - `Keras`/`keras-tuner` and `Tensorflow`
    
4. __Ensemble Method (Combining different ML models):__
    - `Tensorflow`/`Keras` and `Scikit-Learn`
    
5. App Development and Deployment (in progress...)

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
Used models separately and then combined them into one ensembled model:

- __Deep Neural Network (DNN)__
- __Support Vector Machine (SVM)__
- __Random Forest (RF)__

### Backend Data API and Development (in progress)
Generated the latest fighter details and used trained models to predict matches

__© TheDeepestLearners__



