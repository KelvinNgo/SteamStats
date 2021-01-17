import json
from urllib.request import urlopen


def get_total_hours(secret, user_id) -> list:
    """Retrieve games in user's steam library as a list of dictionaries."""
    total_hours = json.load(urlopen(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={secret}"
                                    f"&steamid={user_id}&format=json&include_appinfo=1"))
    return total_hours["response"]["games"]


def main():
    print(get_total_hours("41B25A670436FE9A3CE2D0640FAB95F4", "76561198147800445"))


if __name__ == "__main__":
    main()
