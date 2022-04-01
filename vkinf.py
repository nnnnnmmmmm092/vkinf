import requests
import json
import random
import time




def page_inf(token, target_id):
    date_time = time.time()
    response = requests.get(
        "https://api.vk.com/method/users.get?user_ids={}&fields=id,about,first_name_nom,last_name_nom,photo_max_orig,"
        "last_seen,online,maiden_name,"
        "nickname,screen_name,status,photo_id,verified,sex,bdate,city,country,books,movies,music,occupation,personal"
        ",connections,contacts,counters,domain,education,career,home_town,quotes,"
        "relatives,relation,schools,site,timezone,trending,tv,universities,wall_default,friend_status,"
        "blacklisted,blacklisted_by_me&access_token={}&v=5.103".format(
            target_id,
            token))
    data = response.json()
    try:
        with open('{} {} [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                               data['response'][0]['last_name_nom'],
                                               time.ctime(date_time), data['response'][0]['id']), 'xt') as outfile:
            json.dump(response.json(), outfile, ensure_ascii=False)
    except FileExistsError:
        with open('{} {} [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                               data['response'][0]['last_name_nom'],
                                               time.ctime(date_time), data['response'][0]['id']), 'xt') as outfile:
            json.dump(response.json(), outfile, ensure_ascii=False)

    response_wall = requests.get("https://api.vk.com/method/wall.get?owner_id={}&extended=1&"
                                 "access_token={}&v=5.103".format(data['response'][0]['id'], token))
    try:
        with open('{} {} WALL [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                                    data['response'][0]['last_name_nom'],
                                                    time.ctime(date_time), data['response'][0]['id']), 'xt') as outfile:
            json.dump(response_wall.json(), outfile, ensure_ascii=False)
    except FileExistsError:
        with open('{} {} WALL [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                                    data['response'][0]['last_name_nom'],
                                                    time.ctime(date_time), data['response'][0]['id']), 'xt') as outfile:
            json.dump(response_wall.json(), outfile, ensure_ascii=False)

    response_photos = requests.get("https://api.vk.com/method/photos.getAll?""owner_id={}&extended=1&"
                                   "no_service_albums=0&need_hidden=1&"
                                   "access_token={}&v=5.103".format(data['response'][0]['id'], token))
    try:
        with open('{} {} PHOTOS [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                                      data['response'][0]['last_name_nom'],
                                                      time.ctime(date_time), data['response'][0]['id']),
                  'xt') as outfile:
            json.dump(response_photos.json(), outfile, ensure_ascii=False)
    except FileExistsError:
        with open('{} {} PHOTOS [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                                      data['response'][0]['last_name_nom'],
                                                      time.ctime(date_time), data['response'][0]['id']),
                  'xt') as outfile:
            json.dump(response_photos.json(), outfile, ensure_ascii=False)

    response_docs = requests.get("https://api.vk.com/method/docs.get?owner_id={}"
                                 "&access_token={}&v=5.103".format(data['response'][0]['id'], token))
    try:
        with open('{} {} DOCS [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                                    data['response'][0]['last_name_nom'],
                                                    time.ctime(date_time), data['response'][0]['id']), 'xt') as outfile:
            json.dump(response_docs.json(), outfile, ensure_ascii=False)
    except FileExistsError:
        with open('{} {} DOCS [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                                    data['response'][0]['last_name_nom'],
                                                    time.ctime(date_time), data['response'][0]['id']), 'xt') as outfile:
            json.dump(response_docs.json(), outfile, ensure_ascii=False)

    response_groups = requests.get("https://api.vk.com/method/groups.get?user_id={}&extended=1&access_token={}&"
                                   "v=5.103".format(data['response'][0]['id'], token))
    try:
        with open('{} {} GROUPS [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                                      data['response'][0]['last_name_nom'],
                                                      time.ctime(date_time), data['response'][0]['id']),
                  'xt') as outfile:
            json.dump(response_groups.json(), outfile, ensure_ascii=False)
    except FileExistsError:
        with open('{} {} GROUPS [{}] {} .json'.format(data['response'][0]['first_name_nom'],
                                                      data['response'][0]['last_name_nom'],
                                                      time.ctime(date_time), data['response'][0]['id']),
                  'xt') as outfile:
            json.dump(response_groups.json(), outfile, ensure_ascii=False)


if __name__ == "__main__":
    page_inf(input(), input())
