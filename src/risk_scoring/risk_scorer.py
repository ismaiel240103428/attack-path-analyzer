def calculate_risk(severity):

    risk_scores = {
        "Critical": 10,
        "High": 8,
        "Medium": 5,
        "Low": 2
    }

    return risk_scores.get(severity, 0)


def get_risk_level(score):

    if score >= 9:
        return "Critical"

    elif score >= 7:
        return "High"

    elif score >= 4:
        return "Medium"

    elif score > 0:
        return "Low"

    else:
        return "Unknown"


def score_vulnerabilities(vulnerabilities):

    scored_vulnerabilities = []

    for vulnerability in vulnerabilities:

        score = calculate_risk(
            vulnerability["Severity"]
        )

        risk_level = get_risk_level(score)

        result = vulnerability.copy()

        result["Risk Score"] = score
        result["Risk Level"] = risk_level

        scored_vulnerabilities.append(result)

    return scored_vulnerabilities