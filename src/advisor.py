def giveSuggestion(salary, rent, food, lifestyle):
    rentPercent = (rent / salary) * 100
    foodPercent = (food / salary) * 100
    lifePercent = (lifestyle / salary) * 100

    adviceList = []

    # simple logic based on salary
    if salary > 100000:
        idealRent = 40
        idealFood = 25
    elif salary > 30000:
        idealRent = 35
        idealFood = 30
    else:
        idealRent = 30
        idealFood = 40

    if rentPercent > idealRent:
        adviceList.append("Try to reduce rent")

    if foodPercent > idealFood:
        adviceList.append("Food spending is high")

    if lifePercent > 25:
        adviceList.append("Cut down lifestyle expenses")

    if len(adviceList) == 0:
        return "You are managing money well 👍"

    return adviceList