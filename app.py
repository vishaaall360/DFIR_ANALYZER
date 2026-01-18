from flask import Flask, render_template
from artifact_parser import parse_system_logs, parse_browser_history
from timeline_builder import build_timeline
from report_generator import generate_report

app = Flask(__name__)

@app.route("/")
def dashboard():
    system_events = parse_system_logs("evidence/system.log")
    browser_history = parse_browser_history("evidence/browser_history.csv")

    timeline = build_timeline(system_events, browser_history)

    generate_report(timeline, "reports/forensic_report.txt")

    return render_template(
        "dashboard.html",
        timeline=timeline
    )

if __name__ == "__main__":
    app.run(debug=True)
