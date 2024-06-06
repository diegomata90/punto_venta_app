import reflex as rx

from punto_venta_app.styles.styles import Size as Size
import punto_venta_app.styles.styles as Styles
from punto_venta_app.styles.color import Color as Color 
from punto_venta_app.styles.color import TextColor as TextColor
from punto_venta_app.components.card import card as Card 

title = "Index Page"

def indexView() -> rx.Component:
    return rx.vstack(
        rx.heading("Welcome to Punto Venta App."),
        rx.text("This is the main content of the page." , style=Styles.subtitle_Style),

        Card(title="Card 1", text="This is card 1", footer="Footer 1"),

        min_height = Styles.MIN_HEIGHT,
        padding_x= Size.DEFAULT.value,
        padding_y= Size.DEFAULT.value,
        
    )