from deta_str.services.deta_base_service import BaseModel
from dataclasses import dataclass
from typing import Union, Any, Optional


@dataclass(kw_only=True, frozen=True)
class SuperModel(BaseModel):
    id: str

    def __post_init__(self):
        BaseModel.__init__(self, **self)