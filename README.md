# 🎬 IMDb Automation Challenge - Playwright (Python)

## 📌 Overview

This project automates different scenarios on IMDb using **Playwright + Pytest**, following the **Page Object Model (POM)** design pattern to ensure scalability, maintainability, and readability.

---

## ✅ Automated Scenarios

* Nicolas Cage navigation
* Top Box Office (Rating button interaction)
* Breaking Bad photos
* Born Yesterday (dynamic date filtering)
* Born 40 Years Ago (advanced date filtering + navigation)

---

## ⚙️ Setup

### 1. Clone repository

```bash
git clone <your-repo-url>
cd "SII Automation"
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

---

### 3. Activate environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Run Tests

### Run all tests

```bash
pytest -v
```

---

### Run tests in parallel

```bash
pytest -v -n auto
```

---

### Run individual tests

#### 🎬 Test 1 - Nicolas Cage

```bash
pytest tests/test_nicolas_cage.py -v
```

#### ⭐ Test 2 - Top Box Office (Rating Button)

```bash
pytest tests/test_top_box_office.py -v
```

#### 📸 Test 3 - Breaking Bad Photos

```bash
pytest tests/test_breaking_bad_photos.py -v
```

#### 🎂 Test 4 - Born Yesterday

```bash
pytest tests/test_born_yesterday.py -v
```

#### 🎯 Test 5 - Born 40 Years Ago

```bash
pytest tests/test_born_40_years_ago.py -v
```

---

### Run Cucumber (Behave) features

Defaults are configured in `behave.ini`:
- `browser=chromium`
- `headless=false`
- `slow_mo=300`

#### Run all Cucumber features

```bash
python -m behave
```

#### Run one tagged feature

```bash
python -m behave --tags @nicolas_cage
```

#### Override runtime options (example)

```bash
python -m behave --tags @top_box_office -D browser=firefox -D headless=false -D slow_mo=300
```

---

### Run specific browser

#### Chromium

```bash
pytest -v --browser chromium
```

#### Firefox

```bash
pytest -v --browser firefox
```

---

## 📸 Screenshots

Screenshots are automatically saved in:

```
/screenshots
```

---

## 🧠 Notes

* Dynamic dates are calculated at runtime (no hardcoded values)
* Explicit waits are used to ensure cross-browser stability (Chromium + Firefox)
* Some filters require clicking **"See results"** to trigger backend updates
* Handles dynamic content such as optional links in result descriptions
* Page Object Model (POM) used for scalability and maintainability

---

## 📂 Project Structure

```
pages/
tests/
cucumber/
screenshots/
```

---

## 🚀 Tech Stack

* Playwright (Python)
* Pytest
* Pytest-xdist (parallel execution)
* Page Object Model (POM)
