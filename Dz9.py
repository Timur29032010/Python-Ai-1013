import requests
class CurrencyConverter:

   def __init__(self):

       self.rates = {}

   def get_rates(self):

       response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

       data = response.json()

       for item in data:

           self.rates[item['cc']] = item['rate']

   def convert(self, amount, from_currency, to_currency):
       return amount

