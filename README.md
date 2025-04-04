# 🛰️ QGIS Script: Add SENTINEL XYZ Tiles to QGIS Browser

This script adds **Sentinel-2 Cloudless Basemaps** as **XYZ Tile layers** to your QGIS Browser Panel using the official tile services from [EOX](https://s2maps.eu/).

Each year (2016–2024) will appear as a persistent layer in the **Browser → XYZ Tiles** panel.

---

## 📂 Included

- `add_sentinel_xyz.py` – Python script to add Sentinel layers to QGIS.

---

## ▶️ How to Run This Script in QGIS

> ✅ Requires **QGIS 3.x**

### Step-by-step instructions:

1. **Open QGIS**

2. Go to the **Python Console**:
   - From the top menu: `Plugins → Python Console`

3. Click the **"Show Editor"** button in the Python Console (or press `Ctrl+Alt+E`).

4. Paste the script from `add_sentinel_xyz.py` **into the editor**, or load the file:
   - `File → Open Script` → Select `add_sentinel_xyz.py`

5. Click **"Run Script"** ▶️

---

## 🧭 Result

You will now see a list of new layers such as:

- `SENTINEL_2016`
- `SENTINEL_2017`
- ...
- `SENTINEL_2024`

They appear under **Browser → XYZ Tiles** and can be dragged into any map canvas.

---

## 🔄 Persistence

These XYZ connections are saved in your QGIS user settings and will remain available even after restarting QGIS.

---

## 🛠️ Customize

You can:
- Adjust the zoom levels (`zmin` / `zmax`)
- Rename or filter the layer list
- Extend the script to support **NICFI** or other tile services

---

## 🧼 Optional: Reset/Remove Existing Layers

To remove previously added SENTINEL layers from QGIS settings, run the following in the QGIS Python Console:

```python
from qgis.PyQt.QtCore import QSettings
prefix = "qgis/connections-xyz/"
settings = QSettings()
for key in settings.allKeys():
    if key.startswith(prefix + "SENTINEL_"):
        settings.remove(key)
