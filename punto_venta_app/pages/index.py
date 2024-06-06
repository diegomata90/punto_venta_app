import reflex as rx

import punto_venta_app.styles.styles as Styles

from punto_venta_app.components.sidebar import sidebar
from punto_venta_app.components.navbar import navbar
from punto_venta_app.view.indexView import indexView
from punto_venta_app.components.footer import footer

@rx.page(route="/", title="Index")
def index():
    return rx.box(  
        sidebar(),
        rx.box(
            navbar(),
            indexView(),
            footer(),
            margin_left = Styles.SIDEBAR_WIDTH,
        )
    )