def generate_report(timeline, output_path):
    with open(output_path, "w") as f:
        f.write("DIGITAL FORENSICS REPORT\n")
        f.write("=" * 40 + "\n\n")
        for event in timeline:
            f.write(event + "\n")