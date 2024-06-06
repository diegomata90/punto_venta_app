import reflex as rx
from punto_venta_app.styles.styles import Size as Size
import punto_venta_app.styles.styles as Styles
from punto_venta_app.styles.color import Color as Color
from punto_venta_app.styles.color import TextColor as TextColor

def header() -> rx.Component:
        return rx.box(
        rx.vstack(
                rx.heading("Admin"),
                bg = Color.PRIMARY.value,
                width = Styles.SIDEBAR_WIDTH,
                padding= Size.SMALL.value,
                position=" sticky",
                )       
        )