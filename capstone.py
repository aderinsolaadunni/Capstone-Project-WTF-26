
import numpy as np
import pandas as pd

# Food byproduct category structure
category_structure = {
    "Plant-Based": [
        "Vegetable Residue",
        "Fruit Pulp",
        "Grain Husk",
        "Root/Tuber Peels"
    ],
    "Animal-Based": [
        "Meat Trimmings",
        "Fish Waste",
        "Poultry Residue",
        "Dairy Whey"
    ],
    "Oil & Fat": [
        "Used Cooking Oil",
        "Animal Fat Residue"
    ]
}

# Real-world perishability + moisture ranges (by subcategory)
subcategory_properties = {
    # Plant-Based
    "Vegetable Residue": {"perish_min": 24, "perish_max": 48, "moisture_min": 0.6, "moisture_max": 0.85},
    "Fruit Pulp": {"perish_min": 12, "perish_max": 36, "moisture_min": 0.7, "moisture_max": 0.9},
    "Grain Husk": {"perish_min": 120, "perish_max": 240, "moisture_min": 0.1, "moisture_max": 0.3},  # very dry, lasts long
    "Root/Tuber Peels": {"perish_min": 24, "perish_max": 72, "moisture_min": 0.5, "moisture_max": 0.8},

    # Animal-Based
    "Meat Trimmings": {"perish_min": 6, "perish_max": 12, "moisture_min": 0.65, "moisture_max": 0.85},
    "Fish Waste": {"perish_min": 4, "perish_max": 10, "moisture_min": 0.7, "moisture_max": 0.9},  # spoils fastest
    "Poultry Residue": {"perish_min": 6, "perish_max": 12, "moisture_min": 0.65, "moisture_max": 0.85},
    "Dairy Whey": {"perish_min": 8, "perish_max": 24, "moisture_min": 0.85, "moisture_max": 0.95},

    # Oil & Fat
    "Used Cooking Oil": {"perish_min": 168, "perish_max": 720, "moisture_min": 0.05, "moisture_max": 0.15},
    "Animal Fat Residue": {"perish_min": 120, "perish_max": 360, "moisture_min": 0.1, "moisture_max": 0.25}
}

# Typical reuse mapping
reuse_map = {
    "Vegetable Residue": "Compost",
    "Fruit Pulp": "Compost",
    "Grain Husk": "Animal Feed",
    "Root/Tuber Peels": "Animal Feed",
    "Meat Trimmings": "Bioenergy",
    "Fish Waste": "Bioenergy",
    "Poultry Residue": "Bioenergy",
    "Dairy Whey": "Animal Feed",
    "Animal Fat Residue": "Biofuel",
    "Used Cooking Oil": "Biofuel"
}

n = 1000
data = []

for i in range(n):

    # Select category and subcategory
    main_category = np.random.choice(list(category_structure.keys()))
    sub_category = np.random.choice(category_structure[main_category])

    # Get realistic properties
    props = subcategory_properties[sub_category]

    perishability = np.random.randint(props["perish_min"], props["perish_max"])
    moisture = np.random.uniform(props["moisture_min"], props["moisture_max"])

    record = {
        "byproduct_id": i + 1,
        "main_category": main_category,
        "sub_category": sub_category,
        "quantity_kg": np.random.randint(50, 2000),
        "moisture_level": round(moisture, 2),
        "perishability_hours": perishability,
        "contamination": np.random.choice([0, 1], p=[0.85, 0.15]),
        "latitude": np.random.uniform(6.4, 6.7),
        "longitude": np.random.uniform(3.2, 3.5),
        "typical_reuse": reuse_map[sub_category]
    }

    data.append(record)

df = pd.DataFrame(data)
print(df.head())

df.to_csv("food_byproducts_data.csv", index=False)
