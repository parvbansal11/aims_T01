# ORDINAL ENCODING FORM SCRATCH
# This module provides a simple implementation of an Ordinal Encoder
# that converts categorical features into ordinal integers. 
# It allows specifying the order of categories and handles unknown categories.
#PARV BANSAL MNC 25/A12/049 

import pandas as pd
import numpy as np  

def ordinal_encode(df, orders, unknown_value=np.nan):
    out = df.copy()

    maps = {col: {cat: i for i, cat in enumerate(order)} for col, order in orders.items()}

    for col, mp in maps.items():
        if col not in out.columns:
            raise ValueError(f"Column '{col}' not in DataFrame")
        out[col] = out[col].map(mp)
        if unknown_value is not np.nan:
            out[col] = out[col].fillna(unknown_value)
        else:
            out[col] = out[col].astype(float)
    return out

if __name__ == "__main__":
    data = pd.DataFrame({
        'size': ['Small', 'Medium', 'Large', 'Medium', 'Extra Large'],
        'grade': ['A', 'B', 'C', 'D', 'A']
    })  
    orders = {
        'size': ['Small', 'Medium', 'Large'],
        'grade': ['D', 'C', 'B', 'A']
    }   
    print("Original DataFrame:")
    print(data)

    enc = ordinal_encode(data, orders, unknown_value=-1)
    print("\nEncoded DataFrame:")
    print(enc)