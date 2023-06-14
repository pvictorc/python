
import json

file = open("covid_data.json","r")
covid_cases = json.load(file)

treshold = 200

for case in covid_cases:
    if (case["Deaths"] > treshold):
        print(case)
        break

# With 'first' library
from first import first

# for case in covid_cases:
#     match
first_case = first(covid_cases, key=lambda x:x["Deaths"] > treshold)
print (first_case)