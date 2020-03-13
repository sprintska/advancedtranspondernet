#!/usr/bin/env python3

import justpy as jp
import platform
import socket
import asyncio

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())


def button_click(self, msg):
    self.num_clicked += 1
    # self.message.text = f"{self.text} clicked. Number of clicks: {self.num_clicked}"
    p = jp.P(text=f"{self.text} clicked. Number of clicks: {self.num_clicked}")
    self.message.add_component(p, 0)
    for button in msg.page.button_list:
        button.set_class("bg-gray-700")
        button.set_class("bg-black", "hover")
    self.set_class("bg-red-500")
    self.set_class("bg-red-700", "hover")


def event_demo():
    number_of_buttons = 25
    wp = jp.WebPage()
    button_div = jp.Div(classes="flex m-4 flex-wrap", a=wp)
    button_classes = "w-auto mr-2 mb-2 transition-colors duration-300 ease-out bg-gray-700 hover:bg-black text-white font-bold py-2 px-4 rounded-full "
    button_list = []
    for i in range(1, number_of_buttons + 1):
        b = jp.Button(
            text=f"Button {i}", a=button_div, classes=button_classes, click=button_click
        )
        b.num_clicked = 0
        button_list.append(b)
    wp.button_list = button_list
    return wp


jp.justpy(event_demo, host=PUBLIC_IP)
