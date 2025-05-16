from datetime import datetime


def validate_year(year):
    try:
        year = int(year)
    except ValueError:
        raise ValueError("Рік має бути цілим числом")

    current_year = datetime.now().year
    if year > current_year:
        raise ValueError(f"Рік не може бути більшим за поточний ({current_year})")

    if year < 0:
        raise ValueError("Рік не може бути від'ємним")

    return year


def validate_text_length(text, field_name, max_length):
    if not text or text.strip() == "":
        raise ValueError(f"{field_name} не може бути порожнім")

    if len(text) > max_length:
        raise ValueError(f"{field_name} не може бути довшим за {max_length} символів")

    return text