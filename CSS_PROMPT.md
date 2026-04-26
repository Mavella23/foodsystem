# CSS Styling Prompt — FoodSystem Project

Copy and paste the prompt below to Claude or ChatGPT to get full CSS styling guidance and code for this Django food ordering system.

---

## PROMPT (copy everything below this line)

---

I have a Django food ordering system called **FoodSystem**. I need you to write professional, standard CSS for it using the following color scheme:

- **Primary:** `#FF6B35` (Orange-red)
- **Secondary:** `#2C3E50` (Dark navy)
- **Background:** `#FFF8F5` (Warm white)
- **Success:** `#27AE60` (Green)
- **White:** `#FFFFFF`
- **Light gray:** `#F0F0F0`
- **Text dark:** `#1A1A1A`
- **Text muted:** `#666666`

### Project structure

The project uses Django with `APP_DIRS=True`. Templates are in `users/templates/` and static files go in `users/static/users/css/style.css`.

All templates extend a `base.html` using `{% extends 'base.html' %}` and `{% block content %}`.

### Pages that need styling

1. **base.html** — shared layout with navbar and footer
2. **home.html** — landing page with hero section and two buttons (Register, Login)
3. **register.html** — registration form (fields: username, role dropdown, email, password, confirm password)
4. **login.html** — login form (fields: username, password) with error message support
5. **dashboard.html** — role-based dashboard using Django `{% if user.role == 'x' %}` blocks with 4 roles:
   - **customer** — cards: Browse Menu, My Orders, Track Delivery
   - **vendor** — cards: My Food Items, Incoming Orders, Earnings
   - **delivery** — cards: Assigned Orders, Mark Delivered, Delivery Map
   - **admin** — cards: Users, Vendors, All Orders, Reports

### What I need from you

Please provide:

1. **`style.css`** — full CSS file using CSS variables for all the colors above. Must include:
   - CSS reset / box-sizing
   - CSS variables (`:root`)
   - Body, typography
   - Navbar (with logo left, links right, logout button)
   - Hero section (home page)
   - Buttons (primary, secondary, outline variants)
   - Form card (centered card with shadow for login/register)
   - Form inputs (clean, focused state with primary color border)
   - Dashboard cards (icon, label, button — 3 or 4 column grid)
   - Role-specific navbar colors:
     - customer → primary `#FF6B35`
     - vendor → success `#27AE60`
     - delivery → `#3498DB` (blue)
     - admin → secondary `#2C3E50`
   - Responsive: stack cards to 1 column on mobile
   - Flash/error messages styling

2. **`base.html`** — Django base template that:
   - Loads `{% load static %}`
   - Links to `style.css`
   - Has a navbar with the FoodSystem logo and logout link (shown only when user is authenticated)
   - Has `{% block content %}{% endblock %}`
   - Has a simple footer

3. **`home.html`** — extends base, hero section with headline, subtext, and two buttons: Register and Login

4. **`login.html`** — extends base, centered form card, username + password fields, error messages in red

5. **`register.html`** — extends base, centered form card, renders `{{ form.as_p }}` with styled inputs

6. **`dashboard.html`** — extends base, role-based content using:
   ```django
   {% if request.user.role == 'customer' %}
   ...
   {% elif request.user.role == 'vendor' %}
   ...
   {% elif request.user.role == 'delivery' %}
   ...
   {% elif request.user.role == 'admin' %}
   ...
   {% endif %}
   ```
   Each role section has:
   - A welcome message with the username
   - A grid of action cards (icon, label, button)
   - Role-colored navbar class

### Django template notes
- Use `{% url 'login' %}`, `{% url 'register' %}`, `{% url 'logout' %}`, `{% url 'dashboard' %}`
- CSRF: `{% csrf_token %}` inside all forms
- Messages: `{% for message in messages %}` loop
- Static files: `{% load static %}` and `{% static 'users/css/style.css' %}`
- `request.user.username` for the logged-in username
- `request.user.role` for the role

### Style expectations
- Clean, modern, professional — like a real food delivery app
- No external CSS frameworks (no Bootstrap, no Tailwind) — pure CSS only
- Smooth hover effects on buttons and cards
- Consistent spacing using a spacing scale (8px base)
- Readable font: system font stack or Google Font (Inter or Poppins)
- Box shadows on cards and forms
- Rounded corners (8px)
