# Python Based AI Chatbot

A simple command-line chatbot built with Python and the OpenAI API.

## Requirements

- Python 3.10 or newer
- An OpenAI API key
- The OpenAI Python package
- The `python-dotenv` package

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install the required packages:

```powershell
pip install openai python-dotenv
```

3. Create a `.env` file in the project folder:

```env
OPENAI_API_KEY=your_api_key_here
```

4. Load the `.env` file in `main.py` before creating the OpenAI client:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

You can also set your API key directly in the terminal instead of using `.env`.

To set it for the current PowerShell session:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

## Run The Chatbot

Start the chatbot with:

```powershell
python main.py
```

Then type a message and press `Enter`. The chatbot will respond in the terminal.

## Troubleshooting

If you see an error like `NameError: name 'key' is not defined`, update `main.py` so the OpenAI client only uses the environment variable:

```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

Make sure the duplicate client setup that references `key` is removed.

If you see an authentication error, confirm that `OPENAI_API_KEY` is set correctly before running `python main.py`.
