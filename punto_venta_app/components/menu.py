import reflex as rx

from punto_venta_app.components.link_button import link_button as link_button

def menu()->rx.Component:
    return rx.box(
        link_button("Inicio","/inicio","home"),
        link_button("Venta","/sales","shopping-cart"),
        link_button("Inventario","/inventory","clipboard-list"),
        link_button("Ingreso","/entry","clipboard-list"),
        link_button("Other","/#","box"),
    )
