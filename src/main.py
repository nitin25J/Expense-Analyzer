from preprocessing import loaddata, preprocessdata
from clustering import clustering
from regression import trainmodel, predictexpense
from visualization import showpiechart, showscatter, comparebars, showtrend, categorybars
from advisor import giveSuggestion
from intelligence import financialScore, detailedReport

def main():
    dataFrame = loaddata('data/expenses.csv')
    dataFrame = preprocessdata(dataFrame)

    dataFrame, model = clustering(dataFrame)

    regModel = trainmodel(dataFrame)

    print("Enter your monthly details:")
    salary = int(input("Salary: "))
    rent = int(input("Rent: "))
    food = int(input("Food: "))
    travel = int(input("Travel: "))
    lifeStyle = int(input("Lifestyle: "))

    userData = {
        "salary": salary,
        "rent": rent,
        "food": food,
        "travel": travel,
        "lifestyle": lifeStyle
    }

    result = predictexpense(regModel, salary)
    print("\nEstimated Expense:", int(result))

    suggestion = giveSuggestion(salary, rent, food, lifeStyle)
    print("\nAdvice:", suggestion)

    score = financialScore(salary, rent, food, lifeStyle)

    print("\n💰 Financial Health Score:", score, "/100")

    if score > 80:
        print("🟢 Excellent financial condition")
    elif score > 60:
        print("🟡 Average condition")
    else:
        print("🔴 Poor financial health")

    reportList = detailedReport(salary, rent, food, lifeStyle)

    print("\n📊 Detailed Suggestions:")
    for item in reportList:
        print("-", item)

    # ================= VISUAL ANALYSIS =================
    print("\n========== VISUAL ANALYSIS ==========")

    print("\n📊 Showing Expense Distribution...")
    showpiechart(userData)

    print("\n📈 Showing Salary vs Expense...")
    showscatter(dataFrame)

    print("\n📊 Comparing Ideal vs Actual Spending...")
    comparebars(userData)

    print("\n📉 Showing Expense Trend...")
    showtrend(dataFrame)

    print("\n📊 Category-wise Average Spending...")
    categorybars(dataFrame)


if __name__ == "__main__":
    main()