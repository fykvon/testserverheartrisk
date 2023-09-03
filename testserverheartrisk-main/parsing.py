from bs4 import BeautifulSoup as bs
import requests

URL_TEMPERATURE = "https://weather.rambler.ru/v-gelendzhike/today/"
URL_MAGN = 'https://ru-meteo.ru/gelendzhik/gm'

req_weather = requests.get(URL_TEMPERATURE)
req_magn = requests.get(URL_MAGN)


def pars_magn(request) -> float:
    """
    Parsing data from url.

    :param request: URL
    :return: float
    """
    soup = bs(request.text, "html.parser")
    raw_data = soup.find(class_='day').find_all(class_='index')
    numbers_list = [int(i.text) for i in raw_data]
    avg_magn = sum(numbers_list) / len(numbers_list)
    return avg_magn


def pars_temp_pressure_humidity(request) -> list:
    """
    Parsing data from url.

    :param request: URL
    :return: list with float average temperature, average humidity and atmosphere pressure
    """
    soup = bs(request.text, "html.parser")

    temp_data = soup.find(class_='ALjB').find_all(class_='Njqa')
    temp = [int(i.text[:2]) for i in temp_data]
    avg_temp = sum(temp) / len(temp)

    pressure_data = soup.find(class_='qRFP').find_all(class_='VaOz d2qU')[1].text
    pressure_s = str("")
    for i in pressure_data:
        if i.isdigit():
            pressure_s += str(i)
    pressure = int(pressure_s)

    humidity_data = soup.find_all(class_='aAfv')[18:27]
    humidity_list = [int(i.text) for i in humidity_data]
    avg_humidity = round(sum(humidity_list) / len(humidity_list))

    return [avg_temp, pressure, avg_humidity]
