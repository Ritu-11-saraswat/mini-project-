"""CartoonCare AI – backend pipeline (matches slide 5: Technical Methodology).

Setup:  pip install -r requirements.txt
        copy .env.example to .env and paste your key
Run:    python story_engine.py
"""
import json, re
import anthropic

try:                                    # optional: load key from .env file
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY
MODEL = "claude-sonnet-5-5"

BANNED = re.compile(r"\b(die|dead|death|kill|scary|terrible|monster)\b", re.I)

SYSTEM = """You write gentle medical storybooks for children.
Rules: warm tone (for ages 12-18 use a respectful, mature, non-childish tone and respect their privacy), honest (never say something won't happen if it will),
no frightening words, short sentences, a child hero, a friendly helper,
a parent or caregiver who stays with the child on every page (include them in each illustration_prompt).
Return ONLY JSON: {"pages":[{"text":"...","illustration_prompt":"..."}]} with exactly 5 pages."""


def clinical_input(name, age, procedure, parent="Mama", notes=""):
    """Step 1: capture care-team input."""
    return {"name": name, "age": age, "procedure": procedure, "parent": parent, "notes": notes}


def generate_story(data):
    """Steps 2-3: simplify clinical terms and build the narrative."""
    msg = client.messages.create(
        model=MODEL, max_tokens=1500, system=SYSTEM,
        messages=[{"role": "user", "content": json.dumps(data)}],
    )
    return json.loads(msg.content[0].text)


def illustration_prompts(story):
    """Step 4: attach a consistent cartoon style to every scene.
    Send these prompts to any image model (e.g. Stable Diffusion API)."""
    style = "soft pastel cartoon, friendly round shapes, children's book, no text"
    return [f"{p['illustration_prompt']}, {style}" for p in story["pages"]]


def safety_review(story, data):
    """Step 5: automated checks, then a human clinician signs off."""
    text = " ".join(p["text"] for p in story["pages"])
    return {
        "no_scary_words": not BANNED.search(text),
        "personalized": text.count(data["name"]) >= 3,
        "five_pages": len(story["pages"]) == 5,
        "parent_present": text.count(data["parent"]) >= 3,
        "clinician_approved": False,     # set True only after human review
    }


if __name__ == "__main__":
    d = clinical_input("Aarav", 7, "blood test")
    s = generate_story(d)
    print(json.dumps(s, indent=2, ensure_ascii=False))
    print(illustration_prompts(s))
    print(safety_review(s, d))
