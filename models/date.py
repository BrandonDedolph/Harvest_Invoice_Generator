from pydantic import ConstrainedStr, ValidationError
from datetime import date

class ISODate(ConstrainedStr):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_iso_date

    @classmethod
    def validate_iso_date(cls, values):
        try:
            # Attempt to parse the date
            parsed_date = date.fromisoformat(value)
            return parsed_date.isoformat()
        except:
            raise ValueError('String must be in ISO date format (YYYY-MM-DD)')

