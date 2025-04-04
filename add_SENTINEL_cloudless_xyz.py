"""
Hardcoded Sentinel-2 Cloudless XYZ Layers
Adds each layer to the QGIS Browser Panel (XYZ Tiles)
"""

from qgis.PyQt.QtCore import QSettings
from qgis.utils import iface

# Sentinel-2 Cloudless URLs (hardcoded)
sentinel_urls = [
    "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2018_3857/default/g/{z}/{y}/{x}.jpg",
    "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2019_3857/default/g/{z}/{y}/{x}.jpg",
    "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2020_3857/default/g/{z}/{y}/{x}.jpg",
    "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2021_3857/default/g/{z}/{y}/{x}.jpg",
    "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2022_3857/default/g/{z}/{y}/{x}.jpg",
    "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2023_3857/default/g/{z}/{y}/{x}.jpg",
    "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpg",
]

# Register each layer
for url in sentinel_urls:
    year = url.split("s2cloudless-")[-1].split("_")[0]
    name = f"SENTINEL_{year}"
    encoded_url = url.replace("{x}", "%7Bx%7D").replace("{y}", "%7By%7D").replace("{z}", "%7Bz%7D")

    base_key = f"qgis/connections-xyz/{name}"
    QSettings().setValue(f"{base_key}/url", encoded_url)
    QSettings().setValue(f"{base_key}/zmin", "0")
    QSettings().setValue(f"{base_key}/zmax", "18")
    QSettings().setValue(f"{base_key}/yOriginTop", True)
    print(f"✅ Added {name}")

# Refresh QGIS browser
iface.reloadConnections()
print("🎉 All SENTINEL layers have been added to the XYZ Tiles panel.")


