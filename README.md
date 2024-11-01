# Doodle Game

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Building an Executable](#building-an-executable)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**Doodle Game** is a simple drawing application developed using Python and Pygame. It allows users to draw on the screen, change brush colors, and adjust brush sizes. This project is ideal for beginners looking to learn game development and Python programming.

## Features

- **Drawing:** Click and drag the mouse to draw on the canvas.
- **Color Selection:** Change brush colors using keyboard shortcuts:
  - `R` - Red
  - `G` - Green
  - `B` - Blue
  - `K` - Black
- **Brush Size Adjustment:**
  - `+` or `=` - Increase brush size
  - `-` - Decrease brush size

## Installation

### Prerequisites

- **Python 3.12.6**
- **Pygame 2.6.1**

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Jimmyu2foru18/doodle.git
   cd doodle
   ```

2. **Set Up a Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *If you don't have a `requirements.txt`, manually install Pygame:*

   ```bash
   pip install pygame
   ```

## Usage

### Running the Game


### Controls

- **Draw:** Click and drag the mouse.
- **Change Color:**
  - Press `R` for Red.
  - Press `G` for Green.
  - Press `B` for Blue.
  - Press `K` for Black.
- **Adjust Brush Size:**
  - Press `+` or `=` to increase the brush size.
  - Press `-` to decrease the brush size.

## Building an Executable

To create a standalone executable using PyInstaller:

1. **Ensure PyInstaller is Installed:**

   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable:**

   ```bash
   pyinstaller --onefile --add-data "assets;assets" doodleJ.py
   ```

   - `--onefile`: Creates a single executable file.
   - `--add-data "assets;assets"`: Includes the `assets` folder in the executable.

   **Note:** On Windows, use a semicolon (`;`) to separate source and destination paths in `--add-data`.

3. **Find the Executable:**

   After the build process completes, the executable `doodleJ.exe` will be located in the `dist` folder.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add new feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## Acknowledgements

- [Pygame](https://www.pygame.org/) for making game development in Python enjoyable.
- [GitHub](https://github.com/) for hosting the repository.
