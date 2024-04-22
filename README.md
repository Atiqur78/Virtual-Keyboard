# Virtual Keyboard

This project utilizes Mediapipe and OpenCV to create a virtual keyboard controlled by hand gestures. The keyboard layout mimics the QWERTY layout and includes keys for letters, numbers, and special characters.

## Requirements

- Python 3.x
- OpenCV library (cv2)
- Mediapipe library
- Numpy library (imported with Mediapipe)

You can install these libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use the virtual keyboard, run the `virtual_keyboard.py` script. It will open a window displaying the virtual keyboard and a text area for displaying typed text.

- To type a character, hover your hand over the corresponding key on the keyboard and make a fist. The key will highlight, and the character will be added to the text area.
- To delete a character, hover your hand over the "Delete" key and make a fist.
- To add a space, hover your hand over the "Space" key and make a fist.
- To exit the application, press the 'q' key.

## Keyboard Layout

The keyboard layout is based on the QWERTY layout and includes keys for letters, numbers, and special characters. It is divided into three rows, with each row containing a set of keys arranged in a grid.

---
