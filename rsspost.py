import webbrowser
import urllib.parse
import requests
import os
from bs4 import BeautifulSoup

BASE_URL = "http://ria.ru/export/rss2/politics/index.xml"  # TODO: replace this with your rss feed URL
GROUP_ID = '97205249'  # TODO: replace this with your group id


def check_exist(items, token):
    counter = 0
    request_data = {'owner_id': '-' + GROUP_ID,
                    'count': 1,
                    'filter': 'owner',
                    'extended': 0,
                    'access_token': token}
    r = requests.get('https://api.vk.com/method/wall.get', data=request_data).json()
    if r['response'] == [0]:
        return -1
    else:
        text = r['response'][1]['text'][:r['response'][1]['text'].find('<br>')]
        if text in items[len(items) - 1]['text']:
            return 0
        else:
            while text not in items[counter]['text'] and counter < len(items) - 1:
                print(items[counter]['text'][:items[counter]['text'].find('\n')])
                counter += 1
            return counter


def post_news(news, image, token):
    news_post = urllib.parse.quote_plus(news)
    request_data = {'owner_id': '-' + GROUP_ID,
                    'from_group': 1,
                    'message': news_post,
                    'attachments': image,
                    'access_token': token}
    return requests.post('https://api.vk.com/method/wall.post', data=request_data).json()


def photo_upload(photo_url, token):
    request_data = {'group_id': GROUP_ID, 'access_token': token}
    r = requests.get('https://api.vk.com/method/photos.getWallUploadServer', data=request_data).json()
    upload_url = r['response']['upload_url']
    p = requests.get(photo_url)
    with open('images/img.jpg', "wb") as out:
        out.write(p.content)
    files = {'photo': ('img.jpg', open('images/img.jpg', "rb"))}
    data = requests.post(upload_url, files=files).json()
    os.remove('images/img.jpg')
    photo_obj = requests.post('https://api.vk.com/method/photos.saveWallPhoto', data=request_data, json=data).json()
    return photo_obj['response'][0]['id']


def get_token():
    link = 'https://oauth.vk.com/authorize?client_id=4963630&scope=wall,groups,offline,photos&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token'
    webbrowser.open(link, new=2, autoraise=True)
    url = input("Скопируйте и вставтье сюда URL страницы, открывшейся в вашем браузере: ")
    token = ''
    for i in range(len(url)):
        if (url.find('ken=') + 3) < i < url.find('&'):
            token = token + url[i]
    return token


def get_html(url):
    return requests.get(url).text


def parse_html(xml):
    soup = BeautifulSoup(xml)
    items = soup.find_all('item')
    list = []
    for item in items:
        title = item.find('title').text
        news = title + '\n\n' + item.find('description').text + '\nЧитать полностью: ' + item.find('link').text
        attachment = item.find('enclosure', {'url': True})
        if attachment is None:
            attachment = ''
            list.append({'text': news, 'image': attachment})
        else:
            list.append({'text': news, 'image': attachment['url']})
    list.reverse()
    return list


def check_token():
    with open('token.dat', 'r') as f:
        s = f.read()
        if s != '':
            return s
        else:
            return False


def write_token(token):
    with open('token.dat', 'w') as f:
        f.write(token)


def main():
    posted = None
    if not check_token():
        write_token(get_token())
    token = check_token()

    items = parse_html(get_html(BASE_URL))
    counter = check_exist(items, token)

    if counter == -1:
        for i in range(len(items)):
            if not items[i]['image'] == '':
                p = photo_upload(items[i]['image'], token)
                post_news(items[i]['text'], p, token)
            else:
                post_news(items[i]['text'], items[i]['image'], token)
            print('Группа заполнена')
        posted = True
    elif counter == 0:
        print('Новых новостей в ленте нет!')
        posted = False
    elif not counter == 0 and not counter == -1:
        for i in range(counter + 1, len(items)):
            if not items[i]['image'] == '':
                p = photo_upload(items[i]['image'], token)
                answer = post_news(items[i]['text'], p, token)
            else:
                answer = post_news(items[i]['text'], items[i]['image'], token)
            if 'error' in answer:
                print('Ошибка! Возможно вы превысили лимит в 50 постов в день')
                posted = 'Error'
            else:
                posted = True
                print('Группа обновлена')
    return posted

if __name__ == '__main__':
    main()
