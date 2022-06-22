import pydantic


class ModelBase(pydantic.BaseModel):
    pass


class NameAndPIDModel(ModelBase):
    pid: int
    name: str
