'''
Question 1: Data Cleaning

Objective:
Perform data cleaning operations on the given movie watch dataset.

Tasks:
1. Remove duplicate records.
2. Replace NULL values in:
   - 'watch_time_min' → Replace with average watch time of that country.
   - 'rating' → Replace with average rating of that subscription type.

Approach to Solve:

Step 1: Identify and remove duplicates
- Use a method to drop duplicate rows from the dataset.
- This ensures that each record in the dataset is unique.

Step 2: Handle missing values in 'watch_time_min'
- Group the dataset by 'country' and compute the average watch time for each country.
- Join this average back to the main dataset.
- Replace any NULL values in 'watch_time_min' with the corresponding country's average value.

Step 3: Handle missing values in 'rating'
- Group the dataset by 'subscription_type' and calculate the average rating for each subscription type.
- Join this result back to the dataset.
- Replace any NULL values in 'rating' with the corresponding subscription type’s average value.

Step 4: Validate the results
- Ensure there are no remaining NULL values in 'watch_time_min' or 'rating'.
- Verify that the number of records matches expectations after duplicate removal.

Final Outcome:
- All duplicate rows are removed.
- Missing watch times are replaced with the country-wise average.
- Missing ratings are replaced with the subscription-type average.
- The final dataset is clean, consistent, and ready for further analysis or reporting.
'''
