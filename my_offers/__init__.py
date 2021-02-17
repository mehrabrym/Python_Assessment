import json
import requests
import time
import csv

endpoint = "https://atlas.pretio.in/atlas/coding_quiz"
headers = {"Authorization": "Bearer LpNe5bB4CZnvkWaTV9Hv7Cd37JqpcMNF"}
requestCount = 0

def request_offers(endpoint, headers, requestCount):
    response = requests.get(endpoint, headers=headers)
    get_offers(response, requestCount)

def get_offers(response, requestCount):
    if response.status_code == 429:
        if requestCount == 0:
            print("Received error code 429 for too many requests. Waiting 60 seconds before trying again.")
            time.sleep(60)
            request_offers(endpoint, headers, 1)
        if requestCount == 1:
            input("Received error code 429 for too many requests a second time. Press Enter to exit...")
    if response.status_code == 500:
        input("Received error code 500 for internal server error. Press Enter to exit...")
    if response.status_code == 200:
        data = response.json()
        data_offers = data['rows']
        data_offers.sort(key = lambda i: float(i['payout']), reverse=True)
        file = open('offers.csv', 'w', newline='', encoding="utf-8")
        
        writer = csv.writer(file)
        c = 0
        for offer in data_offers:
            if c == 0:
                header = offer.keys()
                writer.writerow(header)
                c += 1            
            writer.writerow(offer.values())        
        file.close()
        
        input("Offers have been written to offers.csv. Press Enter to exit...")
            
            
if __name__ == '__main__':
    request_offers(endpoint, headers, requestCount)
