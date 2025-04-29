## 🚀 Цели проекта

- ✅ Создать репозиторий на GitHub
- ✅ Каждый промежуточный результат оформлять через Pull Request
- ✅ Использовать [Poetry](https://python-poetry.org/) или [UV](https://github.com/astral-sh/uv) для управления виртуальным окружением
- ✅ Реализовать API на Django REST Framework

---

## 🧱 Стек технологий

- Python 3.10+
- Django 4.x
- Django REST Framework
- Poetry / UV
- SQLite / PostgreSQL
- Git + GitHub

---

## 📦 Установка и запуск проекта

```bash
# Клонирование репозитория
git clone https://github.com/your-username/todo-list-drf.git
cd todo-list-drf

# Установка зависимостей через poetry
poetry install
poetry shell

# Или с UV (если используешь UV)
uv venv
uv pip install -r requirements.txt

# Запуск миграций и сервера
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver