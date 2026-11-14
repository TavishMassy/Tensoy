import re


def generate_mock_chat(prompt: str) -> tuple[str, str]:
    """Generate deterministic mock response and a single face emoji based on the prompt."""
    normalized_prompt = prompt.strip().lower()

    if re.search(r"\b(hello|hi|hey|greetings)\b", normalized_prompt):
        return ("Hello! It's great to hear from you. How can I assist you today?", "😊")
    elif re.search(r"\b(why|how|what|who|when|where)\b|\?", normalized_prompt):
        return ("That's a thoughtful question! Here is a helpful mock explanation.", "🤔")
    elif re.search(r"\b(great|awesome|celebrate|win|congrats|milestone)\b", normalized_prompt):
        return ("That sounds wonderful! Celebrating your success.", "🥳")
    elif re.search(r"\b(idea|think|create|design|solve)\b", normalized_prompt):
        return ("Here is an inventive thought to spark new directions.", "🧐")
    else:
        return (f"Acknowledged your input: '{prompt[:60]}...'. I'm here to assist.", "😐")
