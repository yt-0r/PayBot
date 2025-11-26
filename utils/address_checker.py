import re

SOLANA_ADDRESS_REGEX = r"^[1-9A-HJ-NP-Za-km-z]{32,44}$"

def is_valid_solana_address(address: str) -> bool:
    return re.match(SOLANA_ADDRESS_REGEX, address) is not None
