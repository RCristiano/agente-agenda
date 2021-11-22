# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import (
    Email,
    DataRequired,
    EqualTo,
    Length,
    ValidationError,
)

# login and registration


class LoginForm(FlaskForm):
    username = TextField(
        "Username", id="username_login", validators=[DataRequired()]
    )
    password = PasswordField(
        "Password", id="pwd_login", validators=[DataRequired()]
    )


class CreateAccountForm(FlaskForm):
    username = TextField(
        "Username",
        id="username_create",
        validators=[DataRequired(), Length(min=5, max=64)],
    )
    email = TextField(
        "Email", id="email_create", validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password", id="pwd_create", validators=[DataRequired(), Length(min=6)]
    )
    confirm_password = PasswordField(
        "Repeat Password",
        id="confirm_pwd_create",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    prestador = BooleanField(
        "Sou profissional, prestador ou possuo um estabelecimento.",
        id="prestador_create",
    )

    def validate_username(self, username):
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in username.data:
            if char in excluded_chars:
                raise ValidationError(
                    f"Character {char} is not allowed in username."
                )
