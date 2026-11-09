"""Book a courier pickup for a damaged item (stand-in for the courier's API)."""
import sys
from datetime import date, timedelta

order_id = sys.argv[1]
print(f"Pickup for {order_id} booked for {date.today() + timedelta(days=2):%d %b}.")
