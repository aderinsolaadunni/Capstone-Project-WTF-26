import numpy as np
import pandas as pd

# ────────────────────────────────────────────────
# Define buyer main categories and what they accept
# ────────────────────────────────────────────────
buyer_categories = ['animal_feed', 'compost', 'bioenergy', 'biofuel']

# Mapping: main category → list of detailed subcategories it accepts
subcategory_map = {
    "animal_feed": ["Grain Husk", "Root/Tuber Peels", "Bakery Surplus", "Dairy Whey"],
    "compost":     ["Vegetable Residue", "Fruit Pulp", "Restaurant Prep Waste"],
    "bioenergy":   ["Meat Trimmings", "Fish Waste", "Poultry Residue", "Expired Packaged Food"],
    "biofuel":     ["Used Cooking Oil", "Animal Fat Residue"]
}

# ────────────────────────────────────────────────
# Generate synthetic buyers
# ────────────────────────────────────────────────
n_buyers = 200

buyer_data = []

for i in range(n_buyers):
    # Pick one main category
    main_category = np.random.choice(buyer_categories)
    
    # Get the subcategories this buyer accepts
    accepted_subs = subcategory_map[main_category]
    
    record = {
        "buyer_id":               i + 1,
        "buyer_name":             f"Buyer_{i+1}_{main_category.title()}",  # optional but helpful for demo
        "main_category":          main_category,                           # e.g. 'bioenergy'
        "needs":                  main_category + ", " + main_category,    # e.g. "bioenergy, bioenergy" — simple for now
        # Better version below — choose one:
        # "needs":                ", ".join(set([main_category] + accepted_subs)),  # includes subcats if you want
        
        "accepted_subcategories": ", ".join(accepted_subs),
        "max_capacity_kg":        np.random.randint(500, 8000),
        "current_available_kg":   np.random.randint(0, 6000),              # renamed for clarity
        "max_distance_km":        np.random.randint(10, 80),
        "demand_level":           round(np.random.uniform(0.2, 1.0), 2),
        "latitude":               np.random.uniform(6.4, 7.0),             # wider Lagos-Ibadan range if needed
        "longitude":              np.random.uniform(3.2, 4.0),
    }
    
    buyer_data.append(record)

# Create DataFrame
df_buyers = pd.DataFrame(buyer_data)

# Optional: make 'needs' more realistic (uncomment if you prefer)
df_buyers['needs'] = df_buyers.apply(
    lambda row: ", ".join([row['main_category']] + 
                          np.random.choice(row['accepted_subcategories'].split(", "), 
                                           size=np.random.randint(1,3), replace=False).tolist()),
    axis=1
)

# Save
df_buyers.to_csv("Buyers_new_data.csv", index=False)

# Quick check
print("Columns in buyers data:", df_buyers.columns.tolist())
print("\nFirst 3 rows:")
print(df_buyers.head(3)[['buyer_id', 'main_category', 'needs', 'accepted_subcategories', 
                         'max_capacity_kg', 'latitude', 'longitude']])