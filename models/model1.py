from dataclasses import dataclass

from kernel.base_model import BaseModel


@dataclass
class Model1(BaseModel):

    name: str
    age: int
    country: str
