"""This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

# Import from openfisca-core the objects used to code the legislation in OpenFisca
from openfisca_core.holders import set_input_divide_by_period
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.populations import DIVIDE
from openfisca_core.variables import Variable

# Import the Entities specifically defined for this tax and benefit system
from openfisca_greece.entities import Household, Person


class annual_household_income(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Ετήσιο οικογενειακό εισόδημα"



class last_six_months_household_income(Variable):
    value_type = float
    entity = Household
    definition_period = MONTH  # Δεκτό ανά μήνα, μπορούμε να ζητήσουμε για 6 μήνες
    label = "Εισόδημα νοικοκυριού τελευταίου εξαμήνου"


class has_business_activity(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ασκεί επιχειρηματική δραστηριότητα"


class business_gross_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ακαθάριστα έσοδα από επιχειρηματική δραστηριότητα"