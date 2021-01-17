import json
from urllib.request import urlopen


def get_profile_info(key, steam_id):
    profile = json.load(urlopen(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={steam_id}&format=json"))
    return profile["response"]["players"]
