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
- You can check the custom functions in [functions_importing.py](https://github.com/MeghanBarritt/midterm_project_housing_prices/blob/main/notebooks/functions_importing.py) script.

### Data Cleaning and EDA
- This process can be seen here in [1 - EDA.ipynb](https://github.com/MeghanBarritt/midterm_project_housing_prices/blob/main/notebooks/1%20-%20EDA.ipynb) notebook.
- Removed duplicate entries and dropped columns that were either entirely empty, contained a single constant value, or were mostly empty.
- Generated a list of keys to identify redundant or low-priority columns for merging or removal. 
- Columns with redundant tags (e.g., for garage spaces or bathrooms) and less essential features (like 'views' or nearby sports facilities) were excluded due to quantification challenges and time constraints.
- Merged redundant columns where applicable and removed others as planned.
- Standardized values in the 'property type' column, created a new column, and applied One-Hot Encoding to encode the categories numerically.
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
- The framework of this process can be viewed in [3 - tuning_pipeline.ipynb](https://github.com/MeghanBarritt/midterm_project_housing_prices/blob/main/notebooks/3%20-%20tuning_pipeline.ipynb)
- Started off by examining the documentation to see what parameters could be tuned for each model.
- Initiated models with fixed parameters such as random_state already in place
- Created parameter dictionaries to use with the GridSearch function during tuning.
- Created a GridSearch for each model.
- For each model, and for each of that model's hyperparameters, adjusted the values within the dictionary and reran the search. This process was done in stages, with a max of 5 values per parameter at a time in order to minimize processing time. Only the final value and one one either side is preserved in the notebook. 
- Initiated models using the optimized hyperparameters; saved these models in pickles. (or a .json, in the case of XGBoost.)
- Ran a final prediction with the optimized models.

## Results
- Random Forest performs the strongest with the lowest error and highest accuracy, explaining 60% of price variability. Cross-validated RMSE is around $237,415 ± $34,756, making it the most reliable choice.
- Linear Regression & XGBoost both show moderate accuracy, explaining about 50% of the variability with higher error rates than Random Forest. Cross-validated RMSEs are similar, around $252,473 for Linear Regression and $253,431 for XGBoost.
- Support Vector Machine performs poorly, with high errors and very low predictive accuracy, making it unsuitable for this task. 

## Challenges 
-  Writing the import functions was tricky, particularly with the iterator skipping `None` values and ensuring internal module imports in the `.py` file.
- The model was receiving a mix of NumPy and Pandas objects, so we passed it two NumPy arrays. We identified that `NaNs` in the test data were caused by encoding the average sale price per city.
- Data cleaning took a lot more time, as there were a huge chunk of missing and duplicate date mixed in.
- Hyperparameter tuning for XGBoost in particular was a challenge, as entering more than a few values at a time caused a huge increase in calculation time, which was not ideal when there was a large chance the parameters would need futher tuning.

## Future Goals
- Run the models again with the feature combinations selected in the stretch goals 'Feature Selection' area and then tune them to see how accurate a model could be achieved, and if the model that was most accurate would change.
- Build a pipeline for the cleaning process.
