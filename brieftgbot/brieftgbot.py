# -*- coding: utf-8 -*-

#TODO：完善更多的类和方法
#作者：Brief
#Mail：brf2053@gmail.com
'''
通过post方法发送讯息
与官方的Available Method使用起来一样
目前仅支持机器人的一些发方法，后续将添加更多的功能
'''
import requests
class Bot:
    def __init__(self,token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
    def operate(self,method,params=None):
        return requests.post(self.api_url+method,params).json()
    def getMe(self):
        method = 'getMe'
        return self.operate(method)
    def getUpdates(self,offset=0,timeout=30):
        method = 'getUpdates'
        params = {
            'timeout':timeout,
            'offset':offset
        }
        resp = requests.get(self.api_url+method,params)
        result_json = resp.json()['result']
        return result_json
    def sendMessage(self,chat_id,text,parse_mode=None,disable_web_page_preview=None,disable_notification=None,
                    reply_to_message_id=None,reply_markup=None):
        method = 'sendMessage'
        params = {
            'chat_id':chat_id,
            'text':text,
            'parse_mode':parse_mode,
            'disable_web_preview':disable_web_page_preview,
            'disable_notification':disable_notification,
            'reply_to_message_id':reply_to_message_id,
            'reply_markup':reply_markup
        }
        return self.operate(method,params)
    def forwardMessage(self,chat_id,from_hat_id,disable_notification,message_id):
        method = 'forwardMessage'
        params = {
            'chat_id': chat_id,
            'from_hat_id': from_hat_id,
            'disable_notification': disable_notification,
            'message_id': message_id
        }
        return self.operate(method,params)
    def sendPhoto(self,chat_id,photo,caption=None,parse_mode=None,disable_notification=None,
                  reply_to_message_id=None,reply_markup=None):
        method = 'sendPhoto'
        params = {
            'chat_id': chat_id,
            'photo': photo,
            'caption': caption,
            'parse_mode': parse_mode,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method,params)
    def sendAudio(self,chat_id,audio,caption=None,parse_mode=None,duration=None,performer=None,title=None,
                  thumb=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendAudio'
        params = {
            'chat_id': chat_id,
            'audio': audio,
            'caption': caption,
            'parse_mode': parse_mode,
            'duration':duration,
            'performer':performer,
            'title':title,
            'thumb':thumb,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method,params)
    def sendDocument(self,chat_id,document,thumb=None,caption=None,parse_mode=None,disable_notification=None,
                     reply_to_message_id=None,reply_markup=None):
        method = 'sendDocument'
        params = {
            'chat_id': chat_id,
            'document': document,
            'thumb':thumb,
            'caption': caption,
            'parse_mode': parse_mode,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendVideo(self,chat_id,video,duration=None,width=None,height=None,thumb=None,caption=None,parse_mode=None,
                  supports_streaming=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendVideo'
        params = {
            'chat_id': chat_id,
            'video': video,
            'duration':duration,
            'width':width,
            'height':height,
            'thumb': thumb,
            'caption': caption,
            'parse_mode': parse_mode,
            'supports_streaming':supports_streaming,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendAnimation(self,chat_id,animation,duration=None,width=None,height=None,thumb=None,caption=None,
                      parse_mode=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendAnimation'
        params = {
            'chat_id': chat_id,
            'animation': animation,
            'duration': duration,
            'width':width,
            'height':height,
            'thumb':thumb,
            'caption': caption,
            'parse_mode': parse_mode,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendVoice(self,chat_id,voice,caption=None,animation=None,parse_mode=None,duration=None,
                  disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendVoice'
        params = {
            'chat_id': chat_id,
            'voice': voice,
            'caption': caption,
            'animation': animation,
            'parse_mode': parse_mode,
            'duration':duration,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendVideoNote(self,chat_id,video_note,duration=None,length=None,thumb=None,
                  disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendVideoNote'
        params = {
            'chat_id': chat_id,
            'video_note': video_note,
            'duration': duration,
            'length':length,
            'thumb':thumb,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)

    def sendMediaGroup(self,chat_id,media,disable_notification=None,reply_to_message_id=None):
        method = 'sendMediaGroup'
        params = {
            'chat_id': chat_id,
            'media': media,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id
        }
        return self.operate(method, params)

    def sendLocation(self,chat_id,latitude,longitude,live_period=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendLocation'
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'live_period': live_period,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def editMessageLiveLoaction(self,chat_id,message_id,inline_message_id,latitude,longitude,reply_markup=None):
        method = 'editMessageLiveLoaction'
        params = {
            'chat_id': chat_id,
            'message_id':message_id,
            'inline_message_id':inline_message_id,
            'latitude': latitude,
            'longitude': longitude,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def stopMessageLiveLocation(self,chat_id,message_id,inline_message_id,reply_markup=None):
        method = 'stopMessageLiveLocation'
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendVenue(self,chat_id,latitude,longitude,title,address,foursquare_id=None,foursquare_type=None,
                  disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendVenue'
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'title':title,
            'address':address,
            'foursquare_id':foursquare_id,
            'foursquare_type': foursquare_type,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendContact(self,chat_id,phone_number,first_name,last_name=None,vcard=None,
                  disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendContact'
        params = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'vcard': vcard,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendPoll(self,chat_id,question,options,is_anoymous=None,type=None,allows_multiple_answers=None,
                 correct_option_id=None,explanation=None,explanation_parse_mode=None,open_period=None,
                 close_date=None,is_closed=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendPoll'
        params = {
            'chat_id': chat_id,
            'question': question,
            'options': options,
            'is_anoymous': is_anoymous,
            'type': type,
            'allows_multiple_answers':allows_multiple_answers,
            'correct_option_id':correct_option_id,
            'explanation':explanation,
            'explanation_parse_mode':explanation_parse_mode,
            'open_period':open_period,
            'close_date':close_date,
            'is_closed':is_closed,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendDice(self,chat_id,emoji=None,disable_notification=None,reply_to_message_id=None,reply_markup=None):
        method = 'sendDice'
        params = {
            'chat_id': chat_id,
            'emoji': emoji,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup
        }
        return self.operate(method, params)
    def sendChatAction(self,chat_id,action):
        method = 'sendChatAction'
        params = {
            'chat_id': chat_id,
            'action': action
        }
        return self.operate(method, params)
    def getUserProfilePhotos(self,user_id,offset=None,limit=None):
        method = 'getUserProfilePhotos'
        params = {
            'chat_id': chat_id,
            'offset': offset,
            'limit':limit
        }
        return self.operate(method, params)
    def getFile(self,file_id):
        method = 'getFile'
        params = {
            'file_id': file_id
        }
        return self.operate(method, params)
    def kickChatMember(self,chat_id,user_id,until_date=None):
        method = 'kickChatMember'
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'until_date':until_date
        }
        return self.operate(method, params)
    def unbanChatMember(self,chat_id,user_id):
        method = 'unbanChatMember'
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return self.operate(method, params)
    def restrictChatMember(self,chat_id,user_id,permissions,until_data=None):
        method = 'restrictChatMember'
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'permissions':permissions,
            'until_data':until_data
        }
        return self.operate(method, params)
    def promoteChatMember(self,chat_id,user_id,can_change_info,can_post_messages=None,can_edit_messages=None,
                          can_delete_messages=None,can_invite_users=None,can_restrict_members=None,can_pin_messages=None,can_promote_members=None):
        method = 'promoteChatMember'
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'can_change_info': can_change_info,
            'can_post_messages': can_post_messages,
            'can_edit_messages':can_edit_messages,
            'can_delete_messages':can_delete_messages,
            'can_invite_users':can_invite_users,
            'can_restrict_members':can_restrict_members,
            'can_pin_messages':can_pin_messages,
            'can_promote_members':can_promote_members
        }
        return self.operate(method, params)
    def setChatAdministratorCustomTitle(self,chat_id,user_id):
        method = 'setChatAdministratorCustomTitle'
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'custom_title':custom_title
        }
        return self.operate(method, params)
    def setChatPermissions(self,chat_id,permissions):
        method = 'setChatPermissions'
        params = {
            'chat_id': chat_id,
            'permissions': permissions
        }
        return self.operate(method, params)
    def exportChatInviteLink(self,chat_id):
        method = 'exportChatInviteLink'
        params = {
            'chat_id': chat_id
        }
        return self.operate(method, params)
    def setChatPhoto(self,chat_id,photo):
        method = 'setChatPhoto'
        params = {
            'chat_id': chat_id,
            'photo': photo
        }
        return self.operate(method, params)
    def deleteChatPhoto(self,chat_id):
        method = 'setChatPhoto'
        params = {
            'chat_id': chat_id
        }
        return self.operate(method, params)
    def setChatTitle(self,chat_id,title):
        method = 'setChatTitle'
        params = {
            'chat_id': chat_id,
            'title': title
        }
        return self.operate(method, params)
    def setChatDescription(self,chat_id,description):
        method = 'setChatDescription'
        params = {
            'chat_id': chat_id,
            'description': description
        }
        return self.operate(method, params)
    def pinChatMessage(self,chat_id,message_id,disable_notification=None):
        method = 'setChatAdministratorCustomTitle'
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'disable_notification': disable_notification
        }
        return self.operate(method, params)
    def unpinChatMessage(self,chat_id):
        method = 'unpinChatMessage'
        params = {
            'chat_id': chat_id
        }
        return self.operate(method, params)
    def leaveChat(self,chat_id):
        method = 'leaveChat'
        params = {
            'chat_id': chat_id
        }
        return self.operate(method, params)
    def getChat(self,chat_id):
        method = 'getChat'
        params = {
            'chat_id': chat_id
        }
        return self.operate(method, params)
    def getChatAdministrators(self,chat_id):
        method = 'getChatAdministrators'
        params = {
            'chat_id': chat_id
        }
        return self.operate(method, params)
    def getChatMembersCount(self,chat_id):
        method = 'getChatMembersCount'
        params = {
            'chat_id': chat_id
        }
        return self.operate(method, params)
    def getChatMember(self,chat_id,user_id):
        method = 'getChatMember'
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return self.operate(method, params)
    def setChatStickerSet(self,chat_id,sticker_set_name):
        method = 'setChatStickerSet'
        params = {
            'chat_id': chat_id,
            'sticker_set_name': sticker_set_name
        }
        return self.operate(method, params)
    def deleteChatStickerSet(self,chat_id):
        method = 'deleteChatStickerSet'
        params = {
            'chat_id': chat_id
        }
        return self.operate(method, params)
    def answerCallbackQuery(self,call_back_query_id,text=None,show_alert=None,url=None,cache_time=None):
        method = 'answerCallbackQuery'
        params = {
            'call_back_query_id': call_back_query_id,
            'text': text,
            'show_alert': show_alert,
            'url':url,
            'cache_time':cache_time
        }
        return self.operate(method, params)
    def setMyCommands(self,commands):
        method = 'deleteChatStickerSet'
        params = {
            'commands': commands
        }
        return self.operate(method, params)
    def getMyCommands(self):
        method = 'getMyCommands'
        return self.operate(method)
    def launch(self,function='',print_info=True):
        new_offset = 0
        print('Launching...')
        while True:
            all_updates = self.getUpdates(offset=new_offset)
            if len(all_updates) > 0:
                for current_update in all_updates:
                    self.Msg = current_update
                    if print_info:
                        print(current_update)
                    if function == '':
                        pass
                    else:
                        function()
                    new_offset = current_update['update_id'] + 1