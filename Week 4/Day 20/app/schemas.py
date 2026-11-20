from pydantic import BaseModel, EmailStr, Field, ConfigDict


# Used when creating a new user account.
class UserCreate(BaseModel):

    username: str = Field(min_length=3, max_length=50)

    email: EmailStr

    password: str = Field(min_length=8)


# Used to validate login credentials.
class UserLogin(BaseModel):

    email: EmailStr

    password: str


# Defines the user information returned by the API.
class UserResponse(BaseModel):

    id: int

    username: str

    email: EmailStr

    # Allows Pydantic to read data directly from SQLAlchemy models.
    model_config = ConfigDict(from_attributes=True)


# Defines the response returned after successful authentication.
class TokenResponse(BaseModel):

    access_token: str

    token_type: str


# Used when creating a new item.
class ItemCreate(BaseModel):

    title: str = Field(min_length=2, max_length=100)


# Used when updating an existing item's title.
class ItemUpdate(BaseModel):

    title: str = Field(min_length=2, max_length=100)


# Defines the item information returned by the API.
class ItemResponse(BaseModel):

    id: int

    title: str

    owner_id: int

    # Allows Pydantic to convert SQLAlchemy model objects into response data.
    model_config = ConfigDict(from_attributes=True)