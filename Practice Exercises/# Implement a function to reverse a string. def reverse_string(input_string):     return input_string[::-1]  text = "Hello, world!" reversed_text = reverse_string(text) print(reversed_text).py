# Create a simple currency converter function.
def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

usd_amount = 100
exchange_rate = 1.18  # USD to EUR
euro_amount = convert_currency(usd_amount, exchange_rate)
print(f"{usd_amount} USD is equal to {euro_amount} EUR")
