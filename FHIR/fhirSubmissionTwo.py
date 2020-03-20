import matplotlib.pyplot as plt
import pandas as pd
from fhir_parser import FHIR

fhir = FHIR(endpoint='https://fhir.compositegrid.com:5001/api/')
patients = fhir.get_all_patients()

languageConversion = {}
languageConversion['English'] = "en"
languageConversion["Spanish"] = "es"
languageConversion["French"] = "fr"
languageConversion["Italian"] = "it"
languageConversion["Greek"] = "el"
languageConversion["Hindi"] = "hi"
languageConversion["Portugese"] = "pt"
languageConversion["Chinese"] = "zh"
languageConversion["Russian (Russia)"] = "ru"
languageConversion["German (Germany)"] = "de"
languageConversion["Korean"] = "ko"
languageConversion["Vietnamese"] = "vi"
languageConversion["Japanese"] = "ja"
languageConversion["Portuguese"] = "pt"

languages = []
femaleData = {}
maleData = {}
for patient in patients:
    language = str(patient.communications.languages)
    gender = str(patient.gender)
    length = len(language) - 2
    language = language[2:length]
    if language == "French (France)":
        language = "French"
    print(language)
    language = languageConversion[language]
    if language not in languages:
        languages.append(language)
        femaleData[language] = 0
        maleData[language] = 0

    if gender == "female":
        femaleData[language] += 1
    else:
        maleData[language] += 1

r = []
raw_data = {}
raw_data["femaleBars"] = []
raw_data["maleBars"] = []

for x in range(len(languages)):
    print(languages[x])
    r.append(x)
    raw_data["femaleBars"].append(femaleData[languages[x]])
    raw_data["maleBars"].append(maleData[languages[x]])


df = pd.DataFrame(raw_data)
totals = [i+j for i,j in zip(df['femaleBars'], df['maleBars'])]
pinkBars = [i / j * 100 for i,j in zip(df['femaleBars'], totals)]
darkBlueBars = [i / j * 100 for i,j in zip(df['maleBars'], totals)]


# plot
barWidth = 0.85



plt.bar(r, darkBlueBars, color='#4095F6', edgecolor='white', width=barWidth, label="Male")
# Create blue Bars
plt.bar(r, pinkBars, bottom=darkBlueBars, color='#F7C1FC', edgecolor='white', width=barWidth, label="Female")
plt.label
# Custom x axis
plt.xticks(r, languages)
plt.xlabel("Languages (ISO 639-1 Language Codes)")
plt.ylabel("Percentage of People")
plt.title("Languages Spoken Separated by Gender")

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

# Show graphic
plt.show()



