# Use a slim, version-pinned base image to keep the final image small and reproducible.
FROM python:3.12-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr (better container logging).
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container for all subsequent instructions.
WORKDIR /app

# Copy only dependency metadata first so Docker can cache the install layer
# when application source code changes but requirements stay the same.
COPY requirements.txt .

# Install Python dependencies declared in requirements.txt.
# --no-cache-dir avoids storing pip's download cache in the image layer.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source into the image.
COPY app.py .

# Run the container as a non-root user to reduce the impact of a container breakout.
RUN useradd --create-home --shell /bin/bash appuser \
    && chown -R appuser:appuser /app
USER appuser

# ENTRYPOINT defines the main process; CMD supplies default arguments that can be overridden.
# Example: docker run <image>           -> python app.py greet World
#          docker run <image> add 2 3     -> python app.py add 2 3
ENTRYPOINT ["python", "app.py"]
CMD ["greet", "World"]
