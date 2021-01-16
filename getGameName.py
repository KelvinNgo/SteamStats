import json
from urllib.request import urlopen


def get_game_name():
    key = input("Please enter your steam api key: ")
    game_id = input("Please enter your game id: ")
    app_list = load_all_games()
    game = list(filter(lambda game_container: game_container['appid'] == int(game_id), app_list))
    try:
        game_name = game[0]['name']
        return game_name
    except:
        print("error mf")


def load_all_games():
    app_container = json.load(urlopen("https://api.steampowered.com/ISteamApps/GetAppList/v2/"))
    app_list = app_container["applist"]["apps"]
    return app_list


print(get_game_name())
