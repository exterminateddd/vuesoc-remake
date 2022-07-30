from typing import TypedDict, Literal


class PersonalData(TypedDict):
    password: str
    username: str
    email: str


class UserLoginData(TypedDict):
    mode: Literal["username", "email"]
    user_data: PersonalData
