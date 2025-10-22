#imputer
#numbers -> fill NaN with mean
#strings -> fill NaN with mode

import pandas as pd

def simple_imputer(df):
    out = df.copy()
    for col in out.columns:
        if pd.api.types.is_numeric_dtype(out[col]):
            mean_value = out[col].mean()
            out[col] = out[col].fillna(mean_value)
        else:
            mode_value = out[col].mode()[0]
            out[col] = out[col].fillna(mode_value)
    return out
if __name__ == "__main__":
    data = pd.DataFrame({
        'age': [25, 30, None, 22, 28],
        'city': ['New York', None, 'Los Angeles', 'New York', 'Chicago']
    })
    print("Original DataFrame:")
    print(data)

    imputed = simple_imputer(data)
    print("\nImputed DataFrame:")
    print(imputed)