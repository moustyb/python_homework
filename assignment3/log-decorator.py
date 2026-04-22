# TASK 1: Writing and Testing a Decorator
import logging
import functools

# One-time logger setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
# Clear existing handlers to avoid duplicate logs in testing
if not logger.handlers:
    logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    """Decorator that logs function name, parameters, and return value."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Format positional parameters
        pos_params = list(args) if args else "none"
        # Format keyword parameters
        kw_params = dict(kwargs) if kwargs else "none"
        
        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_params}\n"
            f"keyword parameters: {kw_params}\n"
            f"return: {result}\n"
        )
        logger.log(logging.INFO, log_message)
        
        return result
    return wrapper


# Function with no parameters, returns nothing
@logger_decorator
def hello_world():
    """Prints Hello, World!"""
    print("Hello, World!")
    return None


# Function with variable positional arguments, returns True
@logger_decorator
def accepts_any_args(*args):
    """Accepts any positional args and returns True."""
    return True


# Function with variable keyword arguments, returns logger_decorator
@logger_decorator
def accepts_kwargs(**kwargs):
    """Accepts any keyword args and returns the logger_decorator function."""
    return logger_decorator


if __name__ == "__main__":
    # Call each decorated function
    hello_world()
    accepts_any_args(1, 2, 3)
    accepts_kwargs(name="Alice", age=30)
    
    print("Check decorator.log for output!")
