from openfisca_core.model_api import *
from openfisca_greece.entities import Person

class has_car(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Διαθέτει αυτοκίνητο"