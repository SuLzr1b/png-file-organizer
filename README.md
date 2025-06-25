# PNG File Organizer

## Description
This Python script organizes `.png` files from the Downloads folder into a subfolder called "Imagens PNG". Inside "Imagens PNG", it creates three subfolders: "MINECRAFT", "ROBLOX", and "BUILDS". Files are sorted based on their names:
- Files starting with "minecraft" go to "MINECRAFT".
- Files starting with "roblox" go to "ROBLOX".
- Files containing words from a `wordlist.txt` file (located in the same directory as the script) go to "BUILDS".
The project was created to practice Python file handling using the `os` library.

## Requirements
- Python 3.x
- A `wordlist.txt` file in the same directory as the script with construction-related words (one per line, e.g., "casa", "tijolo").

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SuLzr1b/png-file-organizer.git
   ```
2. Place `wordlist.txt` in the same directory as `detecft.py`.

## Usage
1. Add `.png` files to your Downloads folder.
2. Ensure `wordlist.txt` exists with relevant keywords.
3. Run the script:
   ```bash
   python detecft.py
   ```
4. Check the organized files in `Downloads/Imagens PNG/MINECRAFT`, `ROBLOX`, and `BUILDS`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
By **SuLr1b**
