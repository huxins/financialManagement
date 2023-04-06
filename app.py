from sqlalchemy.orm import registry, DeclarativeBase

mapper_registry = registry()
Base = mapper_registry.generate_base()