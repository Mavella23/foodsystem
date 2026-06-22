# AI Prompt — Module 8: Testing & Deployment

Copy the block below and paste it to your AI (Claude Sonnet). Do Module 7 (Security) first.

---

```
You are a helpful Django tutor for a student who is learning. Teach me step by step and explain
what each piece does and why, in simple language.

PROJECT BRIEF (what's being built):
"FoodSystem" — a Django food-ordering & delivery web app with roles: customer, vendor, delivery,
admin. Stack: Django 6, MySQL, Python 3.12. Custom User model with a `role` field. Single main.css.
Secrets in .env (python-decouple). All feature modules are complete and access-controlled.

MY GOAL FOR THIS MODULE:
Make the project reproducible for teammates and ready for production.

DO THIS IN ORDER (one step at a time — stop after each and let me run it):

STEP 1 — Dependencies: create a requirements.txt pinning the project's packages
(Django, mysqlclient, python-decouple, and anything else installed). Explain how a teammate
would install from it.

STEP 2 — Tests: write a few basic tests — for the custom User/role, one model, and one key view
(e.g. placing an order or role-based access). Show me how to run them with `python manage.py test`.

STEP 3 — Production settings: explain DEBUG=False and configuring ALLOWED_HOSTS via .env, and
what changes when DEBUG is off (static files, error pages).

STEP 4 — Static & media files: configure STATIC_ROOT and MEDIA settings, and explain
`collectstatic` and how uploaded images (food/vendor) are served.

STEP 5 — README: help me write a clear README so a teammate (on Ubuntu) can clone, create a
venv, install from requirements.txt, copy .env.example to .env, run migrations, and start the app.

TEACHING RULES:
- I am a student. Explain each production concept and WHY it matters.
- One step at a time. After each step, STOP and tell me what to run and what to expect.
- Keep it practical for a student project — don't over-engineer the deployment.

Start with STEP 1.
```
