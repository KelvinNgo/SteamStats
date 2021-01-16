from howlongtobeatpy import HowLongToBeat
from get_total_playtime import get_total_hours


# ½
# steam id 76561198147800445
# api key E9136FA773F32391F87DA37A4EA149C1


def game_completion_profile(games_owned: list) -> list:
    list_of_game_info = []
    for game in games_owned:
        result = HowLongToBeat(0).search(game["name"])
        if result:
            game_time_played = game["playtime_forever"] / 60
            time_to_complete = result[0].gameplay_main
            print(game["name"])
            print(time_to_complete)
            print(result[0].gameplay_main_unit)
            # percentage_complete = (game_time_played / time_to_complete) * 100
            # list_of_game_info.append({"gamename": game["name"], "gamepic": result[0].game_image_url,
            #                           "percentcomplete": percentage_complete})
    # print(list_of_game_info)



def main():
    game_completion_profile(get_total_hours())


if __name__ == '__main__':
    main()
