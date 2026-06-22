import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report,
                              confusion_matrix, ConfusionMatrixDisplay)
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os, warnings
warnings.filterwarnings("ignore")

OUTPUT = os.path.dirname(os.path.abspath(__file__))

# ╔══════════════════════════════════════════════════════╗
# ║        EMPLOYEE SALARY PREDICTION SYSTEM             ║
# ╚══════════════════════════════════════════════════════╝

def banner(title):
    print("\n" + "═" * 58)
    print(f"  {title}")
    print("═" * 58)

def section(title):
    print("\n" + "─" * 58)
    print(f"  STEP {title}")
    print("─" * 58)

banner("EMPLOYEE SALARY PREDICTION SYSTEM")

# ══════════════════════════════════════════════════════════
# STEP 1 — Load Dataset
# ══════════════════════════════════════════════════════════
section("1 │ Load Dataset")

df = pd.read_csv("employees.csv")

# Inject some missing values to demonstrate handling
np.random.seed(42)
miss_idx_sal = np.random.choice(df.index, size=4, replace=False)
miss_idx_city = np.random.choice(df.index, size=3, replace=False)
df.loc[miss_idx_sal, "salary"] = np.nan
df.loc[miss_idx_city, "city"] = np.nan

print(f"\n  Rows loaded    : {df.shape[0]}")
print(f"  Columns        : {list(df.columns)}")
print(f"  Missing values : {df.isnull().sum().sum()} total")
print(f"\n  Missing per column:")
print(df.isnull().sum().to_string())
print(f"\n  First 5 rows:")
print(df.head().to_string(index=False))

# ══════════════════════════════════════════════════════════
# STEP 2 — Handle Missing Values
# ══════════════════════════════════════════════════════════
section("2 │ Handle Missing Values")

# Salary → mean imputation
sal_missing = df["salary"].isnull().sum()
sal_imputer = SimpleImputer(strategy="mean")
df["salary"] = sal_imputer.fit_transform(df[["salary"]]).astype(int)
print(f"\n  salary  : {sal_missing} nulls filled with mean = {df['salary'].mean():,.0f}")

# City → most frequent imputation
city_missing = df["city"].isnull().sum()
city_imputer = SimpleImputer(strategy="most_frequent")
df["city"] = city_imputer.fit_transform(df[["city"]]).ravel()
print(f"  city    : {city_missing} nulls filled with '{df['city'].value_counts().idxmax()}'")

print(f"\n  Missing values after handling: {df.isnull().sum().sum()} ")

# ══════════════════════════════════════════════════════════
# STEP 3 — Encode Categorical Columns
# ══════════════════════════════════════════════════════════
section("3 │ Encode City & Department")

le_city = LabelEncoder()
le_dept = LabelEncoder()

df["city_encoded"]       = le_city.fit_transform(df["city"])
df["department_encoded"] = le_dept.fit_transform(df["department"])

print("\n  City encoding:")
for city, code in sorted(zip(le_city.classes_, le_city.transform(le_city.classes_))):
    print(f"    {city:<12} → {code}")

print("\n  Department encoding:")
for dept, code in sorted(zip(le_dept.classes_, le_dept.transform(le_dept.classes_))):
    print(f"    {dept:<12} → {code}")

# ══════════════════════════════════════════════════════════
# STEP 4 — Create Salary Category (Target) + Scale Features
# ══════════════════════════════════════════════════════════
section("4 │ Create Target + Scale Features")

# Create salary category label
def salary_category(sal):
    if sal < 50000:   return "Low"
    elif sal < 85000: return "Medium"
    else:             return "High"

df["salary_category"] = df["salary"].apply(salary_category)

print("\n  Salary category distribution:")
print(df["salary_category"].value_counts().to_string())
print("\n  Thresholds:")
print("    Low    → salary < 50,000")
print("    Medium → 50,000 ≤ salary < 85,000")
print("    High   → salary ≥ 85,000")

# Scale numeric features
scaler = StandardScaler()
scale_cols = ["age", "experience_years", "salary"]
df[["age_scaled", "exp_scaled", "salary_scaled"]] = scaler.fit_transform(df[scale_cols])

print(f"\n  StandardScaler applied on: {scale_cols}")
print("  (mean=0, std=1 after scaling)")

# ══════════════════════════════════════════════════════════
# STEP 5 — Train ML Model
# ══════════════════════════════════════════════════════════
section("5 │ Train ML Models")

# Features and target
FEATURES = ["age_scaled", "exp_scaled", "city_encoded", "department_encoded"]
TARGET   = "salary_category"

X = df[FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

print(f"\n  Features used  : {FEATURES}")
print(f"  Training rows  : {len(X_train)}")
print(f"  Testing rows   : {len(X_test)}")

# Model 1: Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Model 2: Logistic Regression
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)

print("\n   Random Forest trained    (100 trees)")
print("   Logistic Regression trained")

# ══════════════════════════════════════════════════════════
# STEP 6 — Predict Salary Category
# ══════════════════════════════════════════════════════════
section("6 │ Predict Salary Category")

rf_preds = rf.predict(X_test)
lr_preds = lr.predict(X_test)

print("\n  Sample predictions (first 8 test rows):")
print(f"\n  {'Actual':<10} {'RandomForest':<15} {'LogisticReg':<15}")
print("  " + "-" * 40)
for actual, rf_p, lr_p in zip(list(y_test)[:8], rf_preds[:8], lr_preds[:8]):
    rf_mark = "T" if rf_p == actual else "F"
    lr_mark = "T" if lr_p == actual else "F"
    print(f"  {actual:<10} {rf_p:<13}{rf_mark}  {lr_p:<13}{lr_mark}")

# Predict a brand-new employee
print("\n" + "─" * 58)
print("  NEW EMPLOYEE PREDICTION")
print("─" * 58)
new_emp = pd.DataFrame({
    "age": [30], "experience_years": [6], "city": ["Delhi"], "department": ["IT"]
})
new_emp["city_encoded"]       = le_city.transform(new_emp["city"])
new_emp["department_encoded"] = le_dept.transform(new_emp["department"])
age_mean, exp_mean, sal_mean = scaler.mean_[:2], scaler.mean_[:2], scaler.mean_[2]
age_std,  exp_std            = scaler.scale_[0], scaler.scale_[1]

new_scaled = np.array([[
    (30  - scaler.mean_[0]) / scaler.scale_[0],
    (6   - scaler.mean_[1]) / scaler.scale_[1],
    new_emp["city_encoded"].values[0],
    new_emp["department_encoded"].values[0]
]])

rf_new = rf.predict(new_scaled)[0]
lr_new = lr.predict(new_scaled)[0]
rf_prob = rf.predict_proba(new_scaled)[0]
lr_prob = lr.predict_proba(new_scaled)[0]

print(f"\n  Employee: Age=30, Experience=6yr, City=Delhi, Dept=IT")
print(f"\n  Random Forest   → {rf_new}")
rf_classes = rf.classes_
for cls, prob in zip(rf_classes, rf_prob):
    bar = "|" * int(prob * 30)
    print(f"    {cls:<8} {bar:<30} {prob*100:.1f}%")
print(f"\n  Logistic Reg    → {lr_new}")
lr_classes = lr.classes_
for cls, prob in zip(lr_classes, lr_prob):
    bar = "|" * int(prob * 30)
    print(f"    {cls:<8} {bar:<30} {prob*100:.1f}%")

# ══════════════════════════════════════════════════════════
# STEP 7 — Evaluate Accuracy
# ══════════════════════════════════════════════════════════
section("7 │ Evaluate Model Accuracy")

rf_acc = accuracy_score(y_test, rf_preds)
lr_acc = accuracy_score(y_test, lr_preds)

print(f"\n  {'Model':<22} {'Accuracy':>10}")
print("  " + "-" * 34)
print(f"  {'Random Forest':<22} {rf_acc*100:>9.1f}%  {' Best' if rf_acc >= lr_acc else ''}")
print(f"  {'Logistic Regression':<22} {lr_acc*100:>9.1f}%  {' Best' if lr_acc > rf_acc else ''}")

print("\n  Random Forest — Classification Report:")
print(classification_report(y_test, rf_preds, zero_division=0))

# Feature importance
print("  Random Forest — Feature Importance:")
importances = rf.feature_importances_
feat_names  = ["age", "experience", "city", "department"]
for feat, imp in sorted(zip(feat_names, importances), key=lambda x: -x[1]):
    bar = "█" * int(imp * 50)
    print(f"    {feat:<12} {bar:<50} {imp*100:.1f}%")

# ══════════════════════════════════════════════════════════
# VISUALIZATIONS
# ══════════════════════════════════════════════════════════
banner("GENERATING CHARTS")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Employee Salary Prediction System — Dashboard", fontsize=15, fontweight="bold")
COLORS = {"Low": "#E24B4A", "Medium": "#BA7517", "High": "#3B6D11"}

# Chart 1: Salary category distribution
ax1 = axes[0, 0]
cats = df["salary_category"].value_counts().reindex(["Low","Medium","High"])
bars = ax1.bar(cats.index, cats.values,
               color=[COLORS[c] for c in cats.index], width=0.5, edgecolor="white")
ax1.set_title("Salary Category Distribution", fontweight="bold")
ax1.set_ylabel("Number of Employees")
for bar, val in zip(bars, cats.values):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
             str(val), ha="center", va="bottom", fontweight="bold")
ax1.set_ylim(0, cats.max() + 3)
ax1.spines[["top","right"]].set_visible(False)

# Chart 2: Experience vs Salary scatter
ax2 = axes[0, 1]
for cat, grp in df.groupby("salary_category"):
    ax2.scatter(grp["experience_years"], grp["salary"],
                color=COLORS[cat], label=cat, alpha=0.8, s=70, edgecolors="white")
ax2.set_title("Experience vs Salary", fontweight="bold")
ax2.set_xlabel("Experience (years)")
ax2.set_ylabel("Salary (₹)")
ax2.legend(title="Category")
ax2.spines[["top","right"]].set_visible(False)

# Chart 3: Model accuracy comparison
ax3 = axes[1, 0]
models  = ["Random Forest", "Logistic Regression"]
accs    = [rf_acc * 100, lr_acc * 100]
colors3 = ["#185FA5", "#0F6E56"]
bars3   = ax3.barh(models, accs, color=colors3, height=0.4, edgecolor="white")
ax3.set_xlim(0, 110)
ax3.set_title("Model Accuracy Comparison", fontweight="bold")
ax3.set_xlabel("Accuracy (%)")
for bar, val in zip(bars3, accs):
    ax3.text(val + 1, bar.get_y() + bar.get_height()/2,
             f"{val:.1f}%", va="center", fontweight="bold")
ax3.spines[["top","right"]].set_visible(False)

# Chart 4: Feature importance
ax4 = axes[1, 1]
feat_sorted = sorted(zip(feat_names, importances), key=lambda x: x[1])
fnames, fimps = zip(*feat_sorted)
colors4 = ["#9FE1CB", "#5DCAA5", "#1D9E75", "#0F6E56"]
bars4   = ax4.barh(fnames, [i*100 for i in fimps],
                   color=colors4, height=0.4, edgecolor="white")
ax4.set_title("Feature Importance (Random Forest)", fontweight="bold")
ax4.set_xlabel("Importance (%)")
for bar, val in zip(bars4, fimps):
    ax4.text(val*100 + 0.3, bar.get_y() + bar.get_height()/2,
             f"{val*100:.1f}%", va="center", fontweight="bold")
ax4.spines[["top","right"]].set_visible(False)

plt.tight_layout()
chart_path = os.path.join(OUTPUT, "salary_prediction_dashboard.png")
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"\n  Chart saved → salary_prediction_dashboard.png")

# Confusion Matrix
fig2, (cax1, cax2) = plt.subplots(1, 2, figsize=(12, 4))
fig2.suptitle("Confusion Matrices", fontsize=13, fontweight="bold")
for ax, preds, title in [(cax1, rf_preds, "Random Forest"),
                          (cax2, lr_preds, "Logistic Regression")]:
    cm = confusion_matrix(y_test, preds, labels=["Low","Medium","High"])
    im = ax.imshow(cm, cmap="Blues")
    ax.set_xticks([0,1,2]); ax.set_yticks([0,1,2])
    ax.set_xticklabels(["Low","Medium","High"])
    ax.set_yticklabels(["Low","Medium","High"])
    ax.set_xlabel("Predicted"); ax.set_ylabel("Actual")
    ax.set_title(title, fontweight="bold")
    for i in range(3):
        for j in range(3):
            ax.text(j, i, cm[i,j], ha="center", va="center",
                    color="white" if cm[i,j] > cm.max()/2 else "black",
                    fontweight="bold", fontsize=14)
plt.tight_layout()
cm_path = os.path.join(OUTPUT, "confusion_matrices.png")
plt.savefig(cm_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Chart saved → confusion_matrices.png")

# Save cleaned ML-ready data
out_csv = os.path.join(OUTPUT, "employees_ml_ready.csv")
df.to_csv(out_csv, index=False)
print(f"  Data  saved → employees_ml_ready.csv")

banner("PIPELINE COMPLETE ")
print(f"  Random Forest Accuracy   : {rf_acc*100:.1f}%")
print(f"  Logistic Reg  Accuracy   : {lr_acc*100:.1f}%")
print(f"  Best Model               : {'Random Forest' if rf_acc >= lr_acc else 'Logistic Regression'}")
print(f"  Output folder            : {OUTPUT}")
print("═" * 58)
