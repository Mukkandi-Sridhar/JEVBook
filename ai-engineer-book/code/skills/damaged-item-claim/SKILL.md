---
name: damaged-item-claim
description: Handle a claim that an item arrived damaged or stopped
  working. Use when a customer reports a broken, cracked, leaking,
  faulty or dead item, in any language.
---

# Damaged item claims

1. Look up the order with check_order_status. A claim must be made
   within 48 hours of delivery (policy section 4). If it is later,
   say so politely and hand the chat to a person.
2. Ask for one clear photo of the damage if none is attached. Do not
   ask for a second photo unless the first is unreadable.
3. Offer a replacement first, and a refund if the customer prefers
   one or the item is out of stock. Hygiene items (policy section 3)
   qualify too, because the item is faulty.
4. Book the courier pickup by running
   `scripts/book_pickup.py ORDER_ID`. It prints the pickup date.
5. For pin codes on the Andaman and Nicobar or Lakshadweep islands,
   read `reference/remote-areas.md` before promising a pickup date.
6. End by telling the customer the pickup date and that the refund
   or replacement starts after the item passes our check.
