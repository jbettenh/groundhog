CHANCES = [
    "Outlook Good",
    "Signs Point to Yes",
    "Don’t Count on It ",
    "My Sources Say No",
    "Ask Again Later",
    "Sorry Canada",
]


def chances(country: str):
    answer = ""

    if country.lower() == "canada":
        answer = CHANCES[5]
    elif (
        country.lower() == "usa"
        or country.lower() == "united states"
        or country.lower() == "united states of america"
        or country.lower() == "america"
    ):
        answer = CHANCES[0]
        # answer = CHANCES[1]
        # answer = CHANCES[2]

    elif country == "":
        answer = CHANCES[3]
    else:
        answer = CHANCES[4]

    return answer
