# Data Science Midterm Project
> Meghan Barritt | Tashrif Mahmud

## Project/Goals
Our primary goal is to build a model that can confidently predict **Housing Prices** based on their typical features.

We will use a large amount of housing data which can be found in the [data](https://github.com/MeghanBarritt/midterm_project_housing_prices/tree/main/data) folder. We use this data to build and test our model.

## Process
### Importing and Compiling Data
- Developed a function to iterate through the data folder, extracting relevant information into a DataFrame. 
- Additionally, created a function to expand tags into columns with partial one-hot encoding, utilizing list comprehension for efficient processing.
- Conducted initial testing on two JSON files in a separate folder to verify that the functions produced the expected output.
- You can check the customer functions in [functions_importing.py](https://github.com/MeghanBarritt/midterm_project_housing_prices/blob/main/notebooks/functions_importing.py) script.

### Data Cleaning and EDA
- This process can be seen here in [1 - EDA.ipynb](https://github.com/MeghanBarritt/midterm_project_housing_prices/blob/main/notebooks/1%20-%20EDA.ipynb) notebook.
- Removed duplicate entries and dropped columns that were either entirely empty, contained a single constant value, or were mostly empty.
- Generated a list of keys to identify redundant or low-priority columns for merging or removal. 
- Columns with redundant tags (e.g., for garage spaces or bathrooms) and less essential features (like 'views' or nearby sports facilities) were excluded due to quantification challenges and time constraints.
- Merged redundant columns where applicable and removed others as planned.
- Standardized values in the 'property type' column, created a new column, and applied One-Hot Encoding to categorize property types.
- Identified and removed extreme outliers affecting the distribution after reviewing scatter plots.
- Imputed missing values for key columns ('year built', 'lot sqft', 'sqft') after the train/test split.
- Did some visualization like scatter plots to get a better understanding of our feature relationships.
- Saved our clean dataframe in [pickles](https://github.com/MeghanBarritt/midterm_project_housing_prices/tree/main/notebooks/pickles) subfolder for using it in our models. 

### Model Building and Selection
- We try four models in our project which are:
> 1. Linear Regression
> 2. Support Vector Machines (SVM)
> 3. Random Forest
> 4. XGBoost
- This whole process can be viewed in [2 - model_selection.ipynb](https://github.com/MeghanBarritt/midterm_project_housing_prices/blob/main/notebooks/2%20-%20model_selection.ipynb) notebook.
- We do some preprocessing before running each model fits.
- We also go over the some feature selection methods to find the best features that can determine Housing Prices.

### Hyperparameter tuning




## Results
- The model results is summarized below: 
> ```
> Linear Regression Metrics:
> Mean Squared Error (MSE): 145854509592.19656
> Root Mean Squared Error (RMSE): 381909.0331377311
> Mean Absolute Error (MAE): 169524.15612256597
> R-squared (R²): 0.5063865830193197
> Adjusted R-squared: 0.42967638983988965
> 
> Support Vector Machine Metrics:
> Mean Squared Error (MSE): 301342955363.1485
> Root Mean Squared Error (RMSE): 548947.1334865941
> Mean Absolute Error (MAE): 240273.5446929714
> R-squared (R²): -0.019830832078835847
> Adjusted R-squared: -0.17831805598297934
>
> Random Forest Metrics:
> Mean Squared Error (MSE): 118289368284.31741
> Root Mean Squared Error (RMSE): 343932.21466492116
> Mean Absolute Error (MAE): 132034.9503377065
> R-squared (R²): 0.5996749127979519
> Adjusted R-squared: 0.5374622303273633
>
> XGBoost Metrics:
> Mean Squared Error (MSE): 152373904869.29163
> Root Mean Squared Error (RMSE): 390351.0021369122
> Mean Absolute Error (MAE): 141338.50884600493
> R-squared (R²): 0.48432308297141446
> Adjusted R-squared: 0.4041841026223775
> ```

## Challenges 
- writing the import funtions was tricky; I (MB) had some issues getting the iterator to skip over None values rather than breaking, and then with the fact that the functions in the .py file needed to import modules internally. 

## Future Goals
(what would you do if you had more time?)
