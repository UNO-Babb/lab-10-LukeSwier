#MapPlot.py
#Name:
#Date:
#Assignment:

import cars
import pandas
import matplotlib.pyplot as plt
years = []
CityMPGs = []
cars = cars.get_car()
for gear in cars:
    year = gear["Identification"]["Year"]
    CityMPG = gear["Fuel Information"]["City mpg"]
    years.append(year)
    CityMPGs.append(CityMPG)

df = pandas.DataFrame([{"Year": years, "City MPG": CityMPGs}])

plt.plot(years, CityMPGs)
plt.savefig("DataTable")