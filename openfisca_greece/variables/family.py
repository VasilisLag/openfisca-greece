from datetime import date

# Import from numpy the operations you need to apply on OpenFisca's population vectors
# Import from openfisca-core the objects used to code the legislation in OpenFisca
from numpy import where

from openfisca_core.periods import ETERNITY, MONTH, YEAR
from openfisca_core.variables import Variable

# Import the Entities specifically defined for this tax and benefit system
from openfisca_greece.entities import Person, Household

class num_dependent_children(Variable):
    value_type = int
    entity = Household
    label = "Αριθμός εξαρτώμενων τέκνων"
    definition_period = YEAR


class is_single_parent(Variable):
    value_type = bool
    entity = Household
    label = "Μονογονεϊκή οικογένεια"
    definition_period = YEAR