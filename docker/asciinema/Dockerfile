FROM rust:slim-bookworm

RUN apt-get update && apt-get install -y \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cargo install --locked --git https://github.com/asciinema/asciinema \
    && cargo install --git https://github.com/asciinema/agg

RUN apt-get update && apt-get install -y \
    fonts-dejavu-core \
    curl \
    unzip \
    fontconfig \
    && curl -fsSL -o /tmp/jbmono.zip https://download.jetbrains.com/fonts/JetBrainsMono-2.304.zip \
    && unzip /tmp/jbmono.zip -d /usr/share/fonts/jetbrains-mono \
    && fc-cache -fv \
    && rm /tmp/jbmono.zip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENTRYPOINT ["tail", "-f", "/dev/null"]
