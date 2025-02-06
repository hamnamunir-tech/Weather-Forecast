import requests
import datetime

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/"


def get_weather(city):
    url = f"{BASE_URL}weather?q={city}&app-id={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']

        report = f"\nCurrent Weather in {city}:\n"
        report += f"Temperature: {temp}°C\n"
        report += f"Humidity: {humidity}%\n"
        report += f"Condition: {condition.capitalize()}\n"
        print(report)
        return report
    else:
        print("Error: City not found or API request failed.")
        return None


def get_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&app-id={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\n5-Day Weather Forecast:")
        report = "\n5-Day Weather Forecast:\n"

        forecasts = {}
        for entry in data['list']:
            date = entry['dt_txt'].split(" ")[0]
            if date not in forecasts:
                forecasts[date] = entry

        for date, forecast in forecasts.items():
            temp_min = forecast['main']['temp_min']
            temp_max = forecast['main']['temp_max']
            condition = forecast['weather'][0]['description']
            forecast_str = f"{date}: {temp_min}°C - {temp_max}°C, {condition.capitalize()}"
            print(forecast_str)
            report += forecast_str + "\n"
        return report
    else:
        print("Error: Could not retrieve forecast data.")
        return None


def save_report(city, report):
    if report:
        with open("weather_report.txt", "w") as file:
            file.write(f"Weather Report for {city}\n")
            file.write(report)
        print("\nWeather report saved to weather_report.txt")


def main():
    city = input("Enter city name: ").strip()
    report = ""

    weather_report = get_weather(city)
    if weather_report:
        report += weather_report

    forecast_report = get_forecast(city)
    if forecast_report:
        report += forecast_report

    if weather_report or forecast_report:
        save_report(city, report)


if __name__ == "__main__":
    main()