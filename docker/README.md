## About

Collection of `docker compose` files for various needs.

## asciinema

[asciinema]https://docs.asciinema.org/getting-started/)


* To make screencast inside docker, install it inside the image by adding following link and rebuilding:
    ```
    # For Debian/Ubuntu-based images:
    RUN apt-get update && apt-get install -y asciinema
    ```
* Play demo using Docker:
    ```
    docker run --rm -it -v ".:/app" -w /app ghcr.io/asciinema/asciinema play demo.cast
    ```

* Play demo using Docker (requires `task build`):
    ```
    docker run --rm -it -v ".:/app" -w /app --entrypoint bash asciinema-asciinema-tools asciinema play demo.cast
    ```
* Convert CAST to GIF using `agg` (requires `task build`):
    ```
    docker run --rm -it -v ".:/app" -w /app --entrypoint bash asciinema-asciinema-tools -c "agg demo.cast demo.gif"
    ```

## Go

* Navigate
    ```
    cd go
    ```
* go: base
    ```
    docker compose -f compose.yaml up
    ```
* go: recreate
    ```
    docker compose -f compose.yaml up -d --no-deps --build go-cli-bundle
    ```
* go: connect to bash
    ```
    docker compose -f compose.yaml exec go-cli-bundle bash
    ```
* go: stop the docker compose
    ```
    docker compose -f compose.yaml down
    ```
