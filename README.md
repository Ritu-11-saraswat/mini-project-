# CartoonCare AI

CartoonCare AI is a prototype for personalized, reassuring storybooks that help children understand a medical procedure or diagnosis. The project includes an offline browser demo and an optional Python story-generation backend.

> **Important:** This is an educational prototype, not medical advice or a medical device. Generated content must be checked for accuracy and approved by a qualified clinician before it is shared with a child. Do not enter identifying patient information.

## Project files

| File | Purpose |
| --- | --- |
| `cartooncare.html` | Interactive, self-contained browser prototype with sample stories, read-aloud, parent tips, and safety checks |
| `story_engine.py` | Optional Anthropic-powered story-generation and safety-review pipeline |
| `requirements.txt` | Python dependencies for the backend |
| `.env.example` | Example environment-variable file; copy it to `.env` and add your API key |
| `.gitignore` | Excludes local secrets, virtual environments, and Python cache files |

## Run the browser prototype

Open `cartooncare.html` in a modern web browser. It runs locally and does not need a server or API key.

## Run the Python backend

You need Python and an Anthropic API key.

1. Create and activate a virtual environment:

   **Windows (PowerShell):**

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```sh
   python -m pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and replace the placeholder with your Anthropic API key:

   ```text
   ANTHROPIC_API_KEY=your_api_key_here
   ```

4. Run the backend:

   ```sh
   python story_engine.py
   ```

Keep `.env` private. It is ignored by Git; never commit an API key.

## Safety and privacy

- Use a first name or a fictional name only; do not include patient records or other personal health information.
- The automated checks in this prototype do not establish clinical accuracy or guarantee safety.
- A qualified clinician must review and approve every story before it is used with a child.
