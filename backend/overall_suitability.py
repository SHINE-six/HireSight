def main(reportData, TechnicalSkillScore, PreparationScore, CulturalFitScore, AttitudeScore, CommunicationSkillScore, AdaptabilityScore):
    behavioralAnalysis = reportData["behavioralAnalysis"]
    speechDisfluencies = reportData["speechDisfluencies"]
    totalCountDisfluencies = speechDisfluencies.get("totalCount", 0)
    # TechnicalSkill = reportData["TechnicalSkill"]
    # TechnicalSkillScore = TechnicalSkill.get("TechnicalSkillScore", 0)
    # SoftSkill = reportData["SoftSkill"]
    # PreparationSkill = SoftSkill["PreparationSkill"]
    # PreparationScore = PreparationSkill.get("PreparationScore", 0)
    # CulturalFitSkill = SoftSkill["CulturalFitSkill"]
    # CulturalFitScore = CulturalFitSkill.get("CulturalFitScore", 0)
    # AttitudeSkill = SoftSkill["AttitudeSkill"]
    # AttitudeScore = AttitudeSkill.get("AttitudeScore", 0)
    # CommunicationSkill = SoftSkill["CommunicationSkill"]
    # CommunicationSkillScore = CommunicationSkill.get("CommunicationSkillScore", 0)
    # AdaptabilitySkill = SoftSkill["AdaptabilitySkill"]
    # AdaptabilityScore = AdaptabilitySkill.get("AdaptabilityScore", 0)
    SoftSkillScore = PreparationScore + CulturalFitScore + AttitudeScore + CommunicationSkillScore + AdaptabilityScore

    if behavioralAnalysis <= 40:
        weighted_scores = {
            "speechspeechDisfluencies": totalCountDisfluencies * weights["speechspeechDisfluencies"],
            "TechnicalSkillScore": TechnicalSkillScore * weights['TechnicalSkillScore'],
            "SoftSkillScore": SoftSkillScore * weights['SoftSkillScore'],
            "ConfidentLevel": behavioralAnalysis * weights['confidentLevel']
        }

        overall_score = sum(weighted_scores.values())
    else: 
        plagiarism = reportData["plagiarism"]
        score = plagiarism.get("Score", 0)

        aiDetector = reportData["aiDetector"]
        probability_ai = aiDetector.get("probability_ai", 0)

        weighted_scores = {
            "speechspeechDisfluencies": totalCountDisfluencies * weights["speechspeechDisfluencies"],
            "plagiarismScore": score * weights['plagiarism'],
            "probability_ai": probability_ai * weights['probability_ai'],
            "TechnicalSkillScore": TechnicalSkillScore * weights['TechnicalSkillScore'],
            "SoftSkillScore": SoftSkillScore * weights['SoftSkillScore'],
        }

        overall_score = sum(weighted_scores.values())

        formatted_result = "{:.2f}".format(overall_score)
        result = {
            "Score": f"{formatted_result}",
    }
    return result

weights = {
    "speechspeechDisfluencies": 0.10,
    "plagiarism": 0.15,
    "probability_ai": 0.15,
    "TechnicalSkillScore": 0.25,
    "SoftSkillScore": 0.35,
    "confidentLevel": 0.30,
}








