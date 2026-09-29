# Image Viewer

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

Select **Open Folder** and choose a directory containing numerically named image files, for example `1.jpg`, `2.png`, and `3.webp`.

## Current controls

- Click the left half of the image to go to the previous image.
- Click the right half to go to the next image.
- Resize the window to fit the image to the available space.

## License

No license has been added yet. Until one is chosen, the source is publicly visible but reuse is not granted.
