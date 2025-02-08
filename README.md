# Weather Forecast CLI Tool

## Description
This Python script allows users to retrieve current weather conditions and a 5-day weather forecast for a specified city using the OpenWeatherMap API. The tool displays temperature, humidity, and weather conditions in a user-friendly format and saves the weather report to a file for reference.

## Features
- Fetches current weather details, including:
  - Temperature (in Celsius)
  - Humidity
  - Weather condition
- Retrieves a 5-day weather forecast with temperature ranges and weather conditions.
- Saves the weather report to a text file (`weather_report.txt`).
- Provides error handling for invalid city names or API request failures.

## Requirements
- Python 3+
- `requests` library
- OpenWeatherMap API key

## Installation
1. Clone or download this repository.
2. Install the required dependencies:
   ```sh
   pip install requests
   ```
3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/).
4. Replace `YOUR_API_KEY` in the script with your actual API key.

## Usage
1. Run the script:
   ```sh
   python weather_forecast.py
   ```
2. Enter the name of the city when prompted.
3. View the current weather and 5-day forecast.
4. The weather report will be saved as `weather_report.txt`.

## Example Output
```
Enter city name: London

Current Weather in London:
Temperature: 15°C
Humidity: 78%
Condition: Cloudy

5-Day Weather Forecast:
2025-02-07: 10°C - 16°C, Light rain
2025-02-08: 11°C - 17°C, Clear sky
...

Weather report saved to weather_report.txt
```

## License
This project is open-source and available under the MIT License.

