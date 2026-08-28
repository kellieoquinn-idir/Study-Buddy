# Study-Buddy
[TLAB Phase 2] Creating a Study Buddy using LLM

**# Study Buddy**

A Python script demonstrating how to interact with LLM APIs using the `openai` client configured for DeepSeek models. This project explores role-setting, temperature tuning, structured JSON outputs, error handling, and basic retry logic.

---

**## Features**

* **Role-Setting & Persona:** Uses system prompts to configure `CoderCompanion`, a patient, encouraging tutor tailored for beginners.
* **Temperature Comparison:** Runs side-by-side completions at `0.2` (predictable/focused) and `0.9` (creative/varied) to evaluate response quality.
* **Structured Output (JSON Mode):** Enforces a strict JSON schema containing explicit keys (`topic`, `explanation`, `follow_up_question`).
* **Robust Error Handling:** Features a wrapper function with exception handling for API failures and fallback retry logic for JSON parsing errors.

---

**## File Structure**

* `study_buddy_starter.py` – Main Python script containing setup, API calls, JSON parsing, error handling, and reflection notes.
* `requirements.txt` – Dependency specifications.
* `.env` – Local environment file for sensitive API keys (excluded from version control).
* `README.md` – Project documentation.
* `REFLECTION.MD` – Extended reflections on model behavior and prompt engineering.

---

**## Prerequisites & Setup**

1. **Clone the repository:**
```bash
git clone https://github.com/kellieoquinn-idir/Study-Buddy.git
cd Study-Buddy

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


*Required packages include `openai` and `python-dotenv`.*
3. **Configure API Key:**
Create a `.env` file in the root directory and add your DeepSeek API key:
```env
DEEPSEEK_API_KEY=your_actual_api_key_here

```



---

**## Usage**

Run the starter script:

```bash
python study_buddy_starter.py

```

---

**## Implementation Details**

**### 1. Temperature Experiments**
The script compares outputs using `deepseek-v4-flash` under two configurations:

* **Low Temperature (`0.2`):** Delivers direct, consistent, and easy-to-understand explanations using real-life examples.
* **High Temperature (`0.9`):** Produces more abstract and creative responses.

**### 2. JSON Response Function (`get_json_response`)**

* Requests structured JSON using `response_format={"type": "json_object"}`.
* Automatically captures API connection errors via `try-except` blocks.
* Attempts a single retry if the returned payload fails standard `json.loads()` validation.
