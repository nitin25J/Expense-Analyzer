# AI Financial Health Analyzer

# About the Project

Honestly this came from something I noticed in my own life. Every month money just disappears and you have no idea where it went. You earn, you spend, and somehow the balance is always lower than you expected. That got me thinking and I decided to build something around it using Python and a few ML concepts I was learning at the time.

It is not trying to be a big system. You put in your salary and expenses, it looks at the numbers and tells you how you are doing financially. A score, some advice, and a few graphs to make it all make sense.


# Problem

Most people do not track their expenses properly. Even if they do they usually do not sit down and actually analyze them. Because of that:
- Money gets spent on things that do not really matter
- Very little ends up being saved
- There is no clear plan for finances



# Solution

This project tries to fix that by doing a few things:
- Taking your salary and expense details as input
- Looking at your spending pattern
- Predicting what your expenses might look like
- Giving you suggestions on where to cut back
- Showing graphs so the data actually means something



# Concepts Used

This project uses concepts learned in AI & ML:

- Clustering (K-Means) 
  Groups users based on spending habits

- Regression (Linear Regression) 
  Predicts total expense based on salary

- Rule-based Logic (AI)  
  Calculates financial score and gives suggestions



# Technologies and Libraries

- Python 3.8 or above
- Pandas (datahandling)  
- Matplotlib (visualization)  
- Scikit-learn (ML models)  



# Features

  - Expense Prediction  
  - Financial Health Score (0–100)  
  - Smart Suggestions based on spending  
  - Multiple Visualizations:
  - Pie chart (expense vs distribution)
  - Scatter plot (salary vs expense)
  - Bar chart (ideal vs actual)
  - Trend graph
  - Category comparison  



# Project Structure

Expense-Analyzer
  ├── data/
  │     └── expenses.csv
  ├── advisor.py
  ├── clustering.py
  ├── intelligence.py
  ├── preprocessing.py
  ├── regression.py
  ├── visualization.py
  ├── main.py
  ├── Project Report.pdf
  └── README.md



# How to Run the Project

1. Download or clone the project and open the root folder:

cd Expense-Analyzer


2. Make sure Python 3.8 or above is installed on your system before going further.

3. Install required libraries:

pip install pandas matplotlib scikit-learn


4. Make sure your folder structure is correct.

5. Open the data/ folder and make sure expenses.csv is placed there.
   The file should have columns for salary and the different expense categories.
   No other configuration is needed.

6. Run the main file from the root Expense-Analyzer/ directory:

python main.py


7. Enter your monthly details when prompted.



# Example Flow

- User enters salary and expenses  
- Data is processed and cleaned  
- Clustering groups similar spending patterns  
- Regression predicts total expense  
- Financial score is calculated  
- Suggestions are generated  
- Graphs are displayed for visualization  



# Output

The program provides:
- Estimated monthly expense  
- Financial health score  
- Personalized advice  
- Visual graphs for analysis  



# Challenges Faced

Building this was not smooth the whole way. A few things that gave me trouble:
- Folder structure was causing import errors that took time to figure out
- Getting the dataset into the right format was confusing at first
- Function names were not matching across files which broke things
- Understanding how the ML models actually behave took some trial and error

Got through all of it eventually, just took some patience.



# Conclusion

This project is a good example of how basic ML can actually be useful in day to day life. It is not trying to impress anyone with complexity. The goal was just to solve a real problem and understand the concepts while doing it.



# Future Improvements

- Add a graphical interface (GUI)  
- Use real-world financial datasets  
- Improve prediction accuracy  
- Convert into a web or mobile app  



# Final Note

This was built as part of learning. The priority was always understanding what I was doing and why, not just making something that works without knowing how.