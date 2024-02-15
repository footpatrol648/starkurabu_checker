import requests

def get_whitelisted_status(address):
    url = f"https://api.starkurabu.com/get_whitelisted_status?addr={address}"
    response = requests.get(url)
    data = response.json()
    status = data.get('status')
    return status

def main():
    # Load addresses from wallets.txt
    with open('wallets.txt', 'r') as file:
        addresses = file.read().splitlines()

    # Iterate over addresses and print results
    for address in addresses:
        result = get_whitelisted_status(address)
        print(f"{address} {result}")

if __name__ == "__main__":
    main()
