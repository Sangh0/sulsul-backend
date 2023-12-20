from typing import List
from pydantic import BaseModel

from core.domain.combination_model import Combination
from core.dto.pairing_dto import PairingResponse


class CombinationResponse(BaseModel):
    id: int
    alcohol: PairingResponse
    food: PairingResponse
    count: int
    description: str | None

    # @classmethod
    # def from_orm(cls, entity: Combination):
    #     dto = super().from_orm(entity)
    #     dto.alcohol = PairingResponse.from_orm(entity.alchohol)
    #     dto.food = PairingResponse.from_orm(entity.food)
    #     return dto

    @classmethod
    def from_orm(cls, entity: Combination):
        return CombinationResponse(
            **entity.__data__,
            alcohol=PairingResponse.from_orm(entity.alcohol),
            food=PairingResponse.from_orm(entity.food),
        )


class CombinationListResponse(BaseModel):
    combinations: List[CombinationResponse]
