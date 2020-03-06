#!/usr/bin/env python3

import justpy as jp
import platform
import socket
import asyncio

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())


def my_click(self, msg):
    self.text = 'I was clicked'
    print(msg)

def event_demo():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-48 text-xl m-2 p-c bg-blue-500 text-white')
    d.on('click', my_click)
    d.additional_properties = ['screenX','pageY','altKey','which','movementX','button','buttons']
    return wp

jp.justpy(event_demo, host=PUBLIC_IP)