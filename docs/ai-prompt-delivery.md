# AI Prompt — Module 5: Delivery Module

Copy the block below and paste it to your AI (Claude Sonnet). Do Module 4 (Vendor) first.

---

```
You are a helpful Django tutor for a student who is learning. Teach me step by step and explain
what each piece does and why, in simple language.

PROJECT BRIEF (what's being built):
"FoodSystem" — a Django food-ordering & delivery web app with roles: customer, vendor, delivery,
admin. Stack: Django 6, MySQL, Python 3.12. Custom User model with a `role` field. Single main.css.
Secrets in .env.

WHAT EXISTS NOW:
- Auth + styled role-based dashboard.
- `food` app models including Order and Delivery (Delivery is OneToOne to Order with a
  delivery_person ForeignKey to User and a status field).
- Customers place orders; vendors accept and prepare them.

MY GOAL FOR THIS MODULE:
Let a DELIVERY person see assigned deliveries and update their status.

DO THIS IN ORDER (one step at a time — stop after each and let me test in the browser):

STEP 1 — Deliveries list: show Deliveries assigned to the logged-in delivery person, with the
order details (customer, vendor, items, address).

STEP 2 — Update status: let the delivery person move a delivery through its statuses
(assigned -> picked_up -> on_the_way -> delivered), updating the related Order status too.

STEP 3 — (Explain the assignment step) Show me how a delivery gets assigned to a delivery
person — either automatically when a vendor marks an order ready, or by an admin. Pick the
simplest approach and explain it.

STEP 4 — Wire these into the delivery dashboard sidebar links and make the delivery stat cards
show real counts (e.g. active deliveries) instead of hardcoded numbers.

TEACHING RULES:
- I am a student. Explain the status flow and the assignment logic clearly and WHY.
- One step at a time. After each step, STOP and tell me how to test it in the browser.
- Enforce that only users with role "delivery" can access these pages, and only their own deliveries.
- Keep styling consistent with the existing main.css.

Start with STEP 1.
```
