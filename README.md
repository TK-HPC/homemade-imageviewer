# Homemade Image Viewer

A small desktop image viewer built with Python and PySide6. Choose a folder to view its images, then click the left or right side of the image to move through the list.

I spent two hours trying to decide which image viewer to use on my fresh Arch install. Some were hard to use, and some were just ugly, so I wrote my own. I love it.

## Requirements

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/)

## Run

```bash
uv sync
uv run python src/main.py
```

## Add a Hyprland app launcher entry (Arch Linux)

Run these commands from the project directory. They install the dependencies and create a user-level desktop entry for Wofi, Rofi, or another launcher that reads `.desktop` files. The entry uses the current project path, so it also works if you clone the repository somewhere else.

```bash
uv sync
PROJECT_DIR="$(pwd)"
mkdir -p "$HOME/.local/share/applications"
cat > "$HOME/.local/share/applications/homemade-imageviewer.desktop" <<EOF
[Desktop Entry]
Name=Homemade Image Viewer
Comment=Browse images in a folder
Exec="$PROJECT_DIR/.venv/bin/python" "$PROJECT_DIR/src/main.py"
Type=Application
Terminal=false
Categories=Graphics;Viewer;
EOF
```

Search for **Homemade Image Viewer** in your app launcher to start it.

Select **Open Folder** and choose a directory containing numerically named image files, for example `1.jpg`, `2.png`, and `3.webp`.

## Current controls

- Click the left half of the image to go to the previous image.
- Click the right half to go to the next image.
- Resize the window to fit the image to the available space.

## License

No license has been added yet. Until one is chosen, the source is publicly visible but reuse is not granted.
