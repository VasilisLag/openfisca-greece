from openfisca_core.model_api import *
from openfisca_greece.entities import Person, Household
from openfisca_core.periods import YEAR, MONTH

class permanent_residence_in_greece(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Μόνιμη διαμονή στην Ελλάδα"

class years_of_residence_in_greece(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Έτη μόνιμης διαμονής στην Ελλάδα"

class marital_status(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Οικογενειακή κατάσταση"


class number_of_dependent_children(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Αριθμός εξαρτώμενων τέκνων"


class number_of_unprotected_children(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Αριθμός απροστάτευτων τέκνων"


class number_of_hosted_members(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Αριθμός φιλοξενούμενων μελών"


class has_vulnerable_household_members(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Υπάρχουν ευάλωτα μέλη στο νοικοκυριό"