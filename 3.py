import random
from string import ascii_lowercase, ascii_uppercase

# Набор символов для генерации паролей
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

def password_generator():
    """
    Генератор случайных паролей длиной 12 символов.
    """
    while True:  # Генерация паролей бесконечна
        yield ''.join(random.choice(chars) for _ in range(12))

# Проверка работы функции-генератора
if __name__ == "__main__":
    gen = password_generator()
    print("Первые пять сгенерированных паролей:")
    for _ in range(5):
        print(next(gen))
