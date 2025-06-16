from openfisca_core.model_api import *
from openfisca_greece.entities import Person

class eligible_for_car_allowance(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Επιλεξιμότητα για επίδομα αυτοκινήτου"

    def formula(persons, period, parameters):
        income = persons("salary", period.this_year, options=[ADD])
        return (income < 12000) & (persons("has_car", period.this_year))