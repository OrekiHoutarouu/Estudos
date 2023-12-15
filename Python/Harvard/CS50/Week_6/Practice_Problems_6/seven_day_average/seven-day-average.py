import csv
import requests


def main():
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    new_cases = calculate(reader)

    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    comparative_averages(new_cases, states)


def calculate(reader):
    newCases = {}

    for row in reader:
        state = row["state"]
        date = row["date"]
        todayCases = int(row["cases"])

        if state not in newCases:
            newCases[state] = []

        if len(newCases[state]) >= 14:
            newCases[state].pop(0)

        newCases[state].append(todayCases)

    return newCases


def comparative_averages(new_cases, states):
    for state in states:
        recentCases = new_cases[state][7:]
        lastWeekCases = new_cases[state][:7]
        averageRecent = round(sum(recentCases) / 7)
        averageLastWeek = round(sum(lastWeekCases) / 7)
        difference = averageRecent - averageLastWeek

        if difference > 0:
            message = "an increase"

        else:
            message = "a decrease"

        try:
            d = difference / averageLastWeek
            percentage = round(d * 100, 2)

        except ZeroDivisionError:
            raise ZeroDivisionError

        print(
            f"{state} had a 7-day average of {averageRecent} and {message} of {percentage}%"
        )


main()
