def financialScore(salary, rent, food, lifeStyle):
    totalAmount = rent + food + lifeStyle
    ratioValue = totalAmount / salary

    scoreValue = 100

    if ratioValue > 0.9:
        scoreValue -= 40
    elif ratioValue > 0.7:
        scoreValue -= 25
    elif ratioValue > 0.5:
        scoreValue -= 10

    if rent > salary * 0.4:
        scoreValue -= 15

    if lifeStyle > salary * 0.25:
        scoreValue -= 15

    return max(scoreValue, 0)


def detailedReport(salary, rent, food, lifeStyle):
    reportList = []

    rentPercent = (rent / salary) * 100

    if rentPercent > 40:
        extraAmount = rent - (0.4 * salary)
        reportList.append(f"Reduce rent by ₹{int(extraAmount)}")

    if food > salary * 0.3:
        reportList.append("Food expenses are high")

    if lifeStyle > salary * 0.25:
        reportList.append("Lifestyle spending is too high")

    if len(reportList) == 0:
        return ["Your financial planning is excellent"]

    return reportList