import sys

def error_message_details(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()

    error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message    