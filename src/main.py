from booking_operator import BookingOperator
from states import states

driver = BookingOperator()

results = {}
for state in states:
    results[state] = ()

for state in states:
    results[state] = driver.select_page(
        location=state, checkin="2024-12-01", checkout="2024-12-02"
    )
    location, prices = results[state]
    print(
        f"Intended Location: {state}, Actual Location: {location}, Average: {sum(prices)/len(prices)}, Num Results: {len(prices)}"
    )
