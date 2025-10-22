#One hot encoding

import pandas as pd

def one_hot_encode(df, columns, drop_first=False):
    out = df.copy()
    for col in columns:
        cats=[]
        for v in out[col]:
            if pd.isna(v):
                continue
            if v not in cats:
                cats.append(v)

    use_cats = cats[1:] if (drop_first and len(cats)>0) else cats

    for cat in use_cats:
        new_col = f"{col}_{cat}"
        out[new_col] = (out[col] == cat).astype(int)

    out = out.drop(columns=[col])
    return out

if __name__ == "__main__":
    data = pd.DataFrame({
        'color': ['Red', 'Blue', 'Green', 'Blue', 'Red'],
        'size': ['Small', 'Medium', 'Large', 'Medium', 'Extra Large']
    })
    print("Original DataFrame:")
    print(data)

    enc = one_hot_encode(data, columns=['color', 'size'], drop_first=True)
    print("\nOne-Hot Encoded DataFrame:")
    print(enc)