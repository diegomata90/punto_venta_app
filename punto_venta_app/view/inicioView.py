import reflex as rx

from punto_venta_app.styles.styles import Size as Size
import punto_venta_app.styles.styles as Styles
from punto_venta_app.styles.color import Color as Color 
from punto_venta_app.styles.color import TextColor as TextColor
from punto_venta_app.components.card import card as Card 



def inicioView() -> rx.Component:
    return rx.vstack(
        rx.heading("Inicio"),
        rx.text("This is the main content of the page." , style=Styles.subtitle_Style),

        Card(title="Card Inicio", text="Inicio", footer="Footer"),

        min_height = Styles.MIN_HEIGHT,
        padding_x= Size.DEFAULT.value,
        padding_y= Size.DEFAULT.value,        
    )