from enum import Enum

from pydantic import BaseModel
from pydantic.v1 import root_validator

from app.exceptions.validation_exception import ValidationException


class PrivacyPolicyAgreement(Enum):
    AGREE = "agree"
    DISAGREE = "disagree"


class UserSignup(BaseModel):
    email: str
    password: str
    age: int
    privacy_policy: PrivacyPolicyAgreement
