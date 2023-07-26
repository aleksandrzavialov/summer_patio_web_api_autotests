import enum


class FirefoxList(enum.Enum):
    IPhone_14ProMax = (1290, 2796),
    IPhone_8 = (750, 1334),
    IPhone_13Pro = (1170, 2532),


class ChromeList(enum.Enum):
    iPad_Mini = "iPad Mini",
    iPhone_SE = 'iPhone SE',
    Nexus_5 = 'Nexus 5',


class DeviceInfo:
    chrome_devices_dict = {
        "iPad_Mini": "iPad Mini",
        "iPhone_SE": 'iPhone SE',
        "Nexus_5": 'Nexus 5'

    }
    firefox_devices_dict = {
        "IPhone_14ProMax": (1290, 2796),
        "IPhone_8": (750, 1334),
        "IPhone_13Pro": (1170, 2532),
    }

    chrome_devices = ["iPad Mini", "iPhone SE", "Nexus 5"]
    firefox_devices = ["IPhone_14ProMax", "IPhone_8", "IPhone_13Pro"]


