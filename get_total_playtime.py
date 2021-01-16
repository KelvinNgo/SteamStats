import json
from urllib.request import urlopen


def get_total_hours(secret, your_id) -> list:
    total_hours = json.load(urlopen(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={secret}"
                                    f"&steamid={your_id}&format=json&include_appinfo=1"))
    return total_hours["response"]["games"]


def main():
    print(get_total_hours())


if __name__ == "__main__":
    main()
