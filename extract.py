def extract_latest_hours(dataset):
    latest_hours_worked = {}

    for (country, year), hours in dataset.items():
        if country not in latest_hours_worked or year > latest_hours_worked[country][0]:
            latest_hours_worked[country] = (year, hours)

    result_dict = {country: hours for country, (year, hours) in latest_hours_worked.items()}
    return result_dict

import hours_worked as d
latest_hours = extract_latest_hours(d.hours_worked)
print(latest_hours)
