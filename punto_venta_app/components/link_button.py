import reflex as rx
from punto_venta_app.styles.styles import Size as Size
from punto_venta_app.styles.color import TextColor as TextColor
from punto_venta_app.styles.color import Color as Color



def link_button(text:str, url:str, ico:str) -> rx.Component:
    return rx.box(
        rx.link(
            rx.hstack(
                rx.icon(ico, size=18, color= TextColor.HEADER.value),
                rx.text(text, color= TextColor.HEADER.value)
            ),
            align="left",
            padding_x=Size.DEFAULT.value,
            padding_y=Size.DEFAULT.value,
            display="block",
            href=url,
        ),
        width="100%",
        _hover = {"background": Color.SECUNDARY.value}
    )