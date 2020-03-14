#!/usr/bin/env python3

import justpy as jp
import platform
import socket
import asyncio

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())


# def hello_function():
#     wp = jp.WebPage()
#     wp.add(jp.P(text='Hello there!', classes='text-5xl m-2'))
#     return wp

# jp.Route('/hello', hello_function)

@jp.SetRoute('/hello')
def hello_function():
    wp = jp.WebPage()
    wp.add(jp.P(text='Hello there!', classes='text-5x1 m-2'))
    return wp

@jp.SetRoute('/bye')
def bye_function():
    wp = jp.WebPage()
    wp.add(jp.P(text='Goodbye!', classes='text-5x1 m-2'))
    return wp


jp.justpy(host=PUBLIC_IP)
