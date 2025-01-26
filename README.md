# API-INTEGRATION-AND-DATA-VISUALIZATION
USING PYTHON TO FETCH DATA FROM A PUBLIC API (E.G., OPENWEATHERMAP)

COMPANY: CODTECH IT SOLUTIONS

NAME: SWAPNIL RAJ

INTERN ID: CT08LIH

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

##Understanding the Code:

The Python code retrieves weather data for a specific city using the OpenWeatherMap API:

requests library: Facilitates making HTTP requests to web APIs.
Variables:
city_name: Stores the city name (e.g., Lonavala).
API_key: Holds your OpenWeatherMap API key (replace with your own).
API URL Construction:
url: Builds the complete URL with city name and API key.
Sending the Request:
response = requests.get(url): Sends a GET request using requests.
Checking Response Status:
if response.status_code == 200:: Checks for a successful response (status code 200).
Processing Response Data (if successful):
data = response.json(): Converts JSON response data to a Python dictionary.
print statements: Extract and print specific weather information (description, temperature, feels-like temperature, humidity).
Using the Code:

Where to Use:

Weather Monitoring and Alerts: Integrate the code into applications that monitor weather in real-time and set up alerts based on specific criteria.
Weather-Based Decision Making: Incorporate weather data into travel planning apps, agricultural automation systems, or sports scheduling tools.
Educational Projects: Use the code to learn about APIs, web scraping, and data analysis in Python.
Why Use It?

Accessibility: OpenWeatherMap provides a free and easy-to-use API.
Customization: Tailor the code to extract specific weather parameters.
Integration: Integrate the code with various programming languages and platforms.
Additional Considerations:

API Rate Limits: Be mindful of OpenWeatherMap's rate limits.
Error Handling: Implement error handling for issues like invalid API keys or network errors.
Data Security: Ensure proper security measures for storing or transmitting API keys.
Beyond OpenWeatherMap:

Many other APIs exist for various purposes, including news, social media, finance, and location.

Executing the Code in PyCharm:

Create a new Python file (e.g., weather_data.py).
Paste the code and replace the placeholder API key.
Run the script by right-clicking on weather_data.py and selecting "Run 'weather_data.py'".
Key Points:

Treat API keys confidentially.
Refer to OpenWeatherMap's documentation for details on available parameters and response formats.
Analyze retrieved weather data using libraries like pandas and matplotlib for visualizations or statistical calculations.

##OUTPUT:

<img width="1710" alt="Image" src="https://github.com/user-attachments/assets/b5d986fe-42e2-4ad2-bbb5-6b767e96a4a7" />
