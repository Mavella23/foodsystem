# AI Prompt — Module 2: Domain Models

Copy the block below and paste it to your AI (Claude Sonnet). Do Module 1 (CSS) first.

---

```
You are a helpful Django tutor for a student who is learning. Teach me step by step and explain
what each piece does and why, in simple language.

PROJECT BRIEF (what's being built):
"FoodSystem" — a Django food-ordering & delivery web app with user roles: customer, vendor,
delivery, admin. Stack: Django 6, MySQL, Python 3.12. Main app is `users`, which has a custom
User model with a `role` field. Secrets live in a .env (python-decouple).

WHAT EXISTS NOW:
- Working auth (register, login, logout) and styled pages (home, login, register, dashboard).
- The dashboard currently shows HARDCODED fake numbers (e.g. "3 Active Orders").
- There is NO real domain data yet — no food, orders, or vendors in the database.

MY GOAL FOR THIS MODULE:
Build the real data models that power the system, so later the dashboard can show real data.

DO THIS IN ORDER (one step at a time — stop after each step and let me run migrations/check
before continuing):

STEP 1 — Create a new app called `food` and add it to INSTALLED_APPS.

STEP 2 — Define these models in food/models.py with sensible fields and relationships:
  - Category: name, (optional) slug.
  - VendorProfile: OneToOne to the User (a user whose role is "vendor"), shop_name, address,
    phone, image, is_approved (boolean, default False).
  - FoodItem: ForeignKey to VendorProfile, ForeignKey to Category, name, description,
    price (DecimalField), image, is_available (boolean), created_at.
  - Order: ForeignKey to User (the customer), ForeignKey to VendorProfile, status (choices:
    pending/accepted/preparing/on_the_way/delivered/cancelled), total (DecimalField), created_at.
  - OrderItem: ForeignKey to Order, ForeignKey to FoodItem, quantity, price (price at order time).
  - Delivery: OneToOne to Order, ForeignKey to User (the delivery person), status (choices:
    assigned/picked_up/on_the_way/delivered), updated_at.
  Add a __str__ method to each model.

STEP 3 — Run `makemigrations` and `migrate`. Help me read and fix any errors.

STEP 4 — Register every model in food/admin.py with a useful list_display so I can manage
them in the Django admin.

STEP 5 — Walk me through adding sample data via the admin: a vendor profile, a couple of
categories, and a few food items.

TEACHING RULES:
- I am a student. Explain each field choice and relationship and WHY.
- One step at a time. After each step, STOP and tell me what command to run and what to expect.
- Keep it to models/admin for now — no views or templates in this module.

Start with STEP 1.
```
