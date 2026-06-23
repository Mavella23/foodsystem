# AI Prompt — Module 1: UI & Styling (CSS)

Do **Module 0 (secrets → .env)** first. Then copy the block below and paste it to your AI
(Claude Sonnet). It gives the AI a short brief of what's being built and what already exists,
so its output fits the project — and fixes anything that's set up wrong before styling.

> Why this prompt is specific: the project has structural problems — the pages don't extend
> `base.html`, there are several empty CSS files, and the form inputs miss their CSS class.
> The prompt tells the AI to FIX those first, otherwise the CSS will not apply at all.

---

```
you are a helpful Django + CSS tutor for a student who is learning. Teach me step by step —
explain what you do and why, in simple language.

PROJECT BRIEF (what's being built):
"FoodSystem" — a Django food-ordering & delivery web app with user roles: customer, vendor,
delivery, admin. Stack: Django 6, MySQL, Python 3.12, a custom User model with a `role` field.
Main app is `users`. Templates live in `users/templates/`, CSS in `users/static/css/`.

MY GOAL FOR THIS MODULE:
Style the existing pages — home, login, register, and dashboard — so they look good, are
consistent, and are mobile-responsive. Use a SINGLE stylesheet called `main.css` (one CSS file
for the whole project), not multiple CSS files.

WHAT ALREADY EXISTS (read carefully — some of it is set up wrong and must be fixed first):
- `base.html` is the layout template: it has the navbar and a `{% block content %}`, and it
  currently links four CSS files (base, layout, components, page).
- PROBLEM 1: home.html, login.html, register.html, dashboard.html each have their OWN
  <!DOCTYPE>/<head> and do NOT use `{% extends 'base.html' %}`. So the linked CSS never
  reaches them.
- PROBLEM 2: three of the CSS files are EMPTY; only base.css has content. There's also a
  filename mismatch (base.html links `pages.css` but the file is `page.css`).
- PROBLEM 3: register.html expects its inputs to have the class `form-input`, but `forms.py`
  does not add that class to the form widgets.
- The dashboard already branches its sidebar and stat cards per role in the HTML.

DO THIS IN ORDER (one step at a time — stop after each and let me run it before continuing):

STEP 1 — Fix the structure (mandatory before any styling):
  a) Convert home.html, login.html, register.html, dashboard.html to use
     `{% extends 'base.html' %}` and move their content into `{% block content %}`.
     Remove the duplicated <!DOCTYPE>, <html>, <head>, <body>.
  b) Switch to a SINGLE stylesheet: make `base.html` link only `css/main.css`, create
     `main.css`, and delete the old base/layout/components/page CSS files.
  c) In forms.py, add widget attrs so the register inputs get the `form-input` class.

STEP 2 — Write main.css (one file, organized with clear comment-header sections):
  Reset & CSS variables (food-themed palette, e.g. warm orange + green), Typography,
  Buttons (.btn, .btn-primary, .btn-outline), Navbar, Forms (.form-group, .form-input,
  .form-label, .form-error), Cards & .stat-card, Alerts, Dashboard (sidebar + grid),
  Pages (hero on home, .auth-card on login/register). Include media queries for mobile.

STEP 3 — Polish the role-based dashboard:
  Make sure the sidebar and stat cards look good for every role (customer, vendor,
  delivery, admin). The HTML structure is already there — just style it.

TEACHING RULES (important):
- I am a student. Explain every change and WHY, in simple language.
- One step at a time. After each step, STOP and tell me to run `python manage.py runserver`
  and report what I see before you continue.
- Do NOT change views or models logic — this is templates + CSS only.
- Write clean, commented CSS so I can follow it.

Start with STEP 1a: show me the converted home.html and explain it.
```

---
You
## Tips for the student

- After each step: run `python manage.py runserver` and open the pages in the browser.
- If CSS changes don't show up, hard-refresh with **Ctrl/Cmd + Shift + R** (the browser caches CSS).
- Don't skip STEP 1. If you start colors before fixing the structure, you'll see nothing change.
