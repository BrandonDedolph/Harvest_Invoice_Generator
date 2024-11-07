import requests
from date import ISODate

class HarvestError(Exception):
    """Custom exception for Harvest API errors."""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code


class HarvestClient:

    HARVEST_API_BASE_URL = "https://api.harvestapp.com/v2"

    def __init__(self, account_id: str, access_token: str):
        self.account_id = account_id
        self.access_token = access_token
        self.headers = {
                "User-Agent": "Harvest Invoice Gen",
                "Authorization": f"Bearer {self.access_token}",
                "Harvest-Account-ID": self.access_token
                }


    def fetch_time_entries(start_date: ISODate, end_date: ISODate):
        pass



