from dataclasses import dataclass

from deta_str.services.deta_base_service import BaseModel


@dataclass(kw_only=True, frozen=True)
class SuperModel(BaseModel):
    id: str

    def __post_init__(self):
        BaseModel.__init__(self, **self)