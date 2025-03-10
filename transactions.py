import requests
from config import API_URL, SAMPLE_ORDER
from headers import headers

#createdSince argument the return internal server error
def get_transactions(api_url, headers, order_id):
    response = requests.get(
        f"{api_url}/transactions?orderUid={order_id}", headers=headers
    )
    return response.json()

def get_transaction_by_id(api_url, headers, transaction_id):
    response = requests.get(
        f"{api_url}/transactions/{transaction_id}", headers=headers
    )
    return response.json()

transactions = get_transactions(API_URL, headers, SAMPLE_ORDER)
print("transactions: ", transactions)
