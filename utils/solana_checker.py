import aiohttp
from datetime import datetime
from sqlalchemy import select

from database.models import Transaction, Address, User

SOLANA_RPC = "https://api.mainnet-beta.solana.com"

async def get_balance(address: str) -> float:
    """Получает баланс кошелька Solana (в SOL)"""
    async with aiohttp.ClientSession() as session:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [address]
        }
        async with session.post(SOLANA_RPC, json=payload) as resp:
            data = await resp.json()
            lamports = data["result"]["value"]
            return lamports / 1e9  # 1 SOL = 1e9 лампортов
