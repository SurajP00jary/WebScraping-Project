import requests
from bs4 import BeautifulSoup
#URL="https://www.amazon.in/Samsung-Storage-Snapdragon-sAMOLED-Display/dp/B09CV6FJ62/ref=sr_1_1_sspa?dchild=1&keywords=i+pjone11pro&qid=1635138393&sprefix=i+pj%2Caps%2C284&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUzFGSDZRUTBaQjJMJmVuY3J5cHRlZElkPUExMDQ2MjEwSDlOMjRJUUtVTlpaJmVuY3J5cHRlZEFkSWQ9QTAwNzEwOTgzQ0VJWFRKWFEzV1g1JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
#URL="https://www.amazon.in/Apple-iPhone-13-Mini-256GB/dp/B09G995NMD/ref=sr_1_2?dchild=1&keywords=i+phone13mobile+phone+pro+max+%2B&qid=1635138757&sprefix=i+%5B%2Caps%2C329&sr=8-2"
URL_list=[
    {
   "url":"https://www.amazon.in/Xiaomi-Slimmest-Lightest-Smartphone-Replacement/dp/B09G39VLGV/ref=sr_1_3?dchild=1&keywords=i+phone13mobile+phone+pro+max+%2B&qid=1635138757&sprefix=i+%5B%2Caps%2C329&sr=8-3",
   "name":"Xiomi",
        "target_price":15000
    },
    {
    "url":"https://www.amazon.in/Apple-iPhone-13-Mini-256GB/dp/B09G995NMD/ref=sr_1_2?dchild=1&keywords=i+phone13mobile+phone+pro+max+%2B&qid=1635138757&sprefix=i+%5B%2Caps%2C329&sr=8-2",
    "name":"iPhone",
        "target_price":80000
    },
    {"url":"https://www.amazon.in/Realme-Pro-Chroma-White-Storage/dp/B08JCRWW1Q/ref=sr_1_1?crid=2T8LUHU99WJ&dchild=1&keywords=realme+5+pro&qid=1635161012&sprefix=realme+5+%2Caps%2C655&sr=8-1",
     "name":"realme",
     "target_price":17000
     },
    {
        "url":"https://www.amazon.in/OnePlus-Nord-Charcoal-128GB-Storage/dp/B09576CYNP/ref=sr_1_1?crid=2DORQ6LL8A3BR&dchild=1&keywords=one+plus+nord&qid=1635659146&sprefix=one+plus+nord%2Caps%2C576&sr=8-1",
        "name":"oneplus",
        "target_price":25000
    },
    {
     "url":"https://www.amazon.in/Starry-Storage-Additional-Exchange-Offers/dp/B08LRFGM3T/ref=sr_1_1_sspa?dchild=1&keywords=oppo+reno+6%2B&qid=1635659246&sprefix=oppo+%2Caps%2C1498&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQVVYVzRNQTNOWFc0JmVuY3J5cHRlZElkPUEwNjQyMzQ2MjJMWUhGVzdLQ05PVSZlbmNyeXB0ZWRBZElkPUEwNjMzOTI1MU05ODFRNzBHUUFEUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name":"oppo",
        "target_price":33000
    }
]
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
def give_product_price(URL):

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.find(id="priceblock_dealprice")
    if (price == None):
      price = soup.find(id="priceblock_ourprice")
    return price.getText()
result_file=open('my_result.txt','w')
try:
    for every_product in URL_list:
        hello = give_product_price((every_product.get("url")))
        print(hello + " - " + every_product.get("name"))
        hello_new = hello[1:]
        hello_new = hello_new.replace(",", "")
        hello_new = int(float(hello_new))
        print(hello_new)
        if hello_new < every_product.get("target_price"):
            print("available at your price")
            result_file.write(every_product.get('name') +"- \t"+ "available at your price i.e "+str(hello_new)+'\n')
        else:
            print("Still at  current price")

finally:
    result_file.close()






