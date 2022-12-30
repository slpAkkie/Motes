from re import finditer


def camel_case_split(string: str) -> list:
    matches = finditer(
        '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', string)
    return [m.group(0) for m in matches]
