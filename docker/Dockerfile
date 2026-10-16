# Camoufox as a remote Playwright server.
# Build from the repository root: docker build -f docker/Dockerfile .

# Bookworm, because `playwright install-deps` only knows the Debian releases
# Playwright supports.
FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    CAMOUFOX_PORT=3000 \
    CAMOUFOX_WS_PATH=camoufox \
    CAMOUFOX_HEADLESS=true

# Xvfb serves headless="virtual"; install-deps adds Firefox's runtime libraries.
COPY python /src/python
RUN apt-get update \
    && apt-get install -y --no-install-recommends xvfb \
    && pip install --no-cache-dir "/src/python[geoip]" \
    && playwright install-deps firefox \
    && camoufox fetch \
    && rm -rf /src /var/lib/apt/lists/*

COPY docker/serve.py /usr/local/bin/camoufox-serve

EXPOSE 3000

ENTRYPOINT ["python", "/usr/local/bin/camoufox-serve"]
