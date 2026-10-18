FROM python:3.12-slim

WORKDIR /app
COPY app.py .
COPY tests/ tests/

# Run as a non-root user.
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "app.py", "https://example.com"]
