import test_periods
import weather_html
import requests

print('''
Choose a city:
[1] New York City, New York
[2] Los Angeles, California
[3] Philadelphia, Pennsylvania
[4] Chicago, Ilinois
[5] Houston, Texas'''
)
option = int(input('Enter 1-5: '))
cities = {
    1:['NewYorkCityNewYork','New York City, New York', 'https://api.weather.gov/gridpoints/OKX/32,34/forecast'],
    2:['LosAngelesCalifornia','Los Angeles, California', 'https://api.weather.gov/gridpoints/LOX/154,44/forecast'],
    3:['PhiladelphiaPennsylvania', 'Philadelphia, Pennsylvania','https://api.weather.gov/gridpoints/PHI/49,75/forecast'],
    4:['ChicagoIllinois', 'Chicago, Illinois', 'https://api.weather.gov/gridpoints/LOT/75,72/forecast'],
    5:['HoustonTexas', 'Houston, Texas', 'https://api.weather.gov/gridpoints/PHI/49,75/forecast']
}

url = cities[option][2]
response = requests.get(url)
if response.status_code == 200:
    data = response.json()




#Here we are declaring the variables that we are going to use 
# and the period of time
city_name = cities[option]
print(f'{city_name[1]}')
print(f'Forecast document written to {city_name[0]}.html')
#periods = test_periods.periods_that_start_with_a_day
periods = data['properties']['periods']
#This variable has the function create.document and its values. 
#Creates the file name report while adding the city name and 
# calling the values from weather_html.py saved in the []
document = weather_html.create_document(f'{city_name[0]}.html', city_name[1], [weather_html.PERIOD_NAME, weather_html.ICON, weather_html.TEMPERATURE, weather_html.WIND, weather_html.DETAILED_FORECAST])
#This numbers will draw the key from the test_periods.py file that we 
# want to intinerate in the loops.The second is created to benefit 
# the desing of the second loop in the night broadcast
x = 0
y = 1

if periods[0]['isDaytime'] == True:
#The number five is to get this information 5 times
    for i in range(5):
#This adds a row
        weather_html.start_new_row(document)
#And for each row, we are adding a  number to get the key information 
# associate with that number moreover, we want the file to have store 
# two temperatures per row, so the add_period is going to be called to times
        weather_html.add_period(document, periods[x])
        x += 1
        weather_html.add_period(document, periods[x])
        x += 1

#If we choose the second option of periods we are going to neet a blank
#space in the left right of the first row. So we are adding this one.
#This is going to add just one period and will ignore de first one to
#benefit formating and the example given.
elif periods[0]['isDaytime'] == False:
    weather_html.start_new_row(document)
#Ignore the first one and adds a blank space
    weather_html.add_period(document, {})
#Add the first one
    weather_html.add_period(document, periods[x])
    for i in range(4):
        weather_html.start_new_row(document)
#In here we are going to use another variable with other number called y
#This will start at 1 so is going to add one number starting at 1, thus
#ignoring the first value of the code and itinerating 4 times.
        weather_html.add_period(document, periods[y])
        y += 1
        weather_html.add_period(document, periods[y])
        y += 1

#This saves the page
weather_html.write_document(document)