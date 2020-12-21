
# Importing custom exception for implementation 
from exception.custom_exception import CommonException, InvalidException
from exception.custom_code import IntenalCode as IC
from exception.custom_message import IntenalMessage as IM

class MathService:

    def __init__(self, data: dict):
        self.data = data
        

    def _is_value_negative(self):
        """
        check if first and second are negative values.
        """
        self.first = self.data['first']
        self.second = self.data['second']
        self.name = self.data['name']

        if self.first < 0:
            raise InvalidException(IC.NEGATIVE_VALUE, IM.NEGATIVE_VALUE)
        
        if self.second < 0:
            raise InvalidException(IC.NEGATIVE_VALUE, IM.NEGATIVE_VALUE)


    def _is_value_greter_than_2digit(self):
        """
        check if first and second are more than 2 digit values.
        """
        
        if self.first >= 100:
            raise CommonException(IC.EXCEED_LIMIT, IM.EXCEED_LIMIT)

        if self.second >= 100:
            raise CommonException(IC.EXCEED_LIMIT, IM.EXCEED_LIMIT)


    def calculate(self) -> int:
        """
        calculate total of first and second if both the values are valid.
        """
        try:
            self._is_value_negative()
            self._is_value_greter_than_2digit()

            # raise Exception when name == 10. Its for testing purpose.
            if int(self.name) == 10:
                raise Exception("Something went wrong.")

            total = self.first + self.second
            return total

        except InvalidException as ex:
            raise ex

        except CommonException as ex:
            raise ex

        except Exception as ex:
            raise Exception(ex)
