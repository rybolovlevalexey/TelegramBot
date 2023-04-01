import dataclasses
import requests


@dataclasses.dataclass
class AboutBot:
    token: str


file = open("service information.txt")
bot = AboutBot(file.readline().split()[1])
chat_id = "728208900"
url = f"https://api.telegram.org/bot{bot.token}/getUpdates"
res = requests.get(url)
#res1 = requests.get(url, params={"chat_id": chat_id, "text": "и тебе не хворать"})
print(res.text)