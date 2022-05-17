from datetime import datetime, timedelta

class DataEndpointsUtils:
    def api_key_expired(self, created_date, valid_days=60):
        days_since_created = (datetime.today().date() - created_date).days
        if days_since_created <= valid_days:
            return False
        return True