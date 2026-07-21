import json

from groq import Groq

from app.config import settings


client = Groq(api_key=settings.GROQ_API_KEY)


class AIService:

    @staticmethod
    def analyze_incident(
        title: str,
        description: str,
        severity: str,
    ):
        prompt = f"""
You are a Senior Site Reliability Engineer.

Analyze this production incident.

Title:
{title}

Description:
{description}

Severity:
{severity}

Return ONLY valid JSON.

Example:

{{
    "root_cause": "...",
    "impact": "...",
    "recommended_fix": "...",
    "prevention": "..."
}}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()

        if content.startswith("```json"):
            content = content.replace("```json", "", 1)

        if content.startswith("```"):
            content = content.replace("```", "", 1)

        if content.endswith("```"):
            content = content[:-3]

        return content.strip()