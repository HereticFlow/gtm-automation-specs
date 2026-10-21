def score_lead(lead: dict) -> int:
    """
    Calcule un score de 0 à 100 pour prioriser les leads.
    Plus le score est élevé, plus le lead est chaud.
    """
    score = 0
    
    # 1. Taille de l'entreprise (les plus grosses entreprises ont plus de budget)
    company_size = lead.get("company_size", 0)
    if company_size >= 200:
        score += 30
    elif company_size >= 50:
        score += 15
        
    # 2. Séniorité du rôle
    role = lead.get("role", "").lower()
    if any(title in role for title in ["vp", "head", "chief", "founder", "ceo", "cto"]):
        score += 30
    elif "manager" in role or "director" in role:
        score += 15
        
    # 3. Signaux d'intention (Intent signals)
    signal = lead.get("intent_signal", "")
    if signal == "pricing_page_visit":
        score += 25
    elif signal == "competitor_comparison":
        score += 20
        
    # 4. Localisation cible (ex: Benelux + France)
    country = lead.get("country", "").upper()
    if country in ["FR", "BE", "NL", "LU"]:
        score += 15
        
    return min(score, 100) # On plafonne à 100

def route_lead(lead: dict, score: int) -> str:
    """
    Route le lead vers le bon AE en fonction de son score.
    """
    if score >= 70:
        return "Senior AE (Fast Track)"
    elif score >= 40:
        return "Junior AE (Standard Track)"
    else:
        return "Nurture Sequence (Marketing)"
