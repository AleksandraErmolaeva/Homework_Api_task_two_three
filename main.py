import requests
import json

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = ('https://cloud-api.yandex.net/v1/disk/resources/upload')
        params = {'path':file_path.split('\\')[-1]}
        headers = {'Authorization':token}
        response = requests.get(url, headers=headers, params=params)
        if 200 <= response.status_code < 300:        
            url_for_upload = response.json().get('href', '')
            print(response.json())
            with open (file_path, 'rb') as file:
                response_upload = requests.put(url_for_upload, files ={'file':file})
                print(response_upload.status_code)
         


if __name__ == '__main__':
    path_to_file = input(str('Введите путь к файлу'))
    token = input('Введите OAuth + ваш токен')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


# Task three
url_stack = 'http://api.stackexchange.com/2.3/questions?fromdate=1686700800&todate=1686787200&order=desc&sort=activity&tagged=Python&site=stackoverflow'
response_stack = requests.get(url_stack)
for info in response_stack.json()['items']:
    print(info['title'])
