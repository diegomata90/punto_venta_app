import reflex as rx
from enum import Enum
from .color import Color as Color
from .color import TextColor as TextColor
from .fonts import Font as Font

#Constants
MIN_HEIGHT = "0px"


#Sidebar
SIDEBAR_WIDTH = "160px"


#Sizes
class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    LARGE = "2em"

# Stylos base
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,

    "background":Color.BACKGROUND.value,

    rx.heading: {
        "font_family": Font.TITLE.value,
        "font_weight": "700",
        "color": TextColor.HEADER.value,
    },

    rx.link: {
        "color": TextColor.BODY.value,
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value
        }   
    },

    rx.chakra.card: {
        "bg" : Color.PRIMARY.value,
        "color": TextColor.HEADER.value,
        "size":"sm",
        "width":"100%",
        "height":"100%",
        "display":"flex",
        "flexDirection":"column",
        "justifyContent":"space-between",
        "variant": "outline",

    },
    rx.chakra.Heading: {
        "color":TextColor.ACCENT.value,
        "font_family": Font.TITLE.value
    }
}

STYLESIDEBAR = dict(  
    box_shadow = "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)",
    )

title_Style = dict(
    font_family = Font.TITLE.value,
    font_size = Size.MEDIUM.value,
    color     = TextColor.HEADER.value
    )

subtitle_Style = dict(
    font_family = Font.SUBTITLE.value,
    font_size = Size.DEFAULT.value,
    color     = TextColor.BODY.value
    )
