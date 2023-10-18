import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:/Users/geord/Desktop/Python/Life_exp.csv')
data = df.loc[:, ["Country", "Population", "Continent", "Life_expectancy ", "GDP", "Income_composition_of_resources",
                  "Schooling"]].copy()
# with pd.option_context('display.max_rows', None, ):
#    print(data[df["Year"] == 2015])
yr_2015 = data[df["Year"] == 2015].copy()
GDP = np.array(list(yr_2015['GDP']))
pop = np.array(list((yr_2015['Population'])))

gdp_per_cap = list(GDP * 1000000000 / pop)
GDP_per_cap = pd.DataFrame(gdp_per_cap)
idx = pd.Index(range(138))
yr_2015.set_index(idx)
yr_2015.insert(7, "GDP_per_cap", gdp_per_cap)
color = {'Asia': 'blue', 'Europe': 'red', 'Africa': 'brown', 'South America': 'green', 'Australia': 'yellow',
         'North America': 'purple', 'Oceania': 'yellow', 'Asia/Europe': 'red'
         }
continents = yr_2015["Continent"]
colour = []
for i in continents:
    colour.append(color[i])
# Scatter plot
plt.scatter(x=yr_2015['GDP_per_cap'], y=yr_2015['Life_expectancy '], s=pop / 1000000, alpha=0.8, c=colour)

# customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2015')
plt.xticks([1000, 10000, 100000, 1000000, 1000000000], ['1k', '10k', '100k', '1m', '1bn'])

# Show the plot
# plt.show()

# year 2014
yr_2014 = data[df["Year"] == 2014].copy()
for lab, row in yr_2014.iterrows():
    yr_2014.loc[lab, "gdp par dimoune"] = row['GDP'] * 1000000000 / row['Population']

Country_dict = {"AF": "Afghanistan",
                "AX": "Aland Islands",
                "AL": "Albania",
                "DZ": "Algeria",
                "AS": "American Samoa",
                "AD": "Andorra",
                "AO": "Angola",
                "AI": "Anguilla",
                "AQ": "Antarctica",
                "AG": "Antigua and Barbuda",
                "AR": "Argentina",
                "AM": "Armenia",
                "AW": "Aruba",
                "AU": "Australia",
                "AT": "Austria",
                "AZ": "Azerbaijan",
                "BS": "Bahamas",
                "BH": "Bahrain",
                "BD": "Bangladesh",
                "BB": "Barbados",
                "BY": "Belarus",
                "BE": "Belgium",
                "BZ": "Belize",
                "BJ": "Benin",
                "BM": "Bermuda",
                "BT": "Bhutan",
                "BO": "Bolivia, Plurinational State of",
                "BQ": "Bonaire, Sint Eustatius and Saba",
                "BA": "Bosnia and Herzegovina",
                "BW": "Botswana",
                "BV": "Bouvet Island",
                "BR": "Brazil",
                "IO": "British Indian Ocean Territory",
                "BN": "Brunei Darussalam",
                "BG": "Bulgaria",
                "BF": "Burkina Faso",
                "BI": "Burundi",
                "KH": "Cambodia",
                "CM": "Cameroon",
                "CA": "Canada",
                "CV": "Cabo Verde",
                "KY": "Cayman Islands",
                "CF": "Central African Republic",
                "TD": "Chad",
                "CL": "Chile",
                "CN": "China",
                "CX": "Christmas Island",
                "CC": "Cocos (Keeling) Islands",
                "CO": "Colombia",
                "KM": "Comoros",
                "CG": "Congo",
                "CD": "Congo, The Democratic Republic of the",
                "CK": "Cook Islands",
                "CR": "Costa Rica",
                "CI": "Côte d'Ivoire",
                "HR": "Croatia",
                "CU": "Cuba",
                "CW": "Curaçao",
                "CY": "Cyprus",
                "CZ": "Czech Republic",
                "DK": "Denmark",
                "DJ": "Djibouti",
                "DM": "Dominica",
                "DO": "Dominican Republic",
                "EC": "Ecuador",
                "EG": "Egypt",
                "SV": "El Salvador",
                "GQ": "Equatorial Guinea",
                "ER": "Eritrea",
                "EE": "Estonia",
                "ET": "Ethiopia",
                "FK": "Falkland Islands (Malvinas)",
                "FO": "Faroe Islands",
                "FJ": "Fiji",
                "FI": "Finland",
                "FR": "France",
                "GF": "French Guiana",
                "PF": "French Polynesia",
                "TF": "French Southern Territories",
                "GA": "Gabon",
                "GM": "Gambia",
                "GE": "Georgia",
                "DE": "Germany",
                "GH": "Ghana",
                "GI": "Gibraltar",
                "GR": "Greece",
                "GL": "Greenland",
                "GD": "Grenada",
                "GP": "Guadeloupe",
                "GU": "Guam",
                "GT": "Guatemala",
                "GG": "Guernsey",
                "GN": "Guinea",
                "GW": "Guinea-Bissau",
                "GY": "Guyana",
                "HT": "Haiti",
                "HM": "Heard Island and McDonald Islands",
                "VA": "Holy See (Vatican City State)",
                "HN": "Honduras",
                "HK": "Hong Kong",
                "HU": "Hungary",
                "IS": "Iceland",
                "IN": "India",
                "ID": "Indonesia",
                "IR": "Iran, Islamic Republic of",
                "IQ": "Iraq",
                "IE": "Ireland",
                "IM": "Isle of Man",
                "IL": "Israel",
                "IT": "Italy",
                "JM": "Jamaica",
                "JP": "Japan",
                "JE": "Jersey",
                "JO": "Jordan",
                "KZ": "Kazakhstan",
                "KE": "Kenya",
                "KI": "Kiribati",
                "KP": "Korea, Democratic People's Republic of",
                "KR": "Korea, Republic of",
                "KW": "Kuwait",
                "KG": "Kyrgyzstan",
                "LA": "Lao People's Democratic Republic",
                "LV": "Latvia",
                "LB": "Lebanon",
                "LS": "Lesotho",
                "LR": "Liberia",
                "LY": "Libya",
                "LI": "Liechtenstein",
                "LT": "Lithuania",
                "LU": "Luxembourg",
                "MO": "Macao",
                "MK": "Macedonia, Republic of",
                "MG": "Madagascar",
                "MW": "Malawi",
                "MY": "Malaysia",
                "MV": "Maldives",
                "ML": "Mali",
                "MT": "Malta",
                "MH": "Marshall Islands",
                "MQ": "Martinique",
                "MR": "Mauritania",
                "MU": "Mauritius",
                "YT": "Mayotte",
                "MX": "Mexico",
                "FM": "Micronesia, Federated States of",
                "MD": "Moldova, Republic of",
                "MC": "Monaco",
                "MN": "Mongolia",
                "ME": "Montenegro",
                "MS": "Montserrat",
                "MA": "Morocco",
                "MZ": "Mozambique",
                "MM": "Myanmar",
                "NA": "Namibia",
                "NR": "Nauru",
                "NP": "Nepal",
                "NL": "Netherlands",
                "NC": "New Caledonia",
                "NZ": "New Zealand",
                "NI": "Nicaragua",
                "NE": "Niger",
                "NG": "Nigeria",
                "NU": "Niue",
                "NF": "Norfolk Island",
                "MP": "Northern Mariana Islands",
                "NO": "Norway",
                "OM": "Oman",
                "PK": "Pakistan",
                "PW": "Palau",
                "PS": "Palestinian Territory, Occupied",
                "PA": "Panama",
                "PG": "Papua New Guinea",
                "PY": "Paraguay",
                "PE": "Peru",
                "PH": "Philippines",
                "PN": "Pitcairn",
                "PL": "Poland",
                "PT": "Portugal",
                "PR": "Puerto Rico",
                "QA": "Qatar",
                "RE": "Réunion",
                "RO": "Romania",
                "RU": "Russian Federation",
                "RW": "Rwanda",
                "BL": "Saint Barthélemy",
                "SH": "Saint Helena, Ascension and Tristan da Cunha",
                "KN": "Saint Kitts and Nevis",
                "LC": "Saint Lucia",
                "MF": "Saint Martin (French part)",
                "PM": "Saint Pierre and Miquelon",
                "VC": "Saint Vincent and the Grenadines",
                "WS": "Samoa",
                "SM": "San Marino",
                "ST": "Sao Tome and Principe",
                "SA": "Saudi Arabia",
                "SN": "Senegal",
                "RS": "Serbia",
                "SC": "Seychelles",
                "SL": "Sierra Leone",
                "SG": "Singapore",
                "SX": "Sint Maarten (Dutch part)",
                "SK": "Slovakia",
                "SI": "Slovenia",
                "SB": "Solomon Islands",
                "SO": "Somalia",
                "ZA": "South Africa",
                "GS": "South Georgia and the South Sandwich Islands",
                "ES": "Spain",
                "LK": "Sri Lanka",
                "SD": "Sudan",
                "SR": "Suriname",
                "SS": "South Sudan",
                "SJ": "Svalbard and Jan Mayen",
                "SZ": "Swaziland",
                "SE": "Sweden",
                "CH": "Switzerland",
                "SY": "Syrian Arab Republic",
                "TW": "Taiwan, Province of China",
                "TJ": "Tajikistan",
                "TZ": "Tanzania, United Republic of",
                "TH": "Thailand",
                "TL": "Timor-Leste",
                "TG": "Togo",
                "TK": "Tokelau",
                "TO": "Tonga",
                "TT": "Trinidad and Tobago",
                "TN": "Tunisia",
                "TR": "Turkey",
                "TM": "Turkmenistan",
                "TC": "Turks and Caicos Islands",
                "TV": "Tuvalu",
                "UG": "Uganda",
                "UA": "Ukraine",
                "AE": "United Arab Emirates",
                "GB": "United Kingdom",
                "US": "United States",
                "UM": "United States Minor Outlying Islands",
                "UY": "Uruguay",
                "UZ": "Uzbekistan",
                "VU": "Vanuatu",
                "VE": "Venezuela, Bolivarian Republic of",
                "VN": "Viet Nam",
                "VG": "Virgin Islands, British",
                "VI": "Virgin Islands, U.S.",
                "WF": "Wallis and Futuna",
                "YE": "Yemen",
                "ZM": "Zambia",
                "ZW": "Zimbabwe"}


def getkey(val):
    for key, value in Country_dict.items():
        if val == value:
            return key
    return "key doesn't exist"


for lab, row in yr_2014.iterrows():
    yr_2014.loc[lab, "abb"] = getkey(row['Country'])

yr_2014.index = yr_2014['abb']
del yr_2014['abb']
yr_2014.index.name = None
print(yr_2014)
# renaming a bunch of indexes
# yr_2014.rename(index={"key doesn't exist":'CV'}, inplace=True)

class car(): #defining car class
	def __init__(self,**kwargs): #args receives unlimited no. of arguments as an array
		self.speed = kwargs['s'] #access args index like array does
		self.color = kwargs['c']
				
#creating objects of car class
		
audi=car(s=200,c='red')
bmw=car(s=250,c='black')
mb=car(s=190,c='white')
	
print(audi.color)
print(bmw.speed)
