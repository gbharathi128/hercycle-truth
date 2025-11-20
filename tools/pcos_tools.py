# tools/pcos_tools.py
"""
Simple PCOS helper tools. Each tool returns a short plain-text answer.
These are intentionally deterministic and safe (no medical advice).
"""

def pcos_search(query: str):
    """Search evidence-based PCOS information (simulated)."""
    q = query.strip().lower()
    if "symptom" in q or "symptoms" in q:
        return "Common PCOS symptoms: irregular periods, acne, hair loss, weight gain, and insulin resistance. (Source: Endocrine Society)"
    if "treatment" in q or "manage" in q or "help" in q:
        return "PCOS management commonly includes lifestyle (diet + exercise), weight management, and consulting a doctor for medical options."
    if "cause" in q:
        return "PCOS likely involves hormonal and genetic factors; lifestyle can influence symptoms but is not the sole cause."
    return f"Sorry — I don't have a specific article for '{query}'. Try asking about symptoms, diet, or treatments."

def myth_checker(claim: str):
    """Check a claim for common PCOS myths."""
    c = claim.strip().lower()
    if "seed cycling" in c:
        return "Myth — seed cycling is not proven to cure PCOS. It may be popular but lacks scientific evidence."
    if "spearmint" in c:
        return "Partly true — spearmint tea has been shown in small studies to reduce certain androgen markers, but it is NOT a cure for PCOS."
    if "sugar causes pcos" in c or ("sugar" in c and "cause" in c):
        return "Myth — sugar does not directly cause PCOS; however, high sugar diets can worsen insulin resistance and symptoms."
    return "I couldn't classify this claim automatically. Always consult reliable sources or a doctor."

def symptom_explain(symptom: str):
    """Explain a symptom in a simple way."""
    s = symptom.strip().lower()
    if "hair loss" in s or "hairfall" in s:
        return "Hair loss (androgenic alopecia) can happen in PCOS due to sensitivity to androgens. A doctor can evaluate treatments."
    if "irregular" in s or "period" in s:
        return "Irregular periods often arise when ovulation is infrequent. Lifestyle and medical support can help regulate cycles."
    if "acne" in s:
        return "Acne in PCOS is often driven by higher androgen activity increasing oil production in skin."
    return f"I don't have a detailed explanation for '{symptom}'. Try a more specific symptom name."
