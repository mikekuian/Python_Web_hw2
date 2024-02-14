# Використовуйте офіційний образ Python як базовий
FROM python:3.8-slim

# Встановіть робочу директорію у контейнері
WORKDIR /app

# Скопіюйте вміст вашого проекту в контейнер
COPY . /app

# Встановіть залежності проекту
RUN pip install --no-cache-dir -r requirements.txt

# Вкажіть команду для запуску вашого додатку
CMD ["python", "main.py"]
