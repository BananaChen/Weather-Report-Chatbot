from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, send_button_message, send_quick_reply_message

from parseWeb import WeatherReport


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
        self.weather = WeatherReport()
        self.cityId = ""

    def is_going_to_hello(self, event):
        if event.get("message"):  # 如果使用者有 input
            text = event['message']['text']  # 得到使用者的input message的 text
            # text.lower() change all text to low case
            if (text.lower() == 'hi' or text.lower() == 'hello'):
                return True  # 進入 on_enter_state1
            # return text.lower() == 'go to state1'
        elif event.get("postback"):
            text = event['postback']['payload']
            if (text == "restart"):
                return True
        return False

    def on_enter_hello(self, event):
        print("I'm entering Hello")

        sender_id = event['sender']['id']
        quick_replies = [
            {
                "content_type": "text",
                "title": "北部",
                "payload": "north",
                # "image_url":"http://example.com/img/red.png"
            },
            {
                "content_type": "text",
                "title": "中部",
                "payload": "central",
            },
            {
                "content_type": "text",
                "title": "南部",
                "payload": "south",
            },
            {
                "content_type": "text",
                "title": "東部",
                "payload": "east",
            },
            {
                "content_type": "text",
                "title": "離島",
                "payload": "outter",
            }
        ]
        send_quick_reply_message(sender_id, "你在哪個地區呢?", quick_replies)

    def is_going_to_region(self, event):
        if event.get("message"):  # 如果使用者有 input
            # 得到使用者的input message的 text
            print(event['message'])
            text = event['message']['quick_reply']['payload']
            # text.lower() change all text to low case
            if (text.lower() == 'north' or text.lower() == 'central' or text.lower() == 'south' or text.lower() == 'east' or text.lower() == 'outter'):
                return True  # 進入 on_enter_state1
            # return text.lower() == 'go to state1'
        return False

    def on_enter_region(self, event):
        print("I'm entering Region")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "請輸入您的縣市")
        """send_image_url(sender_id, "https://www.akc.org/wp-content/themes/akc/component-library/assets//img/welcome.jpg")
        buttons = [
                    {
                        #"type":"postback"
                        "type":"web_url",
                        "url": "https://www.messenger.com",
                        "title":"Visit Messenger"
                        #"payload": 
                    }
                ]
        send_button_message(sender_id, "hello", buttons)
        quick_replies = [
            {
                "content_type":"text",
                "title":"Search",
                "payload":"<POSTBACK_PAYLOAD>",
                #"image_url":"http://example.com/img/red.png"
            },
            {
                "content_type":"location"
            }
        ]
        send_quick_reply_message(sender_id, "qqqqq", quick_replies)"""

    def is_going_to_city(self, event):
        if event.get("message"):
            text = event['message']['text']
            self.cityId = self.weather.findCityId(text)
            if (self.cityId):
                return True  # 進入 on_enter_state1
        return False

    def on_enter_city(self, event):
        print("I'm entering City")

        sender_id = event['sender']['id']
        buttons = [
            {
                "type": "postback",
                "title": "氣溫",
                "payload": "temp"
            },
            {
                "type": "postback",
                "title": "降雨機率",
                "payload": "rainProb"
            }
        ]
        send_button_message(sender_id, "想要查詢什麼", buttons)

    def is_going_to_temperature(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            if (text == "temp"):
                return True
        return False

    def on_enter_temperature(self, event):
        sender_id = event['sender']['id']
        temp = self.weather.getTemperature(self.cityId)
        send_text_message(sender_id, "今天的氣溫是" + temp)
        tempRemind = self.weather.tempRemind(temp)
        send_text_message(sender_id, tempRemind)
        send_image_url(
            sender_id, "http://4.bp.blogspot.com/-80qHOLMpbyI/VukT5cVnLTI/AAAAAAABP5c/NUd23CmolwIlgQjWJB1DxfIOh0UdhFjWg/s1600/IMG_2529-757486.JPG")
        buttons = [
            {
                "type": "postback",
                "title": "降雨機率",
                "payload": "rainProb"
            },
            {
                "type": "postback",
                "title": "重新選擇縣市",
                "payload": "restart"
            },
            {
                "type": "postback",
                "title": "掰掰",
                "payload": "byebye"
            }
        ]
        send_button_message(sender_id, "還有什麼想知道的?", buttons)

    def is_going_to_rainProb(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            if (text == "rainProb"):
                return True
        return False

    def on_enter_rainProb(self, event):
        sender_id = event['sender']['id']
        rainProb = self.weather.getRainProb(self.cityId)
        send_text_message(sender_id, "今天的降雨機率是" + rainProb)
        rainRemind = self.weather.rainRemind(rainProb)
        if (rainRemind == "sunny"):
            send_text_message(sender_id, "今天天氣很好ㄛ")
            send_image_url(
                sender_id, "https://cdn-images-1.medium.com/max/799/1*7Ds7nPI79FWhhd4dPk_dLQ.png")
        else:
            send_text_message(sender_id, "小心下雨記得帶傘!")
            send_image_url(
                sender_id, "https://i.ytimg.com/vi/FmMAhlbF1oA/hqdefault.jpg")
        buttons = [
            {
                "type": "postback",
                "title": "氣溫",
                "payload": "temp"
            },
            {
                "type": "postback",
                "title": "重新選擇縣市",
                "payload": "restart"
            },
            {
                "type": "postback",
                "title": "掰掰",
                "payload": "byebye"
            }
        ]
        send_button_message(sender_id, "還有什麼想知道的?", buttons)

    def is_going_to_byebye(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            if (text == "byebye"):
                return True
        return False

    def on_enter_byebye(self, event):
        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "掰掰囉~")
        self.go_back()

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state3'
        return False

    def on_exit_state1(self, event):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state3")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')
