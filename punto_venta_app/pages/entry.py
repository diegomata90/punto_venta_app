import reflex as rx
import punto_venta_app.styles.styles as Styles

from punto_venta_app.components.sidebar import sidebar
from punto_venta_app.components.navbar import navbar
from punto_venta_app.view.inicioView import inicioView
from punto_venta_app.components.footer import footer

@rx.page(route="/entry", title="Ingreso")
def entry():
    return rx.box(  
        sidebar(),
        rx.box(
            navbar(),
            inicioView(),
            footer(),
            margin_left = Styles.SIDEBAR_WIDTH,
        )
)