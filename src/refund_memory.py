import json
import os
from datetime import datetime

DATA_FILE = "data/refund_logs.json"

class RefundMemory:
    def __init__(self, filepath=DATA_FILE):
        self.filepath = filepath
        self.logs = self._load_logs()

    def _load_logs(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r") as f:
            return json.load(f)

    def _save_logs(self):
        with open(self.filepath, "w") as f:
            json.dump(self.logs, f, indent=2)

    def log_refund(self, item_name, excuse, outcome, risk_level, category=None):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "item": item_name,
            "excuse": excuse,
            "outcome": outcome,  # e.g., "approved", "denied", "pending"
            "risk_level": risk_level,  # e.g., "low", "medium", "high"
            "category": category
        }
        self.logs.append(entry)
        self._save_logs()

    def get_successful_excuses(self):
        return [log["excuse"] for log in self.logs if log["outcome"] == "approved"]

    def get_stats(self):
        total = len(self.logs)
        approved = sum(1 for log in self.logs if log["outcome"] == "approved")
        denied = sum(1 for log in self.logs if log["outcome"] == "denied")
        pending = total - approved - denied
        return {
            "total_attempts": total,
            "approved": approved,
            "denied": denied,
            "pending": pending,
            "success_rate": round(approved / total * 100, 2) if total else 0
        }

    def get_risk_profile(self):
        risk_counts = {"low": 0, "medium": 0, "high": 0}
        for log in self.logs:
            risk = log.get("risk_level", "unknown")
            if risk in risk_counts:
                risk_counts[risk] += 1
        return risk_counts

    def get_recent_logs(self, limit=5):
        return self.logs[-limit:]

# Example usage
if __name__ == "__main__":
    memory = RefundMemory()
    memory.log_refund(
        item_name="Bluetooth Headphones",
        excuse="Item arrived with static noise and poor battery life.",
        outcome="approved",
        risk_level="medium",
        category="electronics"
    )

    print("✅ Successful Excuses:", memory.get_successful_excuses())
    print("📊 Stats:", memory.get_stats())
    print("⚠️ Risk Profile:", memory.get_risk_profile())
    print("🕓 Recent Logs:", memory.get_recent_logs())
