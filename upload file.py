import requests

###------------ Upload the text file ------------####

# url = 'http://localhost:5000/upload'
# files = {'file': open('example.txt', 'rb')}
# response = requests.post(url, files=files)
# print(response.json())

###------------ Download the text file ------------####

# url = 'http://localhost:5000/download'
# response = requests.get(url)
# with open('downloaded_file.txt', 'wb') as f:
#     f.write(response.content)


###------------ Upload the rar file ------------####

# url = 'http://localhost:5000/upload'
# files = {'file': open('example.rar', 'rb')}
# response = requests.post(url, files=files)
# print(response.json())

###------------ Download the rar file ------------####

# url = 'http://localhost:5000/download'
# response = requests.get(url)
# with open('downloaded_file.rar', 'wb') as f:
#     f.write(response.content)