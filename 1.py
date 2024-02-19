import re

def validate_email(email):
    # Паттерн для проверки валидности email адреса
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Проверяем соответствие строки паттерну
    if re.match(pattern, email):
        return True
    else:
        return False

# Пример использования
email1 = "example@example.com"
email2 = "invalid_email.com"

print(validate_email(email1))  # True
print(validate_email(email2))  # False