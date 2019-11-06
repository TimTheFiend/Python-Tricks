def proxy(func):
    def wrapper(*args, **kwargs):
        """How to use arguments in decorative wrappers
        
        It uses the * and ** operators in the wrapper closure definitino to collect
        all positional and keyword arguments and stores them in variables (args and kwargs)
        
        The wrapper closure then forwards the collected arguments to the original input function using the * and **
        "argument unpacking" operators.
        """
        return func(*args, **kwargs)
    return wrapper


def trace(func):
    """Argumenter i brug.
    
    Her bliver say decorated med trace, så trace kan nu modtage argumenter.
    trace tager says argumenter og sender dem til wrapper som bruger args og kwargs til at arbejde med dem.
    
    Returns:
        [type] -- [description]
    """
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper
@trace
def say(name, line):
    return f"{name}: {line}"
say("Holden", "What I'd do was, I'd pretend to be one of those deaf-mutes.")