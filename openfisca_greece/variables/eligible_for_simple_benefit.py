from openfisca_core.model_api import *
from openfisca_greece.entities import Person

class eligible_for_simple_benefit(Variable):
    value_type = bool
    entity = Person
    label = "Επιλεξιμότητα για απλό επίδομα"
    definition_period = MONTH

    def formula(persons, period, parameters):
        return persons("salary", period) < 12000
