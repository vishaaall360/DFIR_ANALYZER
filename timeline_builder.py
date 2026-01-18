def build_timeline(system_events, browser_df):
    timeline = []

    for event in system_events:
        timeline.append(f"SYSTEM: {event}")

    for _, row in browser_df.iterrows():
        timeline.append(f"BROWSER: {row['timestamp']} visited {row['url']}")

    timeline.sort()
    return timeline
