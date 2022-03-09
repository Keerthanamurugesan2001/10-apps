import collections
import requests


location = collections.namedtuple('location', 'city state country')
Weather = collections.namedtuple('Weather', 'location units temp condition')


def main():
    # show the header
    show_header()

    # Get the location request
    location_txt = input("where do you want to see the whether? (eg., boston, US"
                         ") ")

    # convert the plaintext to data that we can use
    loc = convert_plaintxt_location(location_txt)

    # Get report from API
    data = get_weather_report(loc)

    # Report the weather
    proper_view(data, loc)


def show_header():
    print("-----------------------------")
    print("       whether forecast")
    print("-----------------------------", end="\n")


def convert_plaintxt_location(location_txt):
    if not location_txt.strip():
        return None
    else:
        location_txt = location_txt.lower().strip()
        parts = location_txt.split(',')

        city = ''
        state = ''
        country = ''
        if len(parts) == 1:
            city = parts[0].strip()
        elif len(parts) == 2:
            city = parts[0].strip()
            country = parts[1].strip()
        else:
            city = parts[0].strip()
            state = parts[1].strip()
            country = parts[2].strip()

    return location(city, state, country)


def get_weather_report(loc):
    url = f"https://weather.talkpython.fm/api/weather?city={loc.city}&units=imperial"

    if loc.country:
        url += f"&country={loc.country}"
    if loc.state:
        url += f"$state={loc.state}"

    resp = requests.get(url)
    if resp.status_code in {400, 404, 500}:
        print(f"error: {resp.text}.")
        return None

    data = resp.json()

    temp = data.get('forecast').get('temp')
    w = data.get('weather')
    condition = f"{w.get('category')}: {w.get('description')}"

    return Weather(loc, 'imperal', temp, condition)


def proper_view(wea,loc):
    txt = f"Weather in {loc.city}"
    if loc.state:
        txt += f", {loc.state}"
    if loc.country:
        txt += f", {loc.country}"

    txt += f" is {wea.temp} F and {wea.condition}"
    print(txt)


if __name__ == '__main__':
    main()
