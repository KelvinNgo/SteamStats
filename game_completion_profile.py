from howlongtobeatpy import HowLongToBeat
from getGameName import get_game_name
from get_total_playtime import get_total_hours


# steam id 76561198147800445
# api key E9136FA773F32391F87DA37A4EA149C1


def game_completion_profile(games_owned: list) -> list:
    for game in games_owned:
        result = HowLongToBeat(0.4).search(get_game_name(game["appid"]))
        if result:
            print(result[0].game_name)


def main():
    game_completion_profile(get_total_hours())


if __name__ == '__main__':
    main()
