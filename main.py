# Import Libraries
import requests
from bs4 import BeautifulSoup

def weather(city):
    # For the Query
    city = city.replace(" ", "+")

    link = "https://www.google.com/search?q=weather+" + city
    res = requests.get(link)
    
    # Website Title
    soup = BeautifulSoup(res.content, "html.parser")
    element = soup.find('div', class_='BNeawe iBp4i AP7Wnd')

    # If the element is found, .text is used to extract the text within the span element.
    if element:
        extracted_text = ""
        # only extract the number
        for letter in element.text:
            if letter.isdigit():
                extracted_text += letter

        return(extracted_text)  # Output: 54

def convertCelsius(num):
    celsius = round((num - 32) * 5/9)
    return str(celsius)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Enter City Here: ")
    # input city
    city = str(input())

    print(weather(city) + "° Fahrenheit")

    print("Would You Like To Covert to Celsius? ")
    # yes or no
    response = str(input())
    if response.isalpha():
        for letter in response:
            if letter == 'y' or letter == 'Y':
                print(convertCelsius(int(weather(city))) + "° Celsius")

    print("Done Computing")
