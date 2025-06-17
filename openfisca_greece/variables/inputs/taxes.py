from openfisca_core.model_api import *
from openfisca_greece.entities import Person
from openfisca_core.periods import YEAR

class has_submitted_tax_declaration(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Έχει υποβληθεί φορολογική δήλωση"



class is_tax_resident_greece(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Μόνιμη φορολογική κατοικία στην Ελλάδα"