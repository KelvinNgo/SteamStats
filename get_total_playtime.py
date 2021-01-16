import json
from urllib.request import urlopen


def get_total_hours():
    total_hours = json.load(urlopen("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=33A26580F04F1550F02B0B4A4B0E8DD1&steamid=76561198159557689&format=json"))
    return total_hours["response"]["games"]


def main():
    print(get_total_hours())


if __name__ == "__main__":
    main()
