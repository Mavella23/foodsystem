# AI Prompt — Module 4: Vendor Module

Copy the block below and paste it to your AI (Claude Sonnet). Do Module 3 (Customer) first.

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
- `food` app models: Category, VendorProfile, FoodItem, Order, OrderItem, Delivery.
- The customer module works: customers can browse food and place orders (creating Orders for vendors).

MY GOAL FOR THIS MODULE:
Let a VENDOR manage their menu and handle incoming orders.

DO THIS IN ORDER (one step at a time — stop after each and let me test in the browser):

STEP 1 — My Menu (CRUD): list the logged-in vendor's FoodItems, plus add / edit / delete.
Use Django ModelForms. A vendor must only see and edit THEIR OWN items.

STEP 2 — Incoming Orders: list Orders placed for this vendor, with the ability to update an
order's status (e.g. accept, preparing, ready). Show order details (the OrderItems).

STEP 3 — Vendor Profile: let the vendor edit their VendorProfile (shop name, address, phone, image).

STEP 4 — Wire these into the vendor's dashboard sidebar links (which already exist), and make
the vendor stat cards show real counts (menu items, pending orders) instead of hardcoded numbers.

TEACHING RULES:
- I am a student. Explain ModelForms, ownership checks, and status updates clearly and WHY.
- One step at a time. After each step, STOP and tell me how to test it in the browser.
- Enforce that only users with role "vendor" can access these pages, and only on their own data.
- Keep styling consistent with the existing main.css.

Start with STEP 1.
```
