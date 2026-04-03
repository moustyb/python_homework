# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"

# Task 3
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
        else:
            return "Invalid operation."
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except Exception:
        return "You can't multiply those values!"

# Task 4
def data_type_conversion(value, type_name):
    try:
        if type_name == "int":
            return int(value)
        elif type_name == "float":
            return float(value)
        elif type_name == "str":
            return str(value)
        else:
            return "Invalid type."
    except Exception:
        return f"You can't convert {value} into a {type_name}."

# Task 5
def grade(*args):
    try:
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except Exception:
        return "Invalid data was provided."

# Task 6
def repeat(text, count):
    result = ""
    for _ in range(count):
        result += text
    return result

# Task 7
def student_scores(mode, **kwargs):
    if mode == "best":
        best_student = None
        best_score = -float("inf")

        for name, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = name

        return best_student

    elif mode == "mean":
        if len(kwargs) == 0:
            return 0
        return sum(kwargs.values()) / len(kwargs)

    else:
        return "Invalid mode."

# Task 8
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()

    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word)
        else:
            result.append(word.capitalize())

    return " ".join(result)


# Task 9
def multiply_list(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

# Task 10
def pig_latin(word):
    try:
        vowels = "aeiouAEIOU"

        if not isinstance(word, str) or len(word) == 0:
            return "Invalid input."

        if word[0] in vowels:
            return word + "yay"
        else:
            return word[1:] + word[0] + "ay"

    except Exception:
        return "Invalid input."# Write your code here.
