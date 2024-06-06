import reflex as rx

from punto_venta_app.styles.styles import Size as Size
import punto_venta_app.styles.styles as Styles
from punto_venta_app.styles.color import Color as Color 
from punto_venta_app.styles.color import TextColor as TextColor
from punto_venta_app.components.card import card as Card 
from punto_venta_app.view.inventory_listView import inventory_listView as inventory_listView



def inventoryView() -> rx.Component:
    return rx.vstack(
        # rx.heading("Inventario"),
        # rx.text("..." , style=Styles.subtitle_Style),

        Card(title="Lista de Inventario", text=inventory_listView(),footer=""),
        

        min_height = Styles.MIN_HEIGHT,
        padding_x= Size.DEFAULT.value,
        padding_y= Size.DEFAULT.value,        
    )