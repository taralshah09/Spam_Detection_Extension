## Report
[SDT_handbook (1).pdf](https://github.com/user-attachments/files/24364589/SDT_handbook.1.pdf)


## Demo
https://github.com/user-attachments/assets/ce0ea6f8-8fa4-4fc3-ac5f-51586456d646

---

## How to run the server?

Follow these steps to set up and run the Spam Detection Tool:

1. **Create a virtual environment** (if it doesn't exist):
   ```
   python -m venv env
   ```

2. **Activate the virtual environment**:
   ```
   env\Scripts\activate
   ```
   (on Windows)

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Start the server**:
   ```
   uvicorn main:app --reload
   ```

5. **Set up the Chrome extension**:
   - Copy the `chrome-extension` folder to a different location on your PC.
   - Load the unpacked extension in your browser (go to chrome://extensions/, enable "Developer mode", and click "Load unpacked" selecting the folder).
   - You're good to go!
