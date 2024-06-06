import reflex as rx
import datetime
from punto_venta_app.styles.styles import Size as Size
from punto_venta_app.styles.color import TextColor as TextColor

copy = f" © {datetime.date.today().year}  Diego Mata. All rights reserved.",

def footer() -> rx.Component:
    return rx.box(
        rx.link(
            rx.text(copy, _hover= {"color": TextColor.ACCENT.value}),
            color=TextColor.FOOTER.value,
            is_external=True,
            href="https://diegomata90.github.io/",
        ),
        width = "100%",
        position = "fixed",
        bottom = Size.DEFAULT.value,
        text_align = "center",
    )