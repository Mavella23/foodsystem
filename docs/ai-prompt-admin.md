# AI Prompt — Module 6: Admin Module

Copy the block below and paste it to your AI (Claude Sonnet). Do Module 5 (Delivery) first.

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
- Working customer, vendor, and delivery modules with real Orders, FoodItems, and Deliveries.
- The admin dashboard stat cards still show HARDCODED numbers (e.g. "120 Total Users").
- This is a CUSTOM in-app admin area for the "admin" role — separate from Django's built-in
  /admin site.

MY GOAL FOR THIS MODULE:
Give the "admin" role a control panel to manage the system and see REAL metrics.

DO THIS IN ORDER (one step at a time — stop after each and let me test in the browser):

STEP 1 — Users management: list all users with their role, and let the admin enable/disable a
user (toggle is_active).

STEP 2 — Vendor approval: list VendorProfiles and let the admin approve/reject them
(toggle is_approved). Unapproved vendors' food should not show to customers.

STEP 3 — Reports: compute and display REAL statistics — total users, total vendors, orders today,
and total revenue — using Django ORM aggregates (count, sum).

STEP 4 — Replace the hardcoded numbers in the admin dashboard stat cards with these real values.

TEACHING RULES:
- I am a student. Explain ORM queries and aggregates (Count, Sum) clearly and WHY.
- One step at a time. After each step, STOP and tell me how to test it in the browser.
- Enforce that only users with role "admin" can access these pages.
- Keep styling consistent with the existing main.css.

Start with STEP 1.
```
