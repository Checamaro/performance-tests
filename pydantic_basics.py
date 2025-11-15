"""
{
  "account": {
    "id": "string",
    "type": "UNSPECIFIED",
    "cards": [
      {
        "id": "string",
        "pin": "string",
        "cvv": "string",
        "type": "UNSPECIFIED",
        "status": "UNSPECIFIED",
        "accountId": "string",
        "cardNumber": "string",
        "cardHolder": "string",
        "expiryDate": "2025-11-15",
        "paymentSystem": "UNSPECIFIED"
      }
    ],
    "status": "UNSPECIFIED",
    "balance": 0
  }
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict,HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
from datetime import date


class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

try:
    tariff = DocumentSchema(
        url="localhost",
        document="document data"
    )
except ValidationError as error:
    print(error)
    print(error.errors())

class CardSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    pin: str
    cvv: str
    type: str
    status: str
    account_id: str = Field(alias="accountId", default="account-id")
    card_number: str = Field(alias="cardNumber", default="1234123412341234")
    card_holder: str = Field(alias="cardHolder", default="Alice Smith")
    expiry_date: date = Field(alias="expiryDate", default=date(2027, 3, 25))
    payment_system: str = Field(alias="paymentSystem", default="VISA")


class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "CREDIT_CARD"
    cards: list[CardSchema] = Field(default_factory=list)
    status: str = "ACTIVE"
    balance: float = 25000

    def get_account_name(self) -> str:
        return f"{self.status} {self.type}"


account_default_model = AccountSchema(
    id="account id",
    type="CREDIT_CARD",
    cards=[
        CardSchema(
            id="card-id",
            pin="1234",
            cvv="123",
            type="PHYSICAL",
            status="ACTIVE",
            accountId="account-id",
            cardNumber="1234123412341234",
            cardHolder="Alice Smith",
            expiryDate=date(2027, 3, 25),
            paymentSystem="VISA"
        )
    ],
    status="ACTIVE",
    balance=100.57
)
print("Account default model:", account_default_model)

account_dict = {
    "id": "account id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alice Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 777.11
}
account_dict_model = AccountSchema(**account_dict)
print("Account dict model:", account_dict_model)

account_json = """
{
    "id": "account id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "1234123412341234",
            "cardHolder": "Alice Smith",
            "expiryDate": "2027-03-25",
            "paymentSystem": "VISA"
        }
    ],
  "status": "ACTIVE",
  "balance": 777.11
}
"""

account_json_model = AccountSchema.model_validate_json(account_json)
print("Account JSON model:", account_json_model)
