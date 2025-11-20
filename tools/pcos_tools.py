"""
PCOS tools for search, myth checking, and info retrieval.
Each tool returns plain text (important for Gemini).
"""

def pcos_search(query: str):
    """Search trusted PCOS sources and summarize results."""
    database = {
        "what is pcos": "PCOS is a hormonal condition where ovaries produce excess androgens. Source: Endocrine Society.",
        "pcos symptoms": "Irregular periods, acne, hair loss, weight gain, insulin resistance. Source: WHO.",
        "pcos treatment": "Lifestyle, exercise, nutrition, and medical evaluation. No cure. Source: AE-PCOS Society."
    }
    return database.get(query.lower(), "No trusted info found. Try a more specific question.")


def myth_checker(statement: str):
    """Check if a PCOS claim is myth or fact."""
    myths = {
        "seed cycling cures pcos": "Myth: Seed cycling does NOT cure PCOS. No scientific evidence.",
        "spearmint tea cures pcos": "Myth: Spearmint tea can reduce mild hair growth but does NOT cure PCOS.",
        "pcos is caused by eating sugar": "Myth: PCOS is genetic + hormonal. Sugar worsens symptoms but is not the cause."
    }
    return myths.get(statement.lower(), "No myth detected. This might be partially true or context-dependent.")


def symptom_explain(symptom: str):
    """Explain a symptom scientifically."""
    info = {
        "hair loss": "Hair loss happens because of androgen sensitivity. Consult your doctor for evaluation.",
        "irregular periods": "Irregular cycles occur due to lack of ovulation.",
        "acne": "Acne is caused by elevated androgens increasing oil glands."
    }
    return info.get(symptom.lower(), "No info available for this symptom.")
