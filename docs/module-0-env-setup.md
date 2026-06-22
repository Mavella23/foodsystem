# Module 0 — Move Secrets to a `.env` File (do this yourself, no AI)

Do this module by hand, step by step. It's small and important — doing it yourself teaches you
how Django configuration and git work. Only after this is done do you start the CSS module.

## Why we do this

Right now, `settings.py` contains **secrets in plain text**: the Django `SECRET_KEY` and the
database password. Two problems:

1. **Security:** anything committed to git stays in its history forever. A leaked `SECRET_KEY`
   lets attackers forge sessions; a leaked DB password exposes your database.
2. **Teamwork:** you and your teammate have *different* machines and *different* database
   passwords. Hardcoding one person's password breaks the other's setup on every pull.

The fix: keep secrets in a `.env` file that is **never committed**, and have `settings.py`
read them at runtime. Each person keeps their own `.env`. We share a `.env.example` so everyone
knows which variables to set.

## Steps

### 1. Install the library
```
pip install python-decouple
```
This is the tool that reads values from a `.env` file.

### 2. Create the `.env` file (your real secrets)
In the project root (next to `manage.py`), create a file named `.env`:
```
SECRET_KEY=your-real-secret-key-here
DEBUG=True
DB_NAME=mavella_db
DB_USER=root
DB_PASSWORD=your-real-database-password
DB_HOST=localhost
DB_PORT=3306
```
> This file holds your real secrets and will be git-ignored — it stays only on your machine.

### 3. Create `.env.example` (the shared template)
Create another file named `.env.example` with the same keys but **placeholder** values:
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=root
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```
> This file IS committed to git. A teammate copies it to `.env` and fills in their own values.

### 4. Ignore `.env` in git
Open `.gitignore` and add:
```
# Environment variables
.env
```
> This stops your real secrets from ever being committed.

### 5. Update `settings.py` to read from `.env`
At the top, below `from pathlib import Path`, add:
```python
from decouple import config
```
Replace the hardcoded `SECRET_KEY` and `DEBUG`:
```python
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```
Replace the database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
    }
}
```

### 6. Verify nothing broke
```
python manage.py check
python manage.py runserver
```
Then confirm `.env` is properly ignored:
```
git status
```
`.env` must **NOT** appear in the list. You should only see `settings.py`, `.gitignore`,
and `.env.example` as changes.

## Done when
- [ ] `settings.py` has no hardcoded secrets — only `config('...')` calls.
- [ ] `.env` exists locally and does not appear in `git status`.
- [ ] `.env.example` exists with placeholder values (ready to commit).
- [ ] The app still runs exactly as before.

➡️ Next: **Module 1 — CSS** (`docs/ai-prompt-css.md`).
