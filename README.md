## Report
[SDT_handbook (1).pdf](https://github.com/user-attachments/files/24364589/SDT_handbook.1.pdf)


## Demo
https://github.com/user-attachments/assets/ce0ea6f8-8fa4-4fc3-ac5f-51586456d646

---

## How to run the server?

Follow these steps to set up and run the Spam Detection Tool:

1. **Create and activate a virtual environment** (if it doesn't exist):
   - Create: `python -m venv env`
   - Activate: `env\Scripts\activate` (on Windows)

2. **Install the required dependencies** (if not done already):
   ```
   pip install -r requirements.txt
   ```

3. **Start the server**:
   ```
   uvicorn main:app --reload
   ```

4. **Set up the Chrome extension**:
   - Copy the `chrome-extension` folder to a different location on your PC.
   - Load the unpacked extension in your browser (go to chrome://extensions/, enable "Developer mode", and click "Load unpacked" selecting the folder).
   - You're good to go!
