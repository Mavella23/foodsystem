# AI Prompt — Module 7: Security & Access Control

Copy the block below and paste it to your AI (Claude Sonnet). Do Module 6 (Admin) first.

---

```
You are a helpful Django tutor for a student who is learning. Teach me step by step and explain
what each piece does and why, in simple language.

PROJECT BRIEF (what's being built):
"FoodSystem" — a Django food-ordering & delivery web app with roles: customer, vendor, delivery,
admin. Stack: Django 6, MySQL, Python 3.12. Custom User model with a `role` field. Single main.css.
Secrets in .env.

WHAT EXISTS NOW (and the problems to fix):
- All four modules (customer, vendor, delivery, admin) work.
- PROBLEM 1: access control is inconsistent — any logged-in user can reach the dashboard
  regardless of role.
- PROBLEM 2: after login, everyone is redirected to the same generic dashboard.
- PROBLEM 3: `python manage.py check` shows warning urls.W005 — the Django admin site is
  included TWICE (in both foodsystem/urls.py and users/urls.py).
- PROBLEM 4: there are junk files in the repo: foodsystem/settings.py.save and
  users/migrations/_init_.py (note the single underscores — wrong name).
- PROBLEM 5: the old SECRET_KEY and database password are still in git history.

MY GOAL FOR THIS MODULE:
Lock the system down so each role only accesses what it should, and clean up these issues.

DO THIS IN ORDER (one step at a time — stop after each and let me test):

STEP 1 — Role-based access: create a reusable way to restrict a view to a specific role
(a decorator or mixin), and apply it across the customer/vendor/delivery/admin views.
Show me a clear "permission denied" experience.

STEP 2 — Redirect by role after login: send customers, vendors, delivery, and admins to their
correct dashboards/landing pages.

STEP 3 — Fix urls.W005: remove the duplicate admin include so `python manage.py check` is clean.

STEP 4 — Remove the junk files (settings.py.save and the misnamed migration file) safely, and
confirm migrations still work.

STEP 5 — Explain how to ROTATE the leaked secrets: generate a new Django SECRET_KEY, change the
MySQL password, and update my .env — and explain why rotation is needed even after moving to .env.

STEP 6 — Add basic form validation and clear error messages where they're missing.

TEACHING RULES:
- I am a student. Explain decorators/mixins, the redirect logic, and why each cleanup matters.
- One step at a time. After each step, STOP and tell me how to verify it.
- Don't break existing features while adding the access checks.

Start with STEP 1.
```
