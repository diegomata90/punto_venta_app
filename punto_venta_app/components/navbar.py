import reflex as rx
from punto_venta_app.styles.styles import Size as Size
from punto_venta_app.styles.color import Color as Color
from punto_venta_app.styles.color import TextColor as TextColor


def navbar() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.menu.root(
                rx.menu.trigger(
                    rx.button("Menu", variant="solid",color_scheme="cyan"),
                    ),
                rx.menu.content(
                    rx.menu.item("Edit", shortcut="⌘ E"),
                    rx.menu.item("Duplicate", shortcut="⌘ D"),
                    rx.menu.item("Other", shortcut="⌘ O"),
                )
        ),
        position="sticky",
        bg=Color.PRIMARY.value,
        padding=Size.SMALL.value,
        color = TextColor.HEADER.value,
    )
