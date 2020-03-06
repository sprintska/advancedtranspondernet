#!/usr/bin/env python3

import justpy as jp
import platform
import socket
import asyncio

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())


def button_click(self, msg):
    self.num_clicked += 1
    self.message.text = f"{self.text} clicked. Number of clicks: {self.num_clicked}"
    self.set_class("bg-red-500")
    self.set_class("bg-red-700", "hover")


def event_demo():
    number_of_buttons = 25
    wp = jp.WebPage()
    button_div = jp.Div(classes="flex m-4 flex-wrap", a=wp)
    button_classes = \
        "w-auto mr-2 mb-2 transition-colors duration-300 ease-out bg-gray-700 hover:bg-black text-white font-bold py-2 px-4 rounded-full "
    message = jp.Div(
        text="No button clicked yet", classes="text-2x1 border m-4 p-2", a=wp
    )
    for i in range(1, number_of_buttons + 1):
        b = jp.Button(
            text=f"Button {i}", a=button_div, classes=button_classes, click=button_click
        )
        b.message = message
        b.num_clicked = 0
    return wp


jp.justpy(event_demo, host=PUBLIC_IP)
