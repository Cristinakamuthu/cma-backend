from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SerializerMixin:
    def to_dict(self, include_relationships=False):
        """
        Convert SQLAlchemy model to dictionary.
        If include_relationships=True, also serialize related objects.
        """
        data = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if hasattr(value, 'isoformat'):  
                value = value.isoformat()
            data[column.name] = value

        if include_relationships:
            for relationship in self.__mapper__.relationships:
                value = getattr(self, relationship.key)
                if value is not None:
                    if isinstance(value, list):
                        data[relationship.key] = [item.to_dict() for item in value]
                    else:
                        data[relationship.key] = value.to_dict()

        return data
