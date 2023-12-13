from json import load, dump


def parse_zap_report(file_path: str):
    f = open(file_path)
    data = load(f)
    f.close()
    parsed_alerts = {"vulnerabilities": []}
    alerts = data["site"][0]["alerts"]
    for alert in alerts:
        name_vulnerability = alert["name"]
        count = int(alert["count"])
        parsed_alerts["vulnerabilities"].append(
            {"name": name_vulnerability,
             "count": count})
    with open(f"parsed_{file_path}", "w") as f:
        dump(parsed_alerts, f)
