#!/usr/bin/env python3

import justpy as jp
import platform
import socket
import asyncio

PUBLIC_IP = socket.gethostbyname(socket.getfqdn())

button_classes = "w-auto mr-2 mb-2 transition-colors duration-300 ease-out bg-gray-700 hover:bg-black text-white font-bold py-2 px-4 rounded-full "
input_classes = "m-2 bg-blue-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
p_classes = "m-2 p-2 h-32 text-xl border-2"


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
    b = jp.Button(text="Click to toggle show", a=wp, classes=button_classes)
    d = jp.Div(text="Toggled by show", classes="m-2 p-2 text-2x1 border w-48", a=wp)
    b.d = d
    jp.Div(text="Will always show", classes="m-2", a=wp)

    def toggle_show(self, msg):
        self.d.show = not self.d.show

    b.on("click", toggle_show)

    b = jp.Button(text="Click to toggle visibility", a=wp, classes=button_classes)
    d = jp.Div(text="Toggled by visible", classes="m-2 p-2 text-2x1 border w-48", a=wp)
    d.visibility_state = "visible"
    b.d = d
    jp.Div(text="Will always show", classes="m-2", a=wp)

    def toggle_visible(self, msg):
        if self.d.visibility_state == "visible":
            self.d.set_class("invisible")
            self.d.visibility_state = "invisible"
        else:
            self.d.set_class("visible")
            self.d.visibility_state = "visible"

    b.on("click", toggle_visible)
    return wp


async def my_input(self, msg):
    self.div.text = self.value


async def input_demo(request):
    wp = jp.WebPage()
    in1 = jp.Input(a=wp, classes=input_classes, placeholder="Please type here")
    in1.div = jp.Div(text="What you type will show up here", classes=p_classes, a=wp)
    in1.on("input", my_input)
    return wp


def color_demo(request):
    wp = jp.WebPage()
    in1 = jp.Input(
        type="color",
        a=wp,
        classes="m-2 p-2",
        style="width: 100px; height: 100px",
        input=color_change,
        debounce=30,
    )
    in1.d = jp.Div(
        text="Click box above to change color of this text",
        a=wp,
        classes="border m-2 p-2 text-2x1 font-bold",
    )
    return wp


def color_change(self, msg):
    self.d.style = f"color: {self.value}"
    self.d.text = f"The color of this text is: {self.value}"


def radio_changed(self, msg):
    self.result_div.text = ""
    d = jp.Div(a=self.result_div, classes="m-2 p-2 border")
    for btn in self.btn_list:
        if btn.checked:
            jp.Span(text=f"{btn.value} is checked", a=d, classes="text-green-500 mr-6")
        else:
            jp.Span(
                text=f"{btn.value} is NOT checked", a=d, classes="text-red-500 mr-6"
            )


def radio_test():
    wp = jp.WebPage()
    genders = ["male", "female", "other"]
    ages = [(0, 30), (31, 60), (61, 100)]

    outer_div = jp.Div(classes="border m-2 p-2 w-64", a=wp)
    # Create div to show radio button selection but don't add yet to page. It will be added at the end
    # It is created here so that it could be assigned to the radio button attribute result_div
    result_div = jp.Div(
        text="Click radio buttons to see results here", classes="m-2 p-2 text-xl"
    )

    jp.P(a=outer_div, text="Please select your gender:")
    gender_list = []
    for gender in genders:
        label = jp.Label(classes="inline-block mg-1 p-1", a=outer_div)
        radio_btn = jp.Input(
            type="radio",
            name="gender",
            value=gender,
            a=label,
            btn_list=gender_list,
            result_div=result_div,
            change=radio_changed,
        )
        gender_list.append(radio_btn)
        jp.Span(classes="ml-1", a=label, text=gender.capitalize())

    jp.Div(a=outer_div, classes="m-2")  # Add spacing and line break

    jp.P(a=outer_div, text="Please select your age:")
    age_list = []
    for age in ages:
        label = jp.Label(classes="inline-block mb-1 p-1", a=outer_div)
        radio_btn = jp.Input(
            type="radio",
            name="age",
            value=age[0],
            a=label,
            btn_list=age_list,
            result_div=result_div,
            change=radio_changed,
        )
        age_list.append(radio_btn)
        jp.Span(classes="ml-1", a=label, text=f"{age[0]} - {age[1]}")
        jp.Br(a=outer_div)

    wp.add(result_div)
    return wp


def check_test():
    wp = jp.WebPage(data={'checked': True})
    label = jp.Label(a=wp, classes='m-2 p-2 inline-block')
    c = jp.Input(type='checkbox', classes='m-2 p-2 form-checkbox', a=label, model=[wp, 'checked'])
    caption = jp.Span(text='Click to get stuff', a=label)

    in1 = jp.Input(model=[wp, 'checked'], a=wp, classes='border block m-2 p-2')
    return wp


def my_blur(self, msg):
    self.set_focus = False

def key_down(self, msg):
    # print(msg.key_data)
    print(msg.key_data.key)
    key = msg.key_data.key
    if key == "Escape":
        self.value = ''
        return
    if key == "Enter":
        self.set_focus = False
        try:
            next_to_focus = self.input_list[self.num + 1]
        except:
            next_to_focus = self.input_list[0]
        next_to_focus.set_focus = True
        return
    return True # Don't update the page

def focus_test():
    wp = jp.WebPage()
    d = jp.Div(classes = 'flex flex-col m-2', a=wp, style='width: 600 px')
    input_list = []
    number_of_fields = 5
    for i in range(1, number_of_fields + 1):
        label = jp.Label(a=d, classes = 'm-2 p-2')
        jp.Span(text=f'Field {i}', a=label)
        in1 = jp.Input(classes = jp.Styles.input_classes, placeholder=f'{i} Type here', a=label, keydown=key_down, spellcheck='false')
        in1.on('blur', my_blur)
        in1.input_list = input_list
        in1.num = i-1
        input_list.append(in1)
    print(input_list)
    return wp


def reset_all(self, msg):
    msg.page.data['text'] = ''


async def model_demo(request):
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


my_html = """
    <div>
    <p class = "m-2 p-2 text-red-500 text-xl">Paragraph 1</p>
    <p class = "m-2 p-2 text-blue-500 text-xl">Paragraph 2</p>
    <p class = "m-2 p-2 text-green-500 text-xl">Paragraph 3</p>
    """

def inner_demo():
    wp = jp.WebPage()
    d = jp.Div(a=wp, classes = 'm-4 p-4 text-3x1')
    d.inner_html = '<pre>Hello there. \n How are you?</pre>'
    jp.Div(a=wp, inner_html=my_html)
    for color in ['red', 'green', 'blue', 'pink', 'yellow', 'teal', 'purple']:
        jp.Div(a=wp, inner_html=f'<p class="ml-2 text-{color}-500 text-3x1">{color}</p>')
    return wp

def html_demo():
    wp = jp.WebPage()
    jp.Div(text='This will not be shown', a=wp)
    wp.html = '<p class="text-2x1 m-2 m-1 text-red-500">Hello world!</p>'
    jp.Div(text='This will not be shown', a=wp)
    return wp

async def parse_demo(request):
    wp = jp.WebPage()
    c = jp.parse_html("""
    <div>
    <p class="m-2 p-2 text-red-500 text-xl">Paragraph 1</p>
    <p class="m-2 p-2 text-blue-500 text-xl">Paragraph 2</p>
    <p class="m-2 p-2 text-green-500 text-xl">Paragraph 3</p>
    </div>
    """, a=wp)
    print(c)
    print(c.components)
    return wp

jp.justpy(parse_demo, host=PUBLIC_IP)
