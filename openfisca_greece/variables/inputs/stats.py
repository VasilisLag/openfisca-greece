from openfisca_core.model_api import *
from openfisca_greece.entities import Household

class real_estate_objective_value(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    set_input = True
    label = "Συνολική αντικειμενική αξία ακίνητης περιουσίας (βάσει ΕΝΦΙΑ)"


class total_financial_assets(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    set_input = True
    label = "Συνολικό ποσό καταθέσεων, μετοχών, ομολόγων και λοιπών περιουσιακών στοιχείων"


class car_expense_objective(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    set_input = True
    label = "Αντικειμενική δαπάνη των επιβατικών αυτοκινήτων (Ι.Χ./Μ.Χ.)"


class has_luxury_assets(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    set_input = True
    label = "Υπάρχουν στοιχεία πολυτελούς διαβίωσης (π.χ. δίδακτρα, προσωπικό, σκάφη)"