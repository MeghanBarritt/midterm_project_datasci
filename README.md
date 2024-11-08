# Data Science Midterm Project
> Meghan Barritt | Tashrif Mahmud

## Project/Goals

## Process
### Importing and compiling data from .json files
- wrote one funcition to iterate through the data folder and extract information into a dataframe, and another to expand the tags list into columns, with partial One-Hot encoding applied, using list comprehension. 
- initial testing of functions done on two .jsons in a separate folder to ensure the expected output was being produced

### Column thinning, data cleaning
- dropped duplicated data
- removed columns that were completely empty, all contained the same value, or where almost completely empty. 
- extracted list of keys to identify redundant columns that could be merged into a single feature, such as redundant tags for garage spaces and bathrooms, as well as features like 'views' or nearby sporting facilities, which, while potentially interesting, are difficult to group and quantify, and were not high priority to include. It was decided that these features would be dropped for time consideration.
- merged redundant columns where appropriate, dropped others as decided
- cleaned up values for 'property type' in new column and then applies OneHotEncoding to those categories
- ran scatter plots, discovered some huge outliers that were having an outsized impact on the distribution; removed them
- imputed some missing values after train/test split: year built, lot sqft, sqft

### Model building

### Hyperparameter tuning




## Results
(fill in how your model performed)

## Challenges 
- writing the import funtions was tricky; I (MB) had some issues getting the iterator to skip over None values rather than breaking, and then with the fact that the functions in the .py file needed to import modules internally. 

## Future Goals
(what would you do if you had more time?)
