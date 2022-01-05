import requests
import json


def open_json_file():
    f = open('example.json', 'r').read()
    return f


def turn_json_to_dict_for_msg():
    jsonToDict = json.loads(open_json_file())
    channels = jsonToDict['channels']
    return channels


def choose_msg_for_chanel_1():
    channels = turn_json_to_dict_for_msg()
    channel_1_txt = channels[0]
    channel_1_txt.pop('channel')
    return channel_1_txt


def choose_msg_for_chanel_2():
    channels = turn_json_to_dict_for_msg()
    channel_2_txt = channels[1]
    channel_2_txt.pop('channel')
    return channel_2_txt


def choose_msg_for_chanel_3():
    channels = turn_json_to_dict_for_msg()
    channel_3_txt = channels[2]
    channel_3_txt.pop('channel')
    return channel_3_txt


def send_msg_to_chanel_1():
    url = "https://hooks.slack.com/services/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"
    msg = choose_msg_for_chanel_1()
    response = requests.post(url, data=json.dumps(msg))
    return response.text


def send_msg_to_chanel_2():
    url = "https://hooks.slack.com/services/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"
    msg = choose_msg_for_chanel_2()
    response = requests.post(url, data=json.dumps(msg))
    return response.text


def send_msg_to_chanel_3():
    url = "https://hooks.slack.com/services/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"
    msg = choose_msg_for_chanel_3()
    response = requests.post(url, data=json.dumps(msg))
    return response.text


send_msg_to_chanel_1()
send_msg_to_chanel_2()
send_msg_to_chanel_3()
