import requests


def send_telegram(text: str):
    da = text.split('\n')
    token = "5355947422:AAFKHVaJSOFpUtxlJ8miz1kXLeYpoJ7PgjE"
    url = "https://api.telegram.org/bot"
    channel_id = "@Geometry_help"
    url += token
    method = url + "/sendMessage"
    with open('static/f/mails.txt', mode='r+') as f:
        t_data = f.read().split('\n')
        if da[1] not in t_data and t_data.count(da[0]) <= 5:
            r = requests.post(method, data={
                 "chat_id": channel_id,
                 "text": text
                  })
            f.write(f'\n{text}')
            if r.status_code != 200:
                raise Exception("post_text error")
