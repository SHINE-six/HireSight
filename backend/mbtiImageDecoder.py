import base64

def main():
    print("here")
    with open("mbtiFolder/wordcloud.png", "rb") as image_file:
        print("got the MBTI image")
        encodedImage = base64.b64encode(image_file.read()).decode('utf-8')
        print("got the encoded image", encodedImage)
    return encodedImage
