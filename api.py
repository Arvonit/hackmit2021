import requests

r = requests.Session()

# Not very secure, but it's whatever
COVID_ACT_NOW_KEY = "0eae9d95ef3642d78fc9eab79e92b570"

us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))


def vaccines(state):
    response = r.get(
        f"https://api.covidactnow.org/v2/state/{state}.json?apiKey={COVID_ACT_NOW_KEY}"
    ).json()
    # vaccination = response["metrics"]["vaccinationsInitiatedRatio"]
    vaccination = response["metrics"]["vaccinationsCompletedRatio"]
    return f"Percentage of population vaccinated in {state}: {round(vaccination * 100, 2)}%"


def total_cases():
    total = 0
    response = r.get(
        f"https://api.covidactnow.org/v2/country/US.json?apiKey={COVID_ACT_NOW_KEY}"
    ).json()
    cases = response["actuals"]["positiveTests"]
    return f"Total number of cases in the US: {cases}"


def total_vaccines():
    response = r.get(
        f"https://api.covidactnow.org/v2/country/US.json?apiKey={COVID_ACT_NOW_KEY}"
    ).json()
    vaccination = response["metrics"]["vaccinationsCompletedRatio"]
    return f"Percentage of population vaccinated in the US: {round(vaccination * 100, 2)}%"


def total_deaths():
    response = r.get(
        f"https://api.covidactnow.org/v2/country/US.json?apiKey={COVID_ACT_NOW_KEY}"
    ).json()
    deaths = response["actuals"]["deaths"]
    return f"The total number of deaths in US: {deaths}"


def deaths(state):
    resp = r.get(f"https://disease.sh/v3/covid-19/nyt/states/{state}?lastdays=1").json()
    deaths = resp[0]['deaths']
    return f"Current number of deaths in {state}: {deaths}"


def cases(state):
    response = r.get(f"https://disease.sh/v3/covid-19/nyt/states/{state}?lastdays=1").json()
    cases = response[0]['cases']
    return f"Current number of cases in {state}: {cases}"
