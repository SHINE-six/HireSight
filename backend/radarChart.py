import plotly.express as px
import pandas as pd
import base64
import plotly.io as pio

def createRadarChart(technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore):
    print("123")
    df = pd.DataFrame(dict(
        r=[technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore],
        theta=['Technical Skill', 'Preparation Skill', 'Cultural Skill', 'Attitude Skill', 'Communication Skill', 'Adaptability Skill']))
    print("456")
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    print("789")
    pio.write_image(fig, "radar.jpeg")
    print("end")

def main(technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore):
    print("here")
    createRadarChart(technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore)
    print("got radar chart")
    with open("radar.jpeg", "rb") as image_file:
        print("got the radar.jpeg")
        encodedImage = base64.b64encode(image_file.read()).decode('utf-8')
        print("got the encoded image", encodedImage)
    return encodedImage







