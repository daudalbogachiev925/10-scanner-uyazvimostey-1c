import pandas as pd, yaml

def build_report(findings):
    df = pd.DataFrame(findings)
    counts = df['severity'].value_counts().to_dict()
    with open('report.html', 'w') as f:
        f.write(f"<h1>Отчёт аудита</h1><pre>{counts}</pre>"
                f"{df.to_html()}")
