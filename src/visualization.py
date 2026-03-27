import matplotlib.pyplot as plt


#  PIE CHART 
def showpiechart(userData):
    labels = ['Rent', 'Food', 'Travel', 'Lifestyle']
    values = [
        userData['rent'],
        userData['food'],
        userData['travel'],
        userData['lifestyle']
    ]

    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Your Expense Distribution")
    plt.show()


#  SCATTER PLOT -
def showscatter(dataFrame):
    plt.figure()
    plt.scatter(dataFrame['salary'], dataFrame['total_expense'])
    plt.xlabel("Salary")
    plt.ylabel("Total Expense")
    plt.title("Salary vs Expense")
    plt.show()


#  IDEAL VS ACTUAL BAR 
def comparebars(userData):
    labels = ['Rent', 'Food', 'Lifestyle']

    actualValues = [
        userData['rent'],
        userData['food'],
        userData['lifestyle']
    ]

    salary = userData['salary']

    idealValues = [
        0.4 * salary,
        0.3 * salary,
        0.25 * salary
    ]

    xAxis = range(len(labels))

    plt.figure()
    plt.bar(xAxis, idealValues, label="Ideal")
    plt.bar(xAxis, actualValues, bottom=idealValues, label="Actual")

    plt.xticks(xAxis, labels)
    plt.title("Ideal vs Actual Spending")
    plt.legend()
    plt.show()


#  TREND LINE 
def showtrend(dataFrame):
    plt.figure()
    plt.plot(dataFrame['salary'], dataFrame['total_expense'], marker='o')
    plt.xlabel("Salary")
    plt.ylabel("Expense")
    plt.title("Expense Trend")
    plt.show()


#  CATEGORY AVERAGE 
def categorybars(dataFrame):
    avgValues = dataFrame[['rent', 'food', 'travel', 'lifestyle']].mean()

    plt.figure()
    avgValues.plot(kind='bar')
    plt.title("Average Spending by Category")
    plt.ylabel("Amount")
    plt.show()