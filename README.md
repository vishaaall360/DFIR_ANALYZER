# 🔎 Digital Forensics & Incident Response (DFIR) Analyzer

The Digital Forensics & Incident Response (DFIR) Analyzer is a cyber-security project that simulates a real-world digital forensics investigation tool. It analyzes system logs and browser artifacts to reconstruct incident timelines and generate forensic reports, similar to tools used by Security Operations Centers (SOC) and DFIR teams.

This project demonstrates blue-team, incident response, and forensic analysis skills, making it a strong GitHub portfolio and academic project.

---

## 🚀 Features

- Analyzes system log files for security events
- Parses browser history artifacts
- Reconstructs a chronological incident timeline
- Generates a detailed forensic report
- Web-based dashboard for visualization
- Modular and extensible design

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** – Web framework
- **Pandas** – Data handling
- **HTML & CSS** – Frontend UI

---

## 📁 Project Structure

dfir-analyzer/
│
├── app.py
├── artifact_parser.py
├── timeline_builder.py
├── report_generator.py
├── requirements.txt
│
├── evidence/
│ ├── system.log
│ └── browser_history.csv
│
├── reports/
│ └── forensic_report.txt
│
├── templates/
│ └── dashboard.html
│
├── static/
│ └── style.css

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Run the Application

python app.py

3️⃣ Open in Browser

http://127.0.0.1:5000

🧠 How It Works

1.System logs and browser history files are loaded as evidence

2.Security-related events are parsed from the artifacts

3.A chronological timeline of events is created

4.A forensic report is generated automatically

5.The timeline is displayed on a web-based dashboard

6.This process simulates how digital forensics teams investigate incidents and reconstruct attack sequences.

🧪 Sample Evidence Used

1.System authentication logs

2.File access and deletion events

3.Browser visit history to suspicious URLs

📌 Use Cases

1.Digital forensics learning

2.Incident response simulations

3.SOC analyst training

4.Cyber-security academic projects

5.Blue-team portfolio development

🌱 Future Enhancements

1.File hash analysis

2.Memory and disk artifact parsing

3.Advanced timeline visualization

4.Exportable forensic reports (PDF)

5.Integration with SIEM tools

👨‍💻 Author

Vishaal S
GitHub: https://github.com/vishaal360

