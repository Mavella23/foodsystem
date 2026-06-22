# FoodSystem — Build Roadmap

A food ordering & delivery system with four user roles: **customer, vendor, delivery, admin**.

This roadmap is written so that — even when using an AI as a teacher — the student always knows:
**what** the module is, **how** to approach it, and **what output (deliverables)** to expect.

> **Learning rule:** finish one module completely (all deliverables met) before moving to the next.
> Don't jump ahead. Each module ends with a working, demonstrable result.

---

## Module 0 — Secrets → Environment Variables  ⬅️ START HERE

**What:**
Move all sensitive values out of `settings.py` and into a `.env` file that is never committed
to git. Provide a `.env.example` so teammates know which variables to set.

**How:**
1. Install `python-decouple` (`pip install python-decouple`).
2. Create `.env` in the project root with the real values:
   `SECRET_KEY`, `DEBUG`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.
3. Create `.env.example` with the same keys but placeholder values (this one IS committed).
4. Add `.env` to `.gitignore`.
5. In `settings.py`, import `config` from `decouple` and replace the hardcoded values:
   `SECRET_KEY = config('SECRET_KEY')`, `DEBUG = config('DEBUG', cast=bool)`,
   and the `DATABASES` credentials with `config('DB_...')`.
6. Run `python manage.py check` and `runserver` to confirm nothing broke.

**Deliverables:**
- `settings.py` contains **no** hardcoded secrets — only `config('...')` calls.
- `.env` exists locally and is git-ignored (confirm with `git status` — it must NOT appear).
- `.env.example` is committed with placeholder values.
- App still runs exactly as before.

---

## Module 1 — UI & Styling (CSS)

**What:**
Make the existing pages (home, login, register, dashboard) look good, consistent, and
mobile-responsive — using a **single `main.css`** as the project's one stylesheet.

**How:**
1. **Fix template inheritance first (mandatory).** Currently `home.html`, `login.html`,
   `register.html`, `dashboard.html` each have their own `<!DOCTYPE>`/`<head>` and do NOT use
   `{% extends 'base.html' %}`, so no CSS reaches them. Convert each to extend `base.html`
   and put its content inside `{% block content %}`.
2. **Consolidate CSS into one file.** Replace the four linked files (base/layout/components/page)
   with a single `main.css`. Update `base.html` to link only `main.css`. Delete the old empty files.
3. **Organize `main.css` by clear sections** (with comment headers): Reset & Variables,
   Typography, Buttons, Navbar, Forms, Cards, Alerts, Dashboard (sidebar + grid), Pages (home/auth).
4. **Fix form input classes.** In `forms.py`, add widget `attrs` so register inputs get the
   `form-input` class (the template already expects it).
5. **Style the role-based dashboard** — the sidebar and stat cards already branch per role in HTML;
   give them proper styling.
6. Use a food-themed palette (e.g. warm orange + green) and add media queries for mobile.

**Deliverables:**
- All four pages extend `base.html` (one navbar, one stylesheet).
- One `main.css` exists; the old split CSS files are gone; no CSS link 404s.
- Login, Register, Home, Dashboard are fully styled and visually consistent.
- Layout works on both mobile and desktop (responsive).
- Dashboard shows a correctly styled, role-specific sidebar and cards.

---

## Module 2 — Domain Models (the core data)

**What:**
Build the real data models behind the food system, so the dashboard shows real data instead
of the current hardcoded fake numbers.

**How:**
1. Create a new app (e.g. `food` or `orders`).
2. Define models: `VendorProfile`, `Category`, `FoodItem`, `Order`, `OrderItem`, `Delivery`,
   with proper relationships (ForeignKeys) and fields (name, price, status, timestamps, etc.).
3. Register every model in `admin.py`.
4. `makemigrations` + `migrate`, then add sample data through the Django admin.

**Deliverables:**
- All models created and migrated with no errors.
- Every model is manageable in Django Admin.
- Sample vendors, categories, and food items exist for testing.

---

## Module 3 — Customer Module

**What:** Let a customer browse food and place an order end-to-end.

**How:**
1. Browse Food page — list `FoodItem`s with filtering by category/vendor and pagination.
2. Food detail page.
3. Cart — add/remove items and change quantity.
4. Place Order — create an `Order` + `OrderItem`s from the cart.
5. My Orders — order history with current status.

**Deliverables:**
- A customer can go from browsing → cart → placed order → seeing it in "My Orders".

---

## Module 4 — Vendor Module

**What:** Let a vendor manage their menu and incoming orders.

**How:**
1. My Menu — full CRUD on the vendor's `FoodItem`s (add/edit/delete).
2. Orders — view incoming orders, accept/reject, update status.
3. Vendor profile — edit shop details.

**Deliverables:**
- A vendor can manage a menu and process real incoming orders.

---

## Module 5 — Delivery Module

**What:** Let a delivery person manage assigned deliveries.

**How:**
1. Deliveries — list orders assigned to this delivery person.
2. Update delivery status (picked up → on the way → delivered).

**Deliverables:**
- A delivery person can track and complete a delivery, updating its status.

---

## Module 6 — Admin Module

**What:** Let an admin manage the whole system and see real metrics.

**How:**
1. Users — list, enable/disable users.
2. Vendors — approve/reject vendors.
3. Reports — real statistics (orders, revenue, users).

**Deliverables:**
- Admin dashboard shows REAL numbers (replacing today's hardcoded values).

---

## Module 7 — Security & Access Control

**What:** Make sure each role only sees what it should, and clean up known issues.

**How:**
1. Add role-based access control — restrict each dashboard/view to the correct role
   (currently any logged-in user can open the dashboard).
2. Redirect users by role after login.
3. Add form validation and clear error messages everywhere.
4. Fix the `urls.W005` warning (admin is currently included twice).
5. Remove junk files: `settings.py.save`, `migrations/_init_.py`.
6. Rotate old secrets (the old MySQL password and SECRET_KEY are still in git history).

**Deliverables:**
- Each role is correctly restricted; no cross-role access.
- No system-check warnings; junk files removed; secrets rotated.

---

## Module 8 — Testing & Deployment

**What:** Make the project reproducible and production-ready.

**How:**
1. Create `requirements.txt` (pin Django, mysqlclient, python-decouple).
2. Write basic tests for key models and views.
3. Set `DEBUG=False` + configure `ALLOWED_HOSTS` for production.
4. Configure static files (`collectstatic`) and media files.
5. Write a README explaining setup (especially for the Ubuntu teammate).

**Deliverables:**
- Anyone can clone, install from `requirements.txt`, set `.env`, and run the project.
- Tests pass; production settings are in place.

---

## Roadmap at a glance

```
[0] Secrets→.env  ⬅️ START
   └▶ [1] CSS (single main.css)
      └▶ [2] Models
         └▶ [3] Customer ─▶ [4] Vendor ─▶ [5] Delivery ─▶ [6] Admin
            └▶ [7] Security ─▶ [8] Testing & Deployment
```

**Golden rule:** every module must be finished and demonstrable before starting the next.
