import requests

url = 'http://0.0.0.1:5000/extract-text'
files = {'file': open('DhruvilKakadiya_Resume.pdf', 'rb')}
response = requests.post(url, files=files)
print(response.json())
