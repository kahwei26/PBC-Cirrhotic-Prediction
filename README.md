## Cirrhotic Stage Prediction of Primary Biliary Cholangitis (PBC) using Random Forest, Support Vector Machine and Extreme Gradient Boosting based on Novel Hybrid Feature Selection
### About
This repository contains the code for my final-year project, which do prediction of the end-stage PBC using machine laerning algorithms. Other than that, this project also introduce a novel hybrid feature selection method, that is, Ensemble Filter Feature Selection with Binary Particle Swarm Optimization (EF-BPSO).

### Dataset 
The dataset that is used in this study is the clinical dataset which was gathered from the Mayo Clinic trial on Primary Biliary Cholngitis (PBC) that was undertaken between 1974 and 1984. 
Link of dataset: https://www.kaggle.com/datasets/fedesoriano/cirrhosis/prediction-dataset. 

### Feature Selection
Feature selection is one of the focuses in this study. A novel hybrid feature selection is proposed.
**Working principle:**
1) Initially, the dataset undergoes four different types of filter feature selection, including Information Gain (IG), Chi-Square, Fisher Score and ReliefF. These methods identify the top-N features closely correlated with the target variables.
2) Then, take the union set of the selected features of all the filter feature selection.
3) From the union set of features, perform another round of feature selection using a wrapper feature selection, that is, BPSO using different classifers. BPSO will determine the feature subset yielding the highest accuracy.

**Explanation:**
Wrapper feature selection can efffectivly select the features which can produce high accuracy. However, its effectiveness can be further enhanced by initially eliminating irrelevant features, as it is able to increase the possibility of getting an optimal feature subset. Typically, in hybrid feature selection methods, people conduct filter feature selection before employing wrapper or embedded feature selection techniques. In this approach, an ensemble feature selection which combined multiple filter feature selection methods is used to combine their strenghts to create a better feature space before doing wrapper feature selection.

### Data Mining
**Data Preprocessing**
- The original dataset includes missing values that are missing completely at random (MCAR). There are a total of 12 features out of 16 features having missing values, and the percentage of the missing values are up to 32.536%. KNN imputation is used to address this issue.
- Normalization is done using MinMax scaler to scale the data to 0-1.
- First round feature selection to get the top-N features using ensemble filter feature selection.
</br＞
**Data Spliting**
- Dataset is split into 90% training, 10% testing.
- Upsampling techniques, SMOTE, is used to balanced the classes for training data.
</br＞
**Model Traning**
- Using BPSO, train models using RF, SVM and XGBoost with the optimal feature subset.
</br＞
**Prediction**
- Utilize the trained models to do cirrhotic stage prediction using the testing set
</br＞
**Model Evaluation**
- Based on the result, evaluate the performance of model in terms of accuracy, precision, recall and f1-score.

### Result
EF-BPSO seems to produce a better outcome compared to single feature selection method.
Random forest, with the features subset **Alk_Phos, Prothrombin, Ascites, Sex, Age, Copper, Hepatomegaly**, achieved best performance: <br>
Accuracy 95.24%, 
Precision: 94.12%, 
Recall: 94.12%, 
F1-Score: 94.12%

### Implementation
The model is then implemented into a web application using Flask. This application facilitates the prediction of the PBC cirrhotic stage through a webpage, where users can input all required clinical information, as illustrated in figure below, to get prediction of PBC cirrhotic stage.
![webpage](https://github.com/kahwei26/PBC-Cirrhotic-Prediction/blob/847081174d506b915252b9a11abba45b69d0a5d0/img/Screenshot%202024-07-22%20231617.png?raw=true)
![result](https://github.com/kahwei26/PBC-Cirrhotic-Prediction/blob/df96f692f371370a9f87aca99d33fc585827d2a0/img/Screenshot%202024-07-22%20232137.png?raw=true)
