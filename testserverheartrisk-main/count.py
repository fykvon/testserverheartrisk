import json
import os
from datetime import datetime

from parsing import pars_temp_pressure_humidity, pars_magn, req_magn, req_weather
from text import green_fon, red_fon


def formula(weather, avg_magnitude, green_fon, red_fon) -> dict:
    """ All calculations here. green_fon and red_fon imported from text.py.
    If you want to change description, change text.py"""

    avg_humidity = float(weather[2])
    pressure = float(weather[1])
    avg_temp = float(weather[0])
    """ Здесь находится формула расчёта коэффициента риска сердечной недостаточности
    (Интелектальная собственность)"""
    if p <= 50:
        message = green_fon
    else:
        message = red_fon
    return {
        'result': p,
        'message': 'Высокий риск развития гипертонического криза у пациентов с гипертонической болезнью.',
        'recomend': message,
        'humiduty': avg_humidity,
        'pressure': pressure,
        'avg_temp': avg_temp,
        'avg_magnitude': avg_magnitude
    }


def count_func() -> dict:
    weather_info = pars_temp_pressure_humidity(request=req_weather)
    magnitude = pars_magn(request=req_magn)
    result = formula(
        weather=weather_info,
        avg_magnitude=magnitude,
        green_fon=green_fon,
        red_fon=red_fon)

    return result


def main():
    """Main func. Use this func in if __name__ == '__main__'"""

    today = datetime.utcnow()
    datename = datetime.date(today)
    file_dir = f'data_files_per_date/{datename}.json'

    if os.path.isfile(file_dir):
        size = os.path.getsize(f'{file_dir}')
        if size != 0:
            with open(f"{file_dir}") as file:
                data_from_file = json.load(file)
                return data_from_file

    else:
        result = count_func()
        with open(f"{file_dir}", "w+") as out:
            json.dump(result, out)
        return result


if __name__ == '__main__':
    main()
