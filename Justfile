run *args:
    #!/usr/bin/env sh

    # Kill all child processes on exit
    trap 'kill 0' EXIT

    # Start the Django server
    py manage.py runserver &

    # Open the browser (after 4s)
    (sleep 2 && py -m webbrowser http://127.0.0.1:8000/) &

    # Start the Tailwind CSS CLI
    just tailwindcss &

    # Wait for all processes to finish
    wait

createsuperuser:
    py manage.py createsuperuser

# Run TailwindCSS CLI in watch mode
tailwindcss: download-tailwindcss
    ./tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --watch=always --minify

# Download TailwindCSS's Standalone CLI binary for Windows
download-tailwindcss:
    #!/usr/bin/env bash

    # Ensure the script runs only on Windows
    if [ "$OS" != "Windows_NT" ]; then
        echo "This script only works on Windows."
        exit 1
    fi

    # Check if the binary already exists
    [ -f "./tailwindcss.exe" ] && echo "TailwindCSS Standalone CLI is already downloaded." && exit 0

    # Set TailwindCSS version and base URL
    TAILWIND_VERSION="4.1.7"
    BASE_URL="https://github.com/tailwindlabs/tailwindcss/releases/download/v${TAILWIND_VERSION}"

    # Determine architecture for Windows
    case "$PROCESSOR_ARCHITECTURE" in
        AMD64) ARCH="windows-x64" ;;
        ARM64) ARCH="windows-arm64" ;;
        *) echo "Unsupported architecture: $PROCESSOR_ARCHITECTURE"; exit 1 ;;
    esac

    # Define binary and output file names
    BINARY="tailwindcss-${ARCH}.exe"
    OUTPUT_FILE="./tailwindcss.exe"

    # Download the binary
    echo "Downloading TailwindCSS Standalone CLI for $ARCH..."
    curl -L -o "$OUTPUT_FILE" "$BASE_URL/$BINARY"
    echo "TailwindCSS Standalone CLI has been downloaded to $OUTPUT_FILE"