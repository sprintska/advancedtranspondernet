#!/usr/bin/env python3

import justpy as jp
import platform
import socket
import asyncio

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())


def hello_world():
    wp = jp.WebPage()
    my_paragraph_design = 'w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-3 rounded'
    for i in range(1,11):
        jp.P(text=f'{i}) Hello World!', a=wp, classes=my_paragraph_design)
    return wp


jp.justpy(
    hello_world, host=PUBLIC_IP, port=8000, websockets=False
)