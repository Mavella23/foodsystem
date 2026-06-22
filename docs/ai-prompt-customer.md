# AI Prompt — Module 3: Customer Module

Copy the block below and paste it to your AI (Claude Sonnet). Do Module 2 (Models) first.

---

```
You are a helpful Django tutor for a student who is learning. Teach me step by step and explain
what each piece does and why, in simple language.

PROJECT BRIEF (what's being built):
"FoodSystem" — a Django food-ordering & delivery web app with roles: customer, vendor, delivery,
admin. Stack: Django 6, MySQL, Python 3.12. Custom User model with a `role` field. Styling is a
single main.css. Secrets in .env.

WHAT EXISTS NOW:
- Auth + styled pages + a role-based dashboard.
- A `food` app with models: Category, VendorProfile, FoodItem, Order, OrderItem, Delivery.
- Sample food data exists in the database.

MY GOAL FOR THIS MODULE:
Let a CUSTOMER browse food and place an order from start to finish.

DO THIS IN ORDER (one step at a time — stop after each and let me test in the browser):

STEP 1 — Browse Food: a view + template listing available FoodItems, with filtering by
category/vendor and pagination. Reuse the existing main.css styles (cards).

STEP 2 — Food detail page: show one FoodItem with an "Add to cart" button.

STEP 3 — Cart: implement a session-based cart (add item, change quantity, remove item) and a
cart page showing items and total.

STEP 4 — Place Order: a view that turns the cart into an Order + OrderItems (saving the price
at order time), clears the cart, and shows a success message.

STEP 5 — My Orders: a page listing the logged-in customer's orders with their current status.

STEP 6 — Wire these into the customer's dashboard sidebar links (which already exist).

TEACHING RULES:
- I am a student. Explain views, URLs, templates, and the cart logic clearly and WHY.
- One step at a time. After each step, STOP and tell me how to test it in the browser.
- Keep styling consistent with the existing main.css. Add only small CSS additions if needed.
- Make sure only logged-in customers can access these pages.

Start with STEP 1.
```
