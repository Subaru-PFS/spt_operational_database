from opdb import models
from sqlalchemy.orm import aliased


def test_relations_consistency():
    # get the first model
    model = next(iter(models.Base.registry.mappers))

    # aliased involves some consistency checks
    aliased(model)
