import pandas as pd

def parse_system_logs(path):
    events = []
    with open(path, "r") as f:
        for line in f:
            events.append(line.strip())
    return events

def parse_browser_history(path):
    return pd.read_csv(path)
