
from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from datetime import datetime

def get_wallet_info(address: str):
    tron = Tron()
    try:
        account = tron.get_account(address)
        trx_balance = account['balance'] / 1e6  # Преобразование из Sun в TRX
        bandwidth = account['bandwidth']
        energy = account['energy']
        return {
            "trx_balance": trx_balance,
            "bandwidth": bandwidth,
            "energy": energy
        }
    except AddressNotFound:
        return None
