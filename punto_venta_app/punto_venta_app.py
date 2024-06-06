import reflex as rx
import punto_venta_app.styles.styles as Styles

from punto_venta_app.pages.index import index
from punto_venta_app.pages.inicio import inicio
from punto_venta_app.pages.inventory import inventory
from punto_venta_app.pages.sales import sales
from punto_venta_app.pages.entry import entry


from rxconfig import config


class State(rx.State):
    pass


app = rx.App(
    style = Styles.BASE_STYLE
    )

app.add_page(index)
app.add_page(inicio)
app.add_page(sales)
app.add_page(inventory)
app.add_page(entry)
