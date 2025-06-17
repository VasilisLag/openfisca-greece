from openfisca_core.model_api import *
from openfisca_greece.entities import Household

class residence_location(Variable):
    value_type = str
    entity = Household
    definition_period = YEAR
    label = "Τόπος διαμονής (π.χ. Νομός ή Δήμος)"



class heating_source(Variable):
    value_type = str
    entity = Household
    definition_period = YEAR
    label = "Πηγή θέρμανσης κατοικίας"


class has_rent_contract(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Υπάρχει ενεργό μισθωτήριο συμβόλαιο"


class monthly_rent_amount(Variable):
    value_type = float
    entity = Household
    definition_period = MONTH
    label = "Μηνιαίο ποσό ενοικίου"