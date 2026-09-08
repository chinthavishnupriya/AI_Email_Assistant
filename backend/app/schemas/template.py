from pydantic import BaseModel, Field, ConfigDict


class TemplateCreate(BaseModel):

    name: str = Field(..., min_length=2, max_length=100)

    category: str = Field(..., min_length=2, max_length=50)

    content: str = Field(..., min_length=10)


class TemplateUpdate(BaseModel):

    name: str = Field(..., min_length=2, max_length=100)

    category: str = Field(..., min_length=2, max_length=50)

    content: str = Field(..., min_length=10)


class TemplateResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    name: str
    category: str
    content: str
    created_at: object
    updated_at: object
