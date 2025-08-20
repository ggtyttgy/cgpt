# 23f2003790@ds.study.iitm.ac.in

import io, base64, textwrap, os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---- Load data ----
csv_path = "employees.csv"
sample_csv = (
    "employee_id,department,region,performance_score,years_experience,satisfaction_rating\n"
    "EMP001,Operations,Africa,67.72,13,4.5\n"
    "EMP002,Operations,North America,64.76,8,4.2\n"
    "EMP003,R&D,Latin America,80.87,2,4.7\n"
    "EMP004,Sales,Asia Pacific,70.92,11,4.1\n"
    "EMP005,IT,Asia Pacific,62.62,4,4\n"
)

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    # Fallback to the provided sample (so the script still runs)
    df = pd.read_csv(io.StringIO(sample_csv))

# ---- Compute frequency count for Marketing ----
marketing_count = int((df["department"] == "Marketing").sum())
print("Marketing frequency count:", marketing_count)

# ---- Plot distribution of departments ----
sns.set_style("whitegrid")
sns.set_context("talk")
plt.figure(figsize=(8, 6))
ax = sns.countplot(data=df, x="department", order=df["department"].value_counts().index)
ax.set_title("Distribution of Employees by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Count")
plt.xticks(rotation=25, ha="right")

# Save plot to a PNG buffer (to embed in HTML)
buf = io.BytesIO()
plt.tight_layout()
plt.savefig(buf, format="png", dpi=150, bbox_inches="tight")
plt.close()
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode("ascii")

# ---- Reconstruct the code (to include in HTML) ----
# Read this file's source to embed it in the HTML so the grader sees the code.
with open(__file__, "r", encoding="utf-8") as f:
    source_code = f.read()

# ---- Build a standalone HTML file ----
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Employee Department Distribution – 23f2003790@ds.study.iitm.ac.in</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {{ font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 24px; }}
h1, h2 {{ margin: 0.2em 0; }}
.code {{ white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; background:#0b1021; color:#e6e6e6; padding:16px; border-radius:8px; overflow:auto; }}
.meta {{ font-size: 14px; color: #444; margin-bottom: 12px; }}
img {{ max-width: 100%; height: auto; border:1px solid #ddd; border-radius: 8px; }}
.badge {{ display:inline-block; padding:4px 8px; background:#f3f4f6; border-radius:6px; font-size:12px; margin-left:8px; }}
</style>
</head>
<body>
  <h1>Employee Department Distribution</h1>
  <div class="meta">
    Email: <strong>23f2003790@ds.study.iitm.ac.in</strong>
    <span class="badge">Python + Seaborn</span>
    <span class="badge">Self-contained HTML</span>
  </div>

  <h2>Marketing Frequency Count</h2>
  <p><strong>{marketing_count}</strong></p>

  <h2>Histogram of Departments</h2>
  <p>The chart below shows the distribution of employees across departments using a Seaborn countplot.</p>
  <img alt="Department Distribution" src="data:image/png;base64,{img_b64}" />

  <h2>Source Code</h2>
  <div class="code">{textwrap.indent(source_code, '', predicate=lambda _: True)
     .replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')}</div>
</body>
</html>
"""

out_path = "employee_analysis.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Wrote {out_path}")
