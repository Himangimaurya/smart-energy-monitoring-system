from config.settings import UNIT_COST


class BillPredictor:
    def calculate_bill(self, total_energy_kwh):
        """
        Calculate electricity bill
        """
        return round(total_energy_kwh * UNIT_COST, 2)

