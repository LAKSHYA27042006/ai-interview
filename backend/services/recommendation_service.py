def get_recommendation(score):
    """
    Generate recommendation based on overall interview score
    """

    if score >= 85:
        return "Highly Recommended"

    elif score >= 70:
        return "Recommended"

    elif score >= 50:
        return "Consider"

    else:
        return "Not Recommended"