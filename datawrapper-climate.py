from datawrapper import Datawrapper
import pandas as pd
import os
from dotenv import load_dotenv

# 🔐 API-Key laden
load_dotenv()
api_key = os.getenv("DATAWRAPPER_APIKEY")

# 📡 Datawrapper initialisieren
dw = Datawrapper(access_token=api_key)

# 📊 CSV laden – passe den Pfad an, falls die Datei woanders liegt
df = pd.read_csv("processed/climate_change.csv")

# 🆔 Chart-IDs
chart_id_berlin = "IK03Y"
chart_id_brooklyn = "ZXp5I"

# 🎨 Farben als Dictionary (Spalten: year, color_*)
colors_berlin = dict(zip(df['year'], df['color_berlin']))
colors_brooklyn = dict(zip(df['year'], df['color_brooklyn']))

# 🔧 Funktion zum Aktualisieren und Veröffentlichen
def update_chart_colors(chart_id, color_dict):
    metadata = dw.get_chart(chart_id)
    metadata['metadata']['visualize']['custom-colors'] = color_dict
    metadata['metadata']['visualize']['show-legend'] = False  # 👈 Legende ausblenden
    dw.update_metadata(chart_id, metadata=metadata['metadata'])
    dw.publish_chart(chart_id)
    print(f"✅ Chart {chart_id} aktualisiert und veröffentlicht.")

# 🔁 Charts aktualisieren
update_chart_colors(chart_id_berlin, colors_berlin)
update_chart_colors(chart_id_brooklyn, colors_brooklyn)
