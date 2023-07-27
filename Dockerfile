# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    libsdl1.2-dev \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    libportmidi-dev \
    libavformat-dev \
    libswscale-dev

# Install pygame library
RUN pip install pygame

# Copy your game files from the "src" directory to the container's working directory
COPY src/shifomi.py .
COPY src/snake.py .
COPY src/pong.py .

# Set the default command to run your games
CMD ["python", "shifomi.py"]
