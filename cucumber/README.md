# Cucumber Setup (Connected Locally)

This folder contains the Cucumber/Gherkin suite connected to step definitions and Page Objects.

Current status:
- Includes `.feature` files with tags for:
  - Nicolas Cage
  - Top Box Office
  - Breaking Bad Photos
  - Born Yesterday
  - Born 40 Years Ago
- It runs independently from the current `pytest` suite.
- Includes step definitions under `cucumber/features/steps/`.
- Includes `cucumber/features/environment.py` for Playwright lifecycle in Cucumber runs.
- Includes `behave.ini` with default Playwright runtime options for Cucumber runs.
- No CI or Jenkins pipeline file was changed yet.

How to run locally:
1. Activate the virtual environment.
2. Run all features with `python -m behave`.
3. Run by tag with `python -m behave --tags @nicolas_cage`.

Suggested CI/Jenkins integration:
1. Ensure the build agent can run Playwright browsers (headed or headless as needed).
2. Install dependencies from `requirements.txt`.
3. Execute Behave by tag (for example `python -m behave --tags @nicolas_cage`).
