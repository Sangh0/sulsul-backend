from datetime import datetime

import peewee

from core.config.orm_config import db
from core.config.var_config import KST, DB_SCHEMA


class BaseEntity(peewee.Model):
    class Meta:
        database = db
        schema = DB_SCHEMA

    id = peewee.AutoField(primary_key=True)
    created_at = peewee.DateTimeField(
        default=datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S%z")
    )
    updated_at = peewee.DateTimeField(
        default=datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S%z")
    )
    is_deleted = peewee.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S%z")
        return super().save(*args, **kwargs)

    @classmethod
    def props(cls) -> dict[str, any]:
        return {
            prop: typ
            for prop, typ in dict(cls.__dict__).items()
            if isinstance(typ, peewee.FieldAccessor)
        }
