import pydantic as pyd


class Base(pyd.BaseModel):
    id: int
    name: str
