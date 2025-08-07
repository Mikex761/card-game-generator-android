# Docker build environment for Card Game Generator Android APK
FROM ubuntu:20.04

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    git \
    unzip \
    openjdk-8-jdk \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set Java environment
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Install Python dependencies
RUN pip3 install --upgrade pip && \
    pip3 install kivy[base]==2.1.0 && \
    pip3 install reportlab>=3.6.0 && \
    pip3 install Pillow>=9.0.0 && \
    pip3 install pandas>=1.3.0 && \
    pip3 install openpyxl>=3.0.0 && \
    pip3 install buildozer==1.4.0 && \
    pip3 install cython==0.29.33

# Create working directory
WORKDIR /app

# Copy app files
COPY . .

# Build the APK
CMD ["buildozer", "android", "debug"]
