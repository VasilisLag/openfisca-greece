# .venv\Scripts\activate
# cd openfisca-greece
# py run.py

from openfisca_greece import CountryTaxBenefitSystem
from openfisca_web_api.app import create_app

app = create_app(CountryTaxBenefitSystem())

if __name__ == "__main__":
    app.run(debug=True, port=5000)