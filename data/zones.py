zones = {

    # 🔴 HIGH STRESS ZONES
    7: {
        "name": "Hadapsar",
        "ndvi": 0.12,
        "population": 140000,
        "heat": 4.4,
        "flood_risk": 8,
        "neighbors": [3, 8, 29, 30],
        "wind_out": [29, 22],        # wind pushes east → Mundhwa, Dhanori
        "drain_to": [29]             # low-lying, drains toward Mundhwa
    },
    3: {
        "name": "Kondhwa",
        "ndvi": 0.10,
        "population": 41000,
        "heat": 4.8,
        "flood_risk": 7,
        "neighbors": [7, 11, 24],
        "wind_out": [7],             # wind flows north-east → Hadapsar
        "drain_to": [24, 7]          # Kondhwa elevated → drains to Dhankawadi + Hadapsar
    },
    15: {
        "name": "PCMC",
        "ndvi": 0.15,
        "population": 180000,
        "heat": 4.1,
        "flood_risk": 6,
        "neighbors": [23, 27],
        "wind_out": [23],            # industrial wind pushes south → Warje
        "drain_to": [23]             # terrain drains south toward Warje
    },
    21: {
        "name": "Yerwada",
        "ndvi": 0.09,
        "population": 160000,
        "heat": 4.6,
        "flood_risk": 9,
        "neighbors": [30, 22],
        "wind_out": [22],            # wind continues east → Dhanori
        "drain_to": [22]             # low basin, flood water flows to Dhanori
    },
    22: {
        "name": "Dhanori",
        "ndvi": 0.11,
        "population": 95000,
        "heat": 4.3,
        "flood_risk": 8,
        "neighbors": [21, 30],
        "wind_out": [],              # eastern edge, wind stops here
        "drain_to": []               # lowest point in this cluster, no outflow
    },

    # 🟡 MEDIUM STRESS ZONES
    8: {
        "name": "Wanowrie",
        "ndvi": 0.18,
        "population": 98000,
        "heat": 3.2,
        "flood_risk": 6,
        "neighbors": [7, 11],
        "wind_out": [7],             # wind moves north-east → Hadapsar
        "drain_to": [7]              # slight slope drains toward Hadapsar
    },
    11: {
        "name": "Bibvewadi",
        "ndvi": 0.20,
        "population": 72000,
        "heat": 3.0,
        "flood_risk": 5,
        "neighbors": [3, 8, 24],
        "wind_out": [8, 3],          # central zone, wind spreads east
        "drain_to": [3]              # drains south toward Kondhwa
    },
    12: {
        "name": "Karvenagar",
        "ndvi": 0.22,
        "population": 85000,
        "heat": 3.3,
        "flood_risk": 5,
        "neighbors": [23, 27],
        "wind_out": [23],            # wind flows east → Warje
        "drain_to": [23]             # slight downslope toward Warje
    },
    23: {
        "name": "Warje",
        "ndvi": 0.19,
        "population": 110000,
        "heat": 3.1,
        "flood_risk": 5,
        "neighbors": [12, 27, 15],
        "wind_out": [15],            # wind pushed north → PCMC corridor
        "drain_to": [15]             # flows north toward PCMC lowlands
    },
    24: {
        "name": "Dhankawadi",
        "ndvi": 0.17,
        "population": 78000,
        "heat": 3.5,
        "flood_risk": 6,
        "neighbors": [3, 11, 28],
        "wind_out": [3, 11],         # wind spreads to nearby stressed zones
        "drain_to": [3]              # drains north toward Kondhwa
    },

    # 🟢 LOW STRESS ZONES
    5: {
        "name": "Magarpatta",
        "ndvi": 0.25,
        "population": 60000,
        "heat": 2.5,
        "flood_risk": 4,
        "neighbors": [7, 29],
        "wind_out": [7, 29],         # green zone pushes clean air east
        "drain_to": [29]             # drains toward Mundhwa (lower)
    },
    25: {
        "name": "Pashan",
        "ndvi": 0.45,
        "population": 52000,
        "heat": 2.1,
        "flood_risk": 2,
        "neighbors": [26, 27],
        "wind_out": [26, 27],        # western green zone, clean wind source
        "drain_to": [27]             # drains east toward Kothrud
    },
    26: {
        "name": "Baner",
        "ndvi": 0.38,
        "population": 67000,
        "heat": 2.3,
        "flood_risk": 3,
        "neighbors": [25, 27],
        "wind_out": [27, 23],        # wind flows east → Kothrud → Warje
        "drain_to": [27]             # drains toward Kothrud
    },
    27: {
        "name": "Kothrud",
        "ndvi": 0.35,
        "population": 88000,
        "heat": 2.6,
        "flood_risk": 3,
        "neighbors": [12, 23, 25, 26],
        "wind_out": [12, 23],        # green corridor pushes air toward stressed zones
        "drain_to": [23]             # drains toward Warje
    },

    # 🔵 SPECIAL ZONES
    28: {
        "name": "Katraj",
        "ndvi": 0.30,
        "population": 73000,
        "heat": 2.8,
        "flood_risk": 9,
        "neighbors": [24],
        "wind_out": [24],            # hilltop → wind flows down to Dhankawadi
        "drain_to": [24, 3]          # Katraj lake area drains north → Dhankawadi, Kondhwa
    },
    29: {
        "name": "Mundhwa",
        "ndvi": 0.08,
        "population": 120000,
        "heat": 5.0,
        "flood_risk": 7,
        "neighbors": [7, 5],
        "wind_out": [],              # industrial dead-end, wind absorbed
        "drain_to": []               # low-lying industrial zone, water stagnates
    },
    30: {
        "name": "Viman Nagar",
        "ndvi": 0.21,
        "population": 145000,
        "heat": 3.4,
        "flood_risk": 5,
        "neighbors": [7, 21, 22],
        "wind_out": [21, 22],        # wind flows east → Yerwada, Dhanori
        "drain_to": [21]             # drains toward Yerwada (lower elevation)
    },
    31: {
        "name": "Sinhagad Road",
        "ndvi": 0.50,
        "population": 45000,
        "heat": 1.8,
        "flood_risk": 2,
        "neighbors": [27],
        "wind_out": [27, 12],        # highest elevation, clean wind source for entire west
        "drain_to": [27]             # hill runoff drains into Kothrud
    }
}
