# Retro OSO

A tool for retrieving Retro Funding metrics from the OSO data lake.

## Setup

This project uses `uv` for dependency management. To get started:

1. Install `uv` if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # Create a .env file
   echo "OSO_API_KEY=your_api_key_here" > .env
   ```

## Usage

### Running Locally

To run the retro funding metrics tool locally:

```bash
# Make sure your .env file is set up with OSO_API_KEY
python src/main.py
```

### Running via GitHub Actions

1. Add your OSO_API_KEY to GitHub repository secrets:
   - Go to your repository settings
   - Navigate to Secrets and Variables > Actions
   - Add a new secret named `OSO_API_KEY` with your API key

2. Trigger the workflow:
   - Go to the Actions tab in your repository
   - Select "Run Retro Funding Metrics" workflow
   - Click "Run workflow"

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── fetch-metrics.yml
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── retro_funding_metrics.py
├── .env (create this file with your API keys)
├── .gitignore
├── README.md
└── requirements.txt
```