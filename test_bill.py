from analytics.bill_prediction import BillPredictor

bill = BillPredictor()

energy_values = [10, 25.5, 72.3]

for energy in energy_values:
    cost = bill.calculate_bill(energy)
    print(f"Energy: {energy} kWh → Bill: ₹{cost}")
