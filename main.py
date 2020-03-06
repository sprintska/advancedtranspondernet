#!/usr/bin/env python3

import justpy as jp
import platform
import socket

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())

def my_click(self, msg):
    self.text = 'I was clicked!'
    print("food")

def hello_world():
    wp = jp.WebPage()
    for i in range(1,11):
        jp.P(text=f'{i}) Hello World!', a=wp, style=f'font-size: {10*i}px')

    d = jp.Div(text='Hello world!')
    d.on('click', my_click)
    wp.add(d)
    print(1)
    return wp

jp.justpy(hello_world, host=PUBLIC_IP, port="80")