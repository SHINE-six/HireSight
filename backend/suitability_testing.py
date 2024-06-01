def main(reportData):
    behavioralAnalysis = reportData["behavioralAnalysis"]
   
    disfluencies = reportData["disfluencies"]
    repetitionCount = disfluencies.get("repetitionCount", 0)
    hesitationCount = disfluencies.get("hesitationCount", 0)

    plagiarism = reportData["plagiarism"]
    score = plagiarism.get("Score", 0)

    aiDetector = reportData["aiDetector"]
    probability_ai = aiDetector.get("probability_ai", 0)

    TechnicalSkill = reportData["TechnicalSkill"]
    TechnicalSkillScore = TechnicalSkill.get("TechnicalSkillScore", 0)
    SoftSkill = reportData["SoftSkill"]
    PreparationSkill = SoftSkill["PreparationSkill"]
    PreparationScore = PreparationSkill.get("PreparationScore", 0)
    CulturalFitSkill = SoftSkill["CulturalFitSkill"]
    CulturalFitScore = CulturalFitSkill.get("CulturalFitScore", 0)
    AttitudeSkill = SoftSkill["AttitudeSkill"]
    AttitudeScore = AttitudeSkill.get("AttitudeScore", 0)
    CommunicationSkill = SoftSkill["CommunicationSkill"]
    CommunicationSkillScore = CommunicationSkill.get("CommunicationSkillScore", 0)
    AdaptabilitySkill = SoftSkill["AdaptabilitySkill"]
    AdaptabilityScore = AdaptabilitySkill.get("AdaptabilityScore", 0)

    weighted_scores = {
        "behavioralAnalysis": behavioralAnalysis * weights['behavioralAnalysis'],
        "repetitionCount": repetitionCount * weights["repetitionCount"],
        "hesitationCount": hesitationCount * weights['hesitationCount'],
        "plagiarismScore": score * weights['plagiarismScore'],
        "probability_ai": probability_ai * weights['probability_ai'],
        "TechnicalSkillScore": TechnicalSkillScore * weights['TechnicalSkillScore'],
        "PreparationScore": PreparationScore * weights['PreparationScore'],
        "CulturalFitScore": CulturalFitScore * weights['CulturalFitScore'],
        "AttitudeScore": AttitudeScore * weights['AttitudeScore'],
        "CommunicationSkillScore": CommunicationSkillScore * weights['CommunicationSkillScore'],
        "AdaptabilityScore": AdaptabilityScore * weights['AdaptabilityScore'],
    }

    overall_score = sum(weighted_scores.values())

    formatted_result = "{:.2f}".format(overall_score)
    result = {
        "Score": f"{formatted_result}%",
    }
    return result

weights = {
    "behavioralAnalysis": 0.15,
    "repetitionCount": 0.05,
    "hesitationCount": 0.05,
    "plagiarismScore": 0.1,
    "probability_ai": 0.1,
    "TechnicalSkillScore": 0.15,
    "PreparationScore": 0.1,
    "CulturalFitScore": 0.15,
    "AttitudeScore": 0.15,
    "CommunicationSkillScore": 0.15,
    "AdaptabilityScore": 0.1,
}








