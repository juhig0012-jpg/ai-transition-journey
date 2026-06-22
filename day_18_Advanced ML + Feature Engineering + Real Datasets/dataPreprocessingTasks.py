import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import os

print("=" * 55)
print("        ML DATA PREPROCESSING PIPELINE")
print("=" * 55)

# ── Load data ──────────────────────────────────────────────
df = pd.read_csv("dataPreprocessing.csv")

print("\n ORIGINAL DATA:")
print(df.to_string(index=False))
print(f"\n  Shape        : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"  Missing vals : {df.isnull().sum().sum()} total")
print(f"  Duplicates   : {df.duplicated().sum()} rows")

# ══════════════════════════════════════════════════════════
# TASK 1 — Fill salary missing values
# ══════════════════════════════════════════════════════════
print("\n" + "─" * 55)
print("TASK 1 │ Fill salary missing values")
print("─" * 55)

missing_before = df["salary"].isnull().sum()
imputer = SimpleImputer(strategy="mean")
df["salary"] = imputer.fit_transform(df[["salary"]]).astype(int)

print(f"  Rows fixed : {missing_before} (filled with mean = {df['salary'].mean():,.0f})")
print(f"  Missing now: {df['salary'].isnull().sum()}")

# ══════════════════════════════════════════════════════════
# TASK 2 — Replace null city
# ══════════════════════════════════════════════════════════
print("\n" + "─" * 55)
print("TASK 2 │ Replace null city values")
print("─" * 55)

missing_before = df["city"].isnull().sum()
city_imputer = SimpleImputer(strategy="most_frequent")
df["city"] = city_imputer.fit_transform(df[["city"]]).ravel()

most_freq = df["city"].value_counts().idxmax()
print(f"  Rows fixed : {missing_before} (filled with '{most_freq}')")
print(f"  Missing now: {df['city'].isnull().sum()}")

# ══════════════════════════════════════════════════════════
# TASK 3 — Remove duplicate rows
# ══════════════════════════════════════════════════════════
print("\n" + "─" * 55)
print("TASK 3 │ Remove duplicate rows")
print("─" * 55)

dupes_before = df.duplicated().sum()
print(f"  Duplicates found : {dupes_before}")
if dupes_before:
    print(df[df.duplicated(keep=False)].to_string(index=False))

df = df.drop_duplicates().reset_index(drop=True)
print(f"  Duplicates after : {df.duplicated().sum()}")
print(f"  Rows removed     : {dupes_before}")

# ══════════════════════════════════════════════════════════
# BONUS — Label Encode
# ══════════════════════════════════════════════════════════
print("\n" + "─" * 55)
print("BONUS  │ Label Encode city & name")
print("─" * 55)

df_encoded = df.copy()
le = LabelEncoder()
df_encoded["city_encoded"] = le.fit_transform(df_encoded["city"])
df_encoded["name_encoded"] = le.fit_transform(df_encoded["name"])
print("  LabelEncoder applied → city_encoded, name_encoded")

# ── Final output ───────────────────────────────────────────
print("\n" + "=" * 55)
print(" CLEANED DATA:")
print("=" * 55)
print(df_encoded[["name","age","salary","city","city_encoded","name_encoded"]].to_string(index=False))
print(f"\n  Final shape  : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"  Missing vals : {df.isnull().sum().sum()}")
print(f"  Duplicates   : {df.duplicated().sum()}")

# ── FIX: Save to same folder as the script (Windows-safe) ──
output_dir = os.path.dirname(os.path.abspath(__file__))
df.to_csv(os.path.join(output_dir, "cleaned_data.csv"), index=False)
df_encoded.to_csv(os.path.join(output_dir, "ml_ready_data.csv"), index=False)
print(f"\n  Files saved to: {output_dir}")
print("=" * 55)