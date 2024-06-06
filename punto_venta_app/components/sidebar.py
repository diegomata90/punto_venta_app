import reflex as rx

from punto_venta_app.components.link_button import link_button as link_button
import punto_venta_app.styles.styles as Styles
from punto_venta_app.styles.styles import Size as Size
from punto_venta_app.components.header import header as header
from punto_venta_app.styles.color import Color as Color

from punto_venta_app.components.menu import menu as menu

def sidebar()-> rx.Component:
        return rx.box(
                header(),
                menu(),
                bg =Color.PRIMARY.value,
                width = Styles.SIDEBAR_WIDTH,
                height = "100vh",
                position= "fixed",
                left ="0",
                top ="0",
                overflow_x ="hidden",
                paddin_top=Size.MEDIUM.value,
                z_index = "5",
                style=Styles.STYLESIDEBAR
        )