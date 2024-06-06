import reflex as rx

from punto_venta_app.styles.styles import Size as Size


def card(title: str, text:str, footer:str) -> rx.Component:
    return rx.chakra.card(
        rx.chakra.text(text),
        header=rx.chakra.heading(title, size="md"),
        footer=rx.chakra.heading(footer, size="sm"),        
        )
    