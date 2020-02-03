

import folium


def inline_map(m):
    from folium import Map
    from IPython.display import HTML, IFrame
    if isinstance(m, Map):
        m._build_map()
        srcdoc = m.HTML.replace('"', '&quot;')
        embed = HTML('<iframe srcdoc="{srcdoc}" '
                     'style="width: 100%; height: 500px; '
                     'border: none"></iframe>'.format(srcdoc=srcdoc))
    elif isinstance(m, str):
        embed = IFrame(m, width=750, height=500)
    return embed
min_lon = -(45 + (58 + 32.27/60) / 60)  # 45°58'32.27"W
max_lon = -(45 + (57 + 54.54/60) / 60)  # 45°57'54.54"W
min_lat = -(23 + (47 +  7.65/60) / 60)  # 23°47' 7.65"S
max_lat = -(23 + (46 + 42.25/60) / 60)  # 23°46'42.25"S

width, height = 650, 500
mapa = folium.Map(location=[-47.563861111111109, -91.940780555555563],
                  min_lon=min_lon, max_lon=max_lon, min_lat=min_lat, max_lat=max_lat,
                  tiles='Stamen Toner', width=width, height=height, zoom_start=15)

inline_map(mapa)

