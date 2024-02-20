import requests

def get_currency_input(prompt):
    while True:
        currency = input(prompt)
        if currency.isalpha() and len(currency) == 3:
            return currency.upper()
        else:
            print("Invalid currency code. Please enter a valid 3-letter currency code.")

def get_amount_input():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("The amount must be greater than 0")
            else:
                return amount
        except ValueError:
            print("The amount must be a numeric value.")

def main():
    init_currency = get_currency_input("Please enter an initial currency: ")
    target_currency = get_currency_input("Please enter a target currency: ")
    amount = get_amount_input()

    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    headers = {"apikey": "N1AMRVmkdrJS3zp4ZTb4HBw5XfN668Uj"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        converted_amount = result['result']
        print(f'{amount} {init_currency} = {converted_amount} {target_currency}')
    else:
        print("Sorry, there was a problem. Please try again later.")

if __name__ == "__main__":
    main()
