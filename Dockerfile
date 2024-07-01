# Используем официальный образ Python в качестве базового
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app/sitewomen

# Устанавливаем зависимости для PostgreSQL и gcc
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл requirements.txt в рабочую директорию
COPY sitewomen/requirements.txt .

# Устанавливаем зависимости Python, включая psycopg2
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в рабочую директорию
COPY sitewomen .

# Create staticfiles directory
RUN mkdir -p /app/sitewomen/staticfiles

# Set directory permissions
RUN chown -R root:root /app/sitewomen/staticfiles

# Устанавливаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=sitewomen.settings
ENV PYTHONUNBUFFERED=1

# Выполняем миграции и собираем статику при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
