import requests

res_parse_list = []
response = requests.get("https://"
                        "bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
   if parse_elem_1.startswith("$"):
       for parse_elem_2 in parse_elem_1.
                           split("</span>"):
          if parse_elem_2.startswith("$")
            and parse_elem_2[1].isdigit():
              res_parse_list.append(parse_
                                   elem_2)
Usd_exchange_rate = res_parse_list[0]
print(usd_exchange_rate)