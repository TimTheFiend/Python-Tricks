"""
Let's say you wanted to validate an input string representing a person's name in your application.
A Toy example for a name validator function might look like this:
"""
#region Example of what you *can* do
def validatefoobar(name):
    if len(name) < 10:
        raise ValueError
"""The downside being that the error message won't specify the error, only say that a ValueError was raised."""
#endregion

#region example of how to make custom exception class
class NametoShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NametoShortError(name)

validate("howdy") # Output: raise NametoShortError(name)
#endregion

#region
class BaseValidationError(ValueError):
    pass
class NameTooShortError(BaseValidationError):
    pass
class NameTooLongError(BaseValidationError):
    pass
class NameTooCuteError(BaseValidationError):
    pass

try:
    validate("audi")
except BaseValidationError as err:
    """handle_validation_error er psuedo kode men kan bruges til at handle exceptions"""
    handle_validation_error(err)

#endregion