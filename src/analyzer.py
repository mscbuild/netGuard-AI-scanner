import logging
from datetime import datetime

class TrafficAnalyzer:
    """A class for analyzing network events and making security decisions."""

    def __init__(self):
        # Trigger threshold for demonstrating logic (e.g. number of packets)
        self.connection_history = {}
        self.THRESHOLD = 50 

    def analyze_connection(self, src_ip: str, port: int) -> bool:
        """
        Basic heuristic analysis.
        Returns True if an anomaly was detected.
        """
        # We count the number of requests from one IP to a specific port
        key = f"{src_ip}:{port}"
        self.connection_history[key] = self.connection_history.get(key, 0) + 1

        if self.connection_history[key] > self.THRESHOLD:
            self._log_anomaly(src_ip, port)
            return True
        return False

    def _log_anomaly(self, ip: str, port: int):
        """Internal method for recording serious incidents."""
        logging.critical(f"ALERT: Suspected brute-force or scanning: {ip} at the port {port}")
