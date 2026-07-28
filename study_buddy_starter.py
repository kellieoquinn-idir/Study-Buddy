# -----------------------------
# Part 1: Setup
# -----------------------------
from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()  # loads .env file
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

# -----------------------------
# Part 2: Role-Setting + Temperature
# -----------------------------
SYSTEM_PROMPT = """
You are 'CoderCompanion', a patient and encouraging tutor for beginners.
- Tone: Friendly, warm and approachable.
- Boundaries: Explain concepts using clear real-life examples.
- Shouldn't: Do not give direct answers; don't use complicated language.
- Should: Ask questions to guide the student to discover the answer using examples. Use clear simple language.
"""

USER_QUESTION = "What is the difference between an encoder and a decoder?"

# Run 1: Temperature 0.2 (Low - Predictable and focused)
response_low = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_QUESTION}
    ],
    temperature=0.2
)

print("\n--- Temp 0.2 Response ---")
print(response_low.choices[0].message.content)

# Run 2: Temperature 0.9 (High - Creative and varied)
response_high = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_QUESTION}
    ],
    temperature=0.9
)

print("\n--- Temp 0.9 Response ---")
print(response_high.choices[0].message.content)

## -----------------------------
# Part 3: JSON Mode
# -----------------------------

SYSTEM_PROMPT_PART3 = """
You are 'CoderCompanion', a patient and encouraging tutor for beginners.
- Tone: Friendly, warm and approachable.
- Boundaries: Explain concepts using clear real-life examples.
- Should: Use clear simple language and guide the student by asking questions. Avoid overly complex language.

Your response MUST be a valid JSON object with exactly the following fields:
{
    "topic": "The main concept being explained (e.g., 'Encoders and Decoders')",
    "explanation": "A friendly, simple explanation of the concept, using real-life examples and asking guiding questions.",
    "follow_up_question": "A single, thought-provoking question to encourage further learning or critical thinking related to the topic."
}
"""

USER_QUESTION_PART3 = "What is the difference between an encoder and a decoder?"


# -----------------------------
# Part 4: Error Handling Function
# -----------------------------

def get_json_response(system_prompt, user_question):
    """
    Handles API errors and JSON parsing errors.
    Retries once if JSON is invalid.
    """

    # 1. API CALL ERROR HANDLING
    try:
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_question}
            ],
            temperature=0.2,
            response_format={"type": "json_object"}
        )
    except Exception as e:
        print("API request failed:", e)
        return None

    # 2. JSON PARSING ERROR HANDLING
    try:
        return json.loads(response.choices[0].message.content)

    except Exception:
        print("Invalid JSON, retrying...")

        # RETRY ONCE
        try:
            retry_response = client.chat.completions.create(
                model="deepseek-v4-flash",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_question}
                ],
                temperature=0.2,
                response_format={"type": "json_object"}
            )

            return json.loads(retry_response.choices[0].message.content)

        except Exception as e:
            print("Retry failed:", e)
            return None


# -----------------------------
# Part 3 (Final Call)
# -----------------------------

json_output = get_json_response(SYSTEM_PROMPT_PART3, USER_QUESTION_PART3)

if json_output:
    print("\nTopic:", json_output["topic"])
    print("Explanation:", json_output["explanation"])
    print("Follow-up Question:", json_output["follow_up_question"])
else:
    print("Could not retrieve valid JSON.")


#-----------------------------
Final Reflection
#-----------------------------
As I was building out the code I ran the two different temperatures a few times. It was interesting to see how the low temperatures were more straightforward with easier to understand. The higher temperatures were more creative and abstract. Although I had used the case to use real-life examples, I felt that the lower temperatures were easier to understand.