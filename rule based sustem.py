
import numpy as np
import pandas as pd

food_byproducts_data_df = pd.read_csv(r"C:\Users\PC\Documents\women techsers\PYTHON VS\exercis 1-5\food_byproducts_data.csv")
buyers_data_df = pd.read_csv(r"C:\Users\PC\Documents\women techsers\PYTHON VS\exercis 1-5\buyers_data.csv")
print(buyers_data_df.head())

def rule_based_category(row):

    hours = row['perishability_hours']
    moisture = row['moisture_level']

    # 1️⃣ Very urgent or very wet → bioenergy
    if hours <= 8 or (hours <= 24 and moisture > 0.75):
        return "bioenergy"

    # 2️⃣ Moderate perishability + medium/high moisture → compost
    elif 8 < hours <= 72 and moisture >= 0.5:
        return "compost"

    # 3️⃣ Long shelf life + low moisture → animal feed
    elif hours > 72 and moisture < 0.4:
        return "animal_feed"

    # 4️⃣ Default fallback
    else:
        return "biofuel"

food_byproducts_data_df['rule_based_category'] = food_byproducts_data_df.apply(rule_based_category, axis=1)

print(food_byproducts_data_df[['perishability_hours', 'moisture_level', 'rule_based_category']].head())


def rule_based_match(row, buyers_df):
    # Use the category we just created
    category = row['rule_based_category']
    
    matches = []
    
    for _, buyer in buyers_df.iterrows():
        # Fake distance (you can improve later with real coords)
        distance = abs(row['fake_lat'] - buyer['fake_lat']) + \
                   abs(row['fake_lon'] - buyer['fake_lon'])
        
        # Hard constraints (must always follow)
        if row['perishability_hours'] <= 8 and distance > 30:
            continue                    # too far for super-urgent waste
        
        if category == "bioenergy" and "bioenergy" not in buyer['Needs'].lower():
            continue
        
        if category == "compost" and "compost" not in buyer['Needs'].lower():
            continue
        
        if category == "animal_feed" and "animal feed" not in buyer['Needs'].lower():
            continue
        
        # If we reach here → it's a valid match
        score = 100 - distance * 2          # closer = higher score
        matches.append({
            'Buyer_ID': buyer['Buyer_ID'],   # change to your column name
            'Buyer_Name': buyer.get('Buyer_name', 'Unknown'),
            'Distance_km': round(distance, 1),
            'Category': category,
            'Reason': f"Rule match: {category} + distance {round(distance,1)} km",
            'Score': score
        })
    
    # Sort best first
    matches.sort(key=lambda x: x['Score'], reverse=True)
    return matches[:3]   # return top 3