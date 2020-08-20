# brief-telegram-bot

[![license](https://img.shields.io/github/license/kenblikylee/imgkernel)](https://github.com/Brief-rf/brief-telegram-bot/blob/master/LICENSE)

使用简洁的代码来创建你的电报机器人

## 1.安装

```bash
pip install brief-telegram-bot
```

## 2.快速上手

```python
from brieftgbot import Bot
#你的机器人token
token = ''
myBot = Bot(token)
#启动机器人
if __name__ == '__main__':
    try:
        myBot.launch()
    except KeyboardInterrupt:
        exit()
```

之后你与机器人对话就可以看到控制台打印的消息了

## 3.高级

**发送消息**

```python
from brieftgbot import Bot
#你的机器人token
token = ''
myBot = Bot(token)
#自定义你的函数
def handler():
    message = myBot.Msg
    chat_id = message['message']['chat']['id']
    if message['message']['texat'] == 'Hi':
        myBot.sendMessage(chat_id,'Hi from bot.')
#启动机器人，并将你的逻辑函数传递进去

if __name__ == '__main__':
    try:
        myBot.launch(handle)
    except KeyboardInterrupt:
        exit()
```

1. 通过**myBot.Msg**即可获得机器人所收到的信息，并以json格式返回，这也是您编写您的逻辑的基础需求
2. 在代码的launch()方法中可以传递的参数：

```python
myBot.launch(function='',print_info=True)
```

- function参数：置空则不会执行任何东西，填写后将会在机器人运行时执行您缩写的函数。默认为空
- print_info参数：True表示在控制台以json格式打印机器人所收到的信息，False表示不打印。默认为True

机器人的所有方法都是根据Telegram官方文档进行编写的，详细参数请参考[官方文档](https://core.telegram.org/bots/api#available-methods)



