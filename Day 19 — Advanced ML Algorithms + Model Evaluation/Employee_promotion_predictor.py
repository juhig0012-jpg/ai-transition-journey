import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os, warnings
warnings.filterwarnings("ignore")

OUTPUT = os.path.dirname(os.path.abspath(__file__))

# ╔══════════════════════════════════════════════════════╗
# ║        EMPLOYEE PROMOTION PREDICTOR                  ║
# ╚══════════════════════════════════════════════════════╝

def banner(title):
    print("\n" + "═" * 58)
    print(f"  {title}")
    print("═" * 58)

def section(title):
    print("\n" + "─" * 58)
    print(f"  STEP {title}")
    print("─" * 58)

banner("EMPLOYEE PROMOTION PREDICTOR")


# ══════════════════════════════════════════════════════════
# STEP 1 — Load Dataset
# ══════════════════════════════════════════════════════════
section("1 │ Load Dataset")

df = pd.read_csv("employees_promotion.csv")

print(f"\n  Rows loaded    : {df.shape[0]}")
print(f"  Columns        : {list(df.columns)}")
print(f"\n  First 5 rows:")
print(df.head().to_string(index=False))
print(f"\n  Class distribution:")
print(df["promoted"].value_counts().rename({0: "Not Promoted", 1: "Promoted"}).to_string())


# ══════════════════════════════════════════════════════════
# STEP 2 — Clean Data
# ══════════════════════════════════════════════════════════
section("2 │ Clean Data")

# Inject a few missing values to demonstrate handling
np.random.seed(42)
miss_exp  = np.random.choice(df.index, size=3, replace=False)
miss_perf = np.random.choice(df.index, size=4, replace=False)
df.loc[miss_exp,  "experience"]  = np.nan
df.loc[miss_perf, "performance"] = np.nan

print(f"\n  Missing values injected for demonstration:")
print(df.isnull().sum().to_string())

# Impute with mean
imputer = SimpleImputer(strategy="mean")
df[["experience", "performance"]] = imputer.fit_transform(
    df[["experience", "performance"]]
).round(1)

print(f"\n  After mean imputation — missing values: {df.isnull().sum().sum()}")
print(f"  Duplicates removed    : {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
print(f"  Rows after cleaning   : {df.shape[0]}")


# ══════════════════════════════════════════════════════════
# STEP 3 — Feature Selection & Scaling
# ══════════════════════════════════════════════════════════
section("3 │ Feature Selection & Scaling")

FEATURES = ["experience", "performance", "attendance"]
TARGET   = "promoted"

X = df[FEATURES]
y = df[TARGET]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=FEATURES)

print(f"\n  Features : {FEATURES}")
print(f"  Target   : {TARGET}  (0 = Not Promoted, 1 = Promoted)")
print(f"\n  StandardScaler applied — mean=0, std=1")
print(f"  Feature means  : {dict(zip(FEATURES, scaler.mean_.round(2)))}")
print(f"  Feature std    : {dict(zip(FEATURES, scaler.scale_.round(2)))}")


# ══════════════════════════════════════════════════════════
# STEP 4 — Train / Test Split
# ══════════════════════════════════════════════════════════
section("4 │ Train / Test Split (80 / 20)")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n  Training rows : {len(X_train)}")
print(f"  Testing rows  : {len(X_test)}")
print(f"\n  Train class balance:")
print(y_train.value_counts().rename({0:"Not Promoted",1:"Promoted"}).to_string())
print(f"\n  Test class balance:")
print(y_test.value_counts().rename({0:"Not Promoted",1:"Promoted"}).to_string())


# ══════════════════════════════════════════════════════════
# STEP 5 — Train All 4 ML Models
# ══════════════════════════════════════════════════════════
section("5 │ Train ML Models")

models = {
    "Logistic Regression" : LogisticRegression(max_iter=1000, random_state=42),
    "Decision Tree"       : DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest"       : RandomForestClassifier(n_estimators=100, random_state=42),
    "KNN"                 : KNeighborsClassifier(n_neighbors=5),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    print(f"\n  ✓ {name} trained")

print("\n  All models trained successfully.")


# ══════════════════════════════════════════════════════════
# STEP 6 — Predict
# ══════════════════════════════════════════════════════════
section("6 │ Predict on Test Set")

predictions = {name: model.predict(X_test) for name, model in models.items()}

print(f"\n  Sample predictions (first 10 test rows):\n")
header = f"  {'Actual':<10}" + "".join(f"{n[:10]:<14}" for n in models)
print(header)
print("  " + "─" * (10 + 14 * len(models)))

actual_list = list(y_test)
for i in range(min(10, len(y_test))):
    actual = actual_list[i]
    row = f"  {actual:<10}"
    for name, preds in predictions.items():
        mark = "T" if preds[i] == actual else "F"
        row += f"{preds[i]}  {mark}          "
    print(row)

# Predict a brand-new employee
print("\n" + "─" * 58)
print("  NEW EMPLOYEE PREDICTION")
print("─" * 58)
new_emp = pd.DataFrame({"experience": [6], "performance": [88], "attendance": [92]})
new_emp_scaled = scaler.transform(new_emp)

print(f"\n  Employee: Experience=6yr, Performance=88, Attendance=92%\n")
print(f"  {'Model':<24} {'Prediction':<18} {'Probability'}")
print("  " + "─" * 56)
for name, model in models.items():
    pred = model.predict(new_emp_scaled)[0]
    label = "Promoted ✓" if pred == 1 else "Not Promoted ✗"
    try:
        prob = model.predict_proba(new_emp_scaled)[0]
        prob_str = f"Not={prob[0]*100:.1f}%  Yes={prob[1]*100:.1f}%"
    except:
        prob_str = "N/A"
    print(f"  {name:<24} {label:<18} {prob_str}")


# ══════════════════════════════════════════════════════════
# STEP 7 — Compare Accuracy
# ══════════════════════════════════════════════════════════
section("7 │ Compare Model Accuracy")

accuracies = {name: accuracy_score(y_test, preds) for name, preds in predictions.items()}
best_model_name = max(accuracies, key=accuracies.get)

print(f"\n  {'Model':<26} {'Accuracy':>10}  {'Status'}")
print("  " + "─" * 48)
for name, acc in accuracies.items():
    tag = " ← Best" if name == best_model_name else ""
    print(f"  {name:<26} {acc*100:>9.1f}%{tag}")


# ══════════════════════════════════════════════════════════
# STEP 8 — Classification Reports
# ══════════════════════════════════════════════════════════
section("8 │ Classification Reports")

for name, preds in predictions.items():
    print(f"\n  ── {name} ──")
    print(classification_report(
        y_test, preds,
        target_names=["Not Promoted", "Promoted"],
        zero_division=0
    ))


# ══════════════════════════════════════════════════════════
# STEP 9 — Confusion Matrices (saved to PNG)
# ══════════════════════════════════════════════════════════
section("9 │ Confusion Matrices")

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle("Confusion Matrices — Employee Promotion Predictor",
             fontsize=14, fontweight="bold")

for ax, (name, preds) in zip(axes.flatten(), predictions.items()):
    cm = confusion_matrix(y_test, preds)
    disp = ConfusionMatrixDisplay(cm, display_labels=["Not Promoted", "Promoted"])
    disp.plot(ax=ax, cmap="Blues", colorbar=False)
    ax.set_title(name, fontweight="bold", fontsize=11)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

plt.tight_layout()
cm_path = os.path.join(OUTPUT, "confusion_matrices.png")
plt.savefig(cm_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"\n  Saved → confusion_matrices.png")


# ══════════════════════════════════════════════════════════
# VISUALIZATIONS DASHBOARD
# ══════════════════════════════════════════════════════════
banner("GENERATING CHARTS")

COLORS = ["#378ADD", "#BA7517", "#1D9E75", "#7F77DD"]
model_names = list(accuracies.keys())
acc_values  = [accuracies[n] * 100 for n in model_names]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Employee Promotion Predictor — Dashboard",
             fontsize=14, fontweight="bold")

# Chart 1: Accuracy comparison bar
ax1 = axes[0, 0]
bars = ax1.barh(model_names, acc_values, color=COLORS, height=0.5, edgecolor="white")
ax1.set_xlim(0, 115)
ax1.set_title("Model Accuracy Comparison", fontweight="bold")
ax1.set_xlabel("Accuracy (%)")
for bar, val in zip(bars, acc_values):
    ax1.text(val + 1, bar.get_y() + bar.get_height() / 2,
             f"{val:.1f}%", va="center", fontweight="bold", fontsize=10)
ax1.spines[["top", "right"]].set_visible(False)

# Chart 2: Promoted vs Not Promoted distribution
ax2 = axes[0, 1]
counts = df["promoted"].value_counts().sort_index()
labels = ["Not Promoted", "Promoted"]
ax2.bar(labels, counts.values, color=["#888780", "#1D9E75"], width=0.5, edgecolor="white")
ax2.set_title("Promotion Distribution", fontweight="bold")
ax2.set_ylabel("Number of Employees")
for i, val in enumerate(counts.values):
    ax2.text(i, val + 0.3, str(val), ha="center", fontweight="bold")
ax2.set_ylim(0, counts.max() + 8)
ax2.spines[["top", "right"]].set_visible(False)

# Chart 3: Feature importance from Random Forest
ax3 = axes[1, 0]
rf_model = models["Random Forest"]
importances = rf_model.feature_importances_
feat_sorted = sorted(zip(FEATURES, importances), key=lambda x: x[1])
fnames, fimps = zip(*feat_sorted)
imp_colors = ["#9FE1CB", "#5DCAA5", "#1D9E75"]
bars3 = ax3.barh(fnames, [i * 100 for i in fimps],
                 color=imp_colors, height=0.5, edgecolor="white")
ax3.set_title("Feature Importance (Random Forest)", fontweight="bold")
ax3.set_xlabel("Importance (%)")
for bar, val in zip(bars3, fimps):
    ax3.text(val * 100 + 0.3, bar.get_y() + bar.get_height() / 2,
             f"{val*100:.1f}%", va="center", fontweight="bold", fontsize=10)
ax3.spines[["top", "right"]].set_visible(False)

# Chart 4: Performance vs Experience scatter coloured by promotion
ax4 = axes[1, 1]
colors_map = {0: "#888780", 1: "#1D9E75"}
for label, grp in df.groupby("promoted"):
    ax4.scatter(grp["experience"], grp["performance"],
                c=colors_map[label],
                label="Promoted" if label else "Not Promoted",
                alpha=0.75, s=60, edgecolors="white")
ax4.set_title("Experience vs Performance", fontweight="bold")
ax4.set_xlabel("Experience (years)")
ax4.set_ylabel("Performance Score")
ax4.legend(title="Status")
ax4.spines[["top", "right"]].set_visible(False)

plt.tight_layout()
dash_path = os.path.join(OUTPUT, "promotion_dashboard.png")
plt.savefig(dash_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved → promotion_dashboard.png")


# ══════════════════════════════════════════════════════════
# STEP 10 — Choose Best Model
# ══════════════════════════════════════════════════════════
section("10 │ Choose Best Model")

best_acc = accuracies[best_model_name]
print(f"\n  Best Model   : {best_model_name}")
print(f"  Accuracy     : {best_acc*100:.1f}%")
print(f"\n  Classification Report for Best Model ({best_model_name}):")
print(classification_report(
    y_test, predictions[best_model_name],
    target_names=["Not Promoted", "Promoted"],
    zero_division=0
))

# Save ML-ready data
out_csv = os.path.join(OUTPUT, "employees_promotion_clean.csv")
df.to_csv(out_csv, index=False)
print(f"  Clean data saved → employees_promotion_clean.csv")

banner("PIPELINE COMPLETE")
for name, acc in accuracies.items():
    tag = " ← Best" if name == best_model_name else ""
    print(f"  {name:<26} {acc*100:.1f}%{tag}")
print(f"\n  Output folder : {OUTPUT}")
print("═" * 58)