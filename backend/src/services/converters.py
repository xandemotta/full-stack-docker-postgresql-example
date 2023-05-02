from typing import TypeVar, Type, List

from pydantic import BaseModel

from models import Base

Model = TypeVar("Model", Base, Base)
DTOModel = TypeVar("DTOModel", BaseModel, BaseModel)


def convert_to_dto(model: Type[Model], to: Type[DTOModel]) -> DTOModel:
    return to(**model)


def convert_multiple_to_dto(models: List[Type[Model]], to: Type[DTOModel]) -> List[DTOModel]:
    dto = []
    for model in models:
        dto.append(convert_to_dto(model, to))
    return dto
