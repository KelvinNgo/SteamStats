from howlongtobeatpy import HowLongToBeat
from get_total_playtime import get_total_hours
from convert_completion_time import convert_completion_time
import sorting_algorithms


def game_completion_profile(games_owned: list) -> list:
    list_of_game_info = []

    for game in games_owned:
        result = HowLongToBeat(0).search(game["name"])

        if result and result[0].gameplay_main != -1:
            game_time_played = game["playtime_forever"] / 60
            time_to_complete = convert_completion_time(result[0].gameplay_main)
            percentage_complete = (game_time_played / time_to_complete) * 100

            if percentage_complete < 100:
                list_of_game_info.append({"gamename": game["name"], "gamepic": result[0].game_image_url,
                                          "percentcomplete": round(percentage_complete, 2)})

    return list_of_game_info


def main():
    print("sup")


if __name__ == '__main__':
    main()
