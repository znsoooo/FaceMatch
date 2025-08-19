# Face Match

Face Match is a simple GUI application designed for comparing and ranking images. It displays two random images side-by-side, allowing you to select your preferred image by clicking or using keyboard shortcuts. The application will auto renames and reorders image files based on your selections.

## Installation

### Requirements

- Python 3.6 or higher
- wxPython (GUI framework)

### Installation Steps

1. **Install wxPython**:
   ```bash
   pip install wxPython
   ```
2. **Place all your image files into the `imgs` folder**:
3. **Run the application**:
   ```bash
   python FaceMatch.py
   ```

## Usage

### Controls

| Mouse Choose         | Keyboard Select | Function             |
| -------------------- | --------------- | -------------------- |
| Click on left image  | Left Arrow      | Select left image    |
| Click on right image | Right Arrow     | Select right image   |
| Click on blank space | Down Arrow      | Skip this comparison |

### How it Works

1. The application starts by displaying two random images from your `imgs` folder.
2. Choose your preferred image by clicking on it or using the arrow keys.
3. Based on your selection, the application renames and reorders the images.
4. Two new random images will appear for the next comparison.
5. Continue until you've compared all images or exit when finished.

