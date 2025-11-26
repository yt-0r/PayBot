import requests

USDT_MINT = "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"
RPC_URL = "https://api.mainnet-beta.solana.com"


def get_balance(wallet_address: str) -> float:
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenAccountsByOwner",
        "params": [
            wallet_address,
            {"mint": USDT_MINT},
            {"encoding": "jsonParsed"}
        ]
    }
    response = requests.post(RPC_URL, json=payload).json()
    accounts = response.get("result", {}).get("value", [])

    balance = 0.0
    for account in accounts:
        balance += float(account["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"])

    return balance



