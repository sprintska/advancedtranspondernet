#!/usr/bin/env python3

import justpy as jp
import platform
import socket
import asyncio

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())


def reset_all(self, msg):
    msg.page.data['text'] = ''


async def input_demo(request):
    wp = jp.WebPage(data={'text':'Initial text'})
    button_classes = 'w-32 m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'
    b = jp.Button(text='Reset', click=reset_all, a=wp, classes=button_classes)
    jp.Hr(a=wp)
    input_classes = "m-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded xtw-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
    for _ in range(5):
        jp.Input(a=wp, classes=input_classes, placeholder='Please type here', model=[wp, 'text'])
    for _ in range(3):
        jp.Div(model=[wp, 'text'], classes='m-2 p-2 h-32 text-xl border-2 overflow-auto', a=wp)
    return wp


jp.justpy(input_demo, host=PUBLIC_IP)
