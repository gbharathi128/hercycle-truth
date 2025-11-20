# tools/pcos_tools.py
"""
PCOS helper tools — deterministic, safe, educational.
They return plain text (safe fallback when Gemini not available).
"""

def pcos_search(query: str):
    q = query.strip().lower()
    if "symptom" in q or "symptoms" in q:
        return ("Common PCOS symptoms: irregular periods, acne, hair thinning, weight gain, "
                "and insulin resistance. Lifestyle changes often help. (Source: Endocrine Society)")
    if "diet" in q or "food" in q:
        return ("PCOS-friendly diet tips: prefer low-GI carbs (millet, oats, brown rice), "
                "include protein every meal, healthy fats, plenty of fiber, and avoid sugary drinks.")
    if "treatment" in q or "manage" in q:
        return ("Management commonly includes lifestyle (diet + exercise), medical follow-up, "
                "and symptom-specific treatments. Please consult a doctor for personal medical advice.")
    return f"Sorry — I don't have a specific article for '{query}'. Try asking about symptoms, diet, or treatments."

def myth_checker(claim: str):
    c = claim.strip().lower()
    if "seed cycling" in c:
        return "Myth — seed cycling is not proven to cure PCOS. Evidence is lacking."
    if "spearmint" in c:
        return ("Partly true — small studies show spearmint might reduce some androgen markers, "
                "but it is NOT a cure for PCOS.")
    if "sugar causes pcos" in c or ("sugar" in c and "cause" in c):
        return ("Myth — sugar itself doesn't directly cause PCOS. However, high sugar intake may worsen "
                "insulin resistance and symptoms.")
    return "I couldn't classify this claim automatically. Always verify with reliable sources or a doctor."

def symptom_explain(symptom: str):
    s = symptom.strip().lower()
    if "hair loss" in s or "hairfall" in s:
        return ("Hair thinning in PCOS is often due to androgen sensitivity. A healthcare provider can advise "
                "on tests and treatments.")
    if "irregular" in s or "period" in s:
        return ("Irregular periods often occur when ovulation is infrequent. Lifestyle changes and medical evaluation "
                "can help regulate cycles.")
    if "acne" in s:
        return ("Acne can be driven by higher androgen activity, increasing oil production. Dermatologic and endocrine "
                "advice can help.")
    return f"I don't have a detailed explanation for '{symptom}'. Try a more specific symptom name."
