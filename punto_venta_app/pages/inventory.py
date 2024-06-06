import reflex as rx
import punto_venta_app.styles.styles as Styles

from punto_venta_app.components.sidebar import sidebar
from punto_venta_app.components.navbar import navbar
from punto_venta_app.components.footer import footer
from punto_venta_app.view.inventoryView import inventoryView

@rx.page(route="/inventory", title="Inventario")
def inventory():
    return rx.box(  
        sidebar(),
        rx.box(
            navbar(),
            inventoryView(),
            footer(),
            margin_left = Styles.SIDEBAR_WIDTH,
        )
)
