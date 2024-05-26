import plotly.express as px
import pandas as pd


def createRadarChart(technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore):
    df = pd.DataFrame(dict(
        r=[technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore],
        theta=['Technical Skill', 'Preparation Skill', 'Cultural Skill', 'Attitude Skill', 'Communication Skill', 'Adaptability Skill']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    return fig

def main(technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore):
    image = createRadarChart(technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore)
    image.write_image("radar.jpeg")
    with open ('radar.jpeg', 'rb') as f:
        print( list(f.read()))
    return list(f.read())

