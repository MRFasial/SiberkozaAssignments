# Example of a custom module to be imported

import re


def validate_email(email_mr):
    if len(email_mr) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email_mr))
