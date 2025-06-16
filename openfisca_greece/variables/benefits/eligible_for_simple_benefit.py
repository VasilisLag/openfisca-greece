from openfisca_core.model_api import *
from openfisca_greece.entities import Person

class eligible_for_simple_benefit(Variable):
    value_type = bool
    entity = Person
    label = "Επιλεξιμότητα για απλό επίδομα"
    definition_period = YEAR

    def formula(persons, period, parameters):
        return persons("salary", period.this_year, options=[ADD]) < 12000
