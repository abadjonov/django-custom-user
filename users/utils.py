from random import randint


def generate_otp() -> str:
    return str(randint(100_000, 999_999))
