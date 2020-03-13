#!/usr/bin/env python3

import justpy as jp
import platform
import socket
import asyncio

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())
button_classes = "w-auto mr-2 mb-2 transition-colors duration-300 ease-out bg-gray-700 hover:bg-black text-white font-bold py-2 px-4 rounded-full "

def html_comps():
    wp = jp.WebPage()
    jp.Div(text="Text in italic", a=wp, classes="italic")
    jp.Div(text="Text in bold", a=wp, classes="font-bold")
    return wp


def html_comps2():
    wp = jp.WebPage()
    for i in range(10):
        d = jp.Div(a=wp, classes="m-2")
        for j in range(10):
            jp.Span(
                text=f"Span #{j+1} in Div #{i+1}",
                a=d,
                classes="text-white bg-blue-700 hover:bg-blue-200 ml-1 p-1",
            )
    return wp


def html_comps_editable_field():
    wp = jp.WebPage()
    for _ in range(10):
        p = jp.P(
            text=f"אני אוהב לתכנת בפייתון",
            a=wp,
            contenteditable=True,
            classes="text-white bg-blue-500 hover:bg-blue-700 ml-1 p-1 w-1/2",
        )
        p.dir = "rtl"
        p.lang = "he"
    return wp


def html_comps_rotate_xform():
    wp = jp.WebPage()
    for degree in range(0, 361, 10):
        image = jp.Img(
            src="https://www.python.org/static/community_logos/python-powered-h-140x182.png",
            a=wp,
        )
        image.classes = "m-4 p-4 inline-block"
        image.style = f"transform: rotate({degree}deg)"
        image.height = 100
        image.width = 100
        image.degree = degree

        def straighten(self, msg):
            self.style = f"transform: rotate(0deg)"

        def rotate_back(self, msg):
            self.style = f"transform: rotate({self.degree}deg)"

        def no_rotate(self, msg):
            self.degree = 0
            self.set_class("bg-red-200")

        image.on("mouseenter", straighten)
        image.on("mouseleave", rotate_back)
        image.on("click", no_rotate)

    return wp


def link_demo_simple():
    wp = jp.WebPage()
    jp.Link(
        text="Python Org",
        href="https://python.org",
        a=wp,
        classes="m-2 p-2 text-xl text-white bg-blue-500 hover:bg-blue-700",
    )
    return wp


def link_demo_bookmark():
    wp = jp.WebPage()
    link = jp.A(
        text="Scroll to target",
        a=wp,
        classes="inline-block m-2 p-2 text-xl text-white bg-blue-500 hover:bg-blue-700",
    )
    # jp.Br(a=wp)
    for i in range(50):
        jp.P(text=f"{i+1} Not a target", classes="m-1 p-1 text-white bg-blue-300", a=wp)
    target = jp.Link(
        text=f"This is the target - it is linked to first link, click to jump there",
        classes="inline-block m-1 p-1 text-white bg-red-500",
        a=wp,
    )
    link.bookmark = target
    link.scroll = True
    target.bookmark = link
    target.scroll = True
    for i in range(50):
        jp.P(
            text=f"{i+50} Not a target", classes="m-1 p-1 text-white bg-blue-300", a=wp
        )
    return wp


def button_click(self, msg):
    print(msg)
    print("click")
    for button in msg.page.button_list:
        button.set_class("bg-gray-700")
        button.set_class("bg-black", "hover")
    self.set_class("bg-red-500")
    self.set_class("bg-red-700", "hover")


def list_demo():
    wp = jp.WebPage()
    button_list = []
    my_list = jp.Ul(a=wp, classes="m-2 p-2 list-disc")
    for i in range(1, 11):
        li = jp.Li(a=my_list)
        b = jp.Button(
            text=f"Button {i}", a=li, classes=button_classes, click=button_click
        )
        button_list.append(b)
    my_list = jp.Ul(a=wp, classes="m-2 p-2 list-disc list-inside")
    for i in range(1, 11):
        jp.Li(text=f"List two item {i}", a=my_list, classes="hover:bg-gray-200")
    my_list = jp.Ul(a=wp, classes="m-2 p-2 list-decimal list-inside")
    for i in range(1, 11):
        jp.Li(text=f"List three item {i}", a=my_list)
    wp.button_list = button_list
    return wp


def show_demo():
    wp = jp.WebPage()
    b = jp.Button(text = 'Click to toggle show', a=wp, classes=button_classes)
    d = jp.Div(text='Toggled by show', classes='m-2 p-2 text-2x1 border w-48', a=wp)
    b.d = d
    jp.Div(text='Will always show', classes = 'm-2', a=wp)

    def toggle_show(self, msg):
        self.d.show = not self.d.show

    b.on('click', toggle_show)

    b = jp.Button(text='Click to toggle visibility', a=wp, classes=button_classes)
    d=jp.Div(text='Toggled by visible', classes='m-2 p-2 text-2x1 border w-48', a = wp)
    d.visibility_state = 'visible'
    b.d = d
    jp.Div(text='Will always show', classes = 'm-2', a=wp)

    def toggle_visible(self, msg):
        if self.d.visibility_state == 'visible':
            self.d.set_class('invisible')
            self.d.visibility_state = 'invisible'
        else:
            self.d.set_class('visible')
            self.d.visibility_state = 'visible'

    b.on('click', toggle_visible)
    return wp


jp.justpy(show_demo, host=PUBLIC_IP)
