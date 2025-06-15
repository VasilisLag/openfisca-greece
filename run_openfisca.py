from openfisca_core.scripts import build_tax_benefit_system
from openfisca_web_api.app import create_app

tax_benefit_system = build_tax_benefit_system("openfisca_greece", extensions=None, reforms=None)

app = create_app(tax_benefit_system)

if __name__ == "__main__":
    app.run(port=5000)