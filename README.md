# New-Heart-Disease

![Capture](https://github.com/MKT17/New-Heart-Disease/assets/152396111/39e44c56-91ef-4d87-8686-d60cabf3e493)

### 1. Data Used

- **Source:** The heart disease dataset loaded from `heart.csv`.
- **Attributes:** The dataset includes the following features:
  - `age`: Age of the patient.
  - `sex`: Sex of the patient (0 = female, 1 = male).
  - `cp`: Chest pain type (4 values: 0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic).
  - `trestbps`: Resting blood pressure (in mm Hg on admission to the hospital).
  - `chol`: Serum cholesterol in mg/dl.
  - `fbs`: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false).
  - `restecg`: Resting electrocardiographic results (values 0, 1, 2).
  - `thalach`: Maximum heart rate achieved.
  - `exang`: Exercise-induced angina (1 = yes, 0 = no).
  - `oldpeak`: ST depression induced by exercise relative to rest.
  - `slope`: Slope of the peak exercise ST segment.
  - `ca`: Number of major vessels (0-3) colored by fluoroscopy.
  - `thal`: Thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect).
  - `target`: Presence of heart disease (1 = yes, 0 = no).

### 2. The Analysis Made

- **Exploratory Data Analysis (EDA):**
  - Initial inspection of the dataset using `.head()`, `.tail()`, `.shape`, and `.info()`.
  - Checking for missing values with `.isnull().sum()`.
  - Identifying and removing duplicate rows using `.duplicated()` and `.drop_duplicates()`.
  - Generating descriptive statistics with `.describe()`.
  - Correlation analysis using `.corr()`.
  - Distribution of the target variable and categorical features using `sns.countplot`.
  - Age distribution with `sns.distplot`.
  - Histograms for continuous features and FacetGrid for distributions based on sex.
  - Histograms for blood pressure (`trestbps`) and cholesterol (`chol`).
  - Histograms for continuous variables.

- **Machine Learning Models:**
  - **Data Preprocessing:**
    - Encoding categorical variables with `pd.get_dummies()`.
    - Feature scaling using `StandardScaler`.
    - Splitting the dataset into training and testing sets using `train_test_split`.
  - **Model Training and Evaluation:**
    - Logistic Regression
    - K-Nearest Neighbors (KNN)
    - Decision Tree Classifier
    - Random Forest Classifier
    - Gradient Boosting Classifier
  - **Model Performance:**
    - Evaluation of each model using `accuracy_score`.

### 3. The Findings

- **Model Performance:**
  - Logistic Regression achieved the highest accuracy of 90.16%.
  - K-Nearest Neighbors and Random Forest both achieved an accuracy of 86.89%.
  - Gradient Boosting Classifier achieved an accuracy of 85.25%.
  - Decision Tree Classifier had the lowest accuracy at 81.97%.

### 4. The Summary

The analysis included a comprehensive exploration of the heart disease dataset, involving the examination of data distributions, correlation among features, and the relationship between categorical features and the target variable. The dataset was preprocessed to encode categorical variables and scale continuous variables. Several machine learning models were trained and evaluated, with Logistic Regression performing the best in terms of accuracy.

### 5. The Limitations

- **Data Quality:** The analysis assumed that the dataset had no missing values or erroneous data, but further investigation might be necessary to confirm data quality.
- **Model Evaluation:** Only accuracy was used to evaluate model performance. Other metrics such as precision, recall, F1-score, and ROC-AUC could provide a more comprehensive evaluation.
- **Generalizability:** The dataset may not be representative of the broader population, and the model’s generalizability to other datasets or real-world data may be limited.
