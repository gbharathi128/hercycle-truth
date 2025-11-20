from langchain_core.tools import tool

@tool
def search_trusted_pcos_sources(query: str):
    """Search only trusted medical sources for PCOS information"""
    return f"According to the 2023 International PCOS Guidelines (Endocrine Society & AE-PCOS): {query} → [real answer would come from PubMed/Tavily here]"

@tool
def debunk_common_myth(myth: str):
    """Debunk a popular PCOS myth with official sources"""
    return f"❌ MYTH: {myth}\n✅ TRUTH: The 2023 evidence-based guidelines state this is not supported. Please consult your doctor."

tools = [search_trusted_pcos_sources, debunk_common_myth]
