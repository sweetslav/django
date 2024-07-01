# Используем официальный образ Python в качестве базового
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости для PostgreSQL и gcc
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости Python, включая psycopg2
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в рабочую директорию
COPY . .

# Создаем директорию для статических файлов
RUN mkdir -p /app/sitewomen/staticfiles

# Устанавливаем права на директорию
RUN chown -R root:root /app/sitewomen/staticfiles

# Устанавливаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=sitewomen.settings
ENV PYTHONUNBUFFERED=1

# Выполняем миграции и собираем статику при запуске контейнера
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --no-input && gunicorn sitewomen.wsgi:application --bind 0.0.0.0:8000"]
