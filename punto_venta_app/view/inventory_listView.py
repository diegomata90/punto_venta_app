import reflex as rx
from punto_venta_app.styles.color import TextColor as TextColor

def inventory_listView() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.divider(),
            rx.hstack(
                rx.text(
                    f"Total: Items",
                    size="5",
                ),
                rx.spacer(),
            ),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Icon"),
                        rx.table.column_header_cell("Name"),
                        rx.table.column_header_cell("Email"),
                        rx.table.column_header_cell("Phone"),
                        rx.table.column_header_cell("Address"),
                        rx.table.column_header_cell("Edit"),
                        rx.table.column_header_cell("Delete"),
                        color=TextColor.HEADER.value,
                    ),
                    color=TextColor.HEADER.value,
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("ico"),
                        rx.table.row_header_cell("Danilo Sousa"),
                        rx.table.cell("danilo@example.com"),
                        rx.table.cell("506"),
                        rx.table.cell("San Jose"),
                        rx.table.cell("Edit"),
                        rx.table.cell("DELETE"),
                        color=TextColor.CONTENT.value,
                    ),
                ),
                # variant="surface",
                size="3",
                width="100%",
            ),
        ),
    )
