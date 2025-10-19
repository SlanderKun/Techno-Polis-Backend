import hashlib
import os
import re
import secrets

import services.auth_service.io
import services.auth_service.models
import services.auth_service.shemas
import services.user_service.io
import services.user_service.models


def create_hash_password(password: str) -> str:
    """Создаёт соль, хеширует пароль и возвращает строку для базы."""
    salt = os.urandom(16)
    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, 100_000
    )
    return f"{salt.hex()}:{hash_bytes.hex()}"


def validate_hash_password(password_input: str, stored: str) -> bool:
    """Проверяет введённый пароль с сохранённым хешем."""
    salt_hex, hash_hex = stored.split(":")
    salt = bytes.fromhex(salt_hex)
    hash_stored = bytes.fromhex(hash_hex)
    hash_input = hashlib.pbkdf2_hmac(
        "sha256", password_input.encode(), salt, 100_000
    )
    return hash_input == hash_stored


def validate_password(password: str):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{}|;':\",.<>/?]", password):
        return False
    return True


async def create_account(
    data: services.auth_service.shemas.RegisterRequestSchema,
):
    """Создаёт аккаунт пользователя."""
    password_hash = create_hash_password(data.password)
    await services.auth_service.io.create_user(
        email=data.email,
        password_hash=password_hash,
    )


async def create_session_token(
    user_id: int,
    location: str = "default",
) -> str:
    """Создаёт сессионный токен для пользователя."""
    token = secrets.token_urlsafe(32)
    while await services.auth_service.io.session_token_exists(token):
        token = secrets.token_urlsafe(32)
    await services.auth_service.io.create_session_token(
        user_id, token, location
    )
    return token
