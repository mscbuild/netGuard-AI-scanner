import argparse
import sys
from src.sniffer import TrafficSniffer
from src.analyzer import TrafficAnalyzer

def main():
    # Setting command line arguments
    parser = argparse.ArgumentParser(description="NetGuard-AI: Sniffer and traffic analyzer.")
    parser.add_argument("-i", "--interface", help="Network interface (e.g. eth0, wlan0)", default="eth0")
    parser.add_argument("-c", "--count", help="Number of packets to capture (0 = endlessly)", type=int, default=0)
    
    args = parser.parse_args()

    print("--- NetGuard-AI Security Monitor ---")
    print(f"[*] Initializing the analyzer...")
    
    # Initializing components
    analyzer = TrafficAnalyzer()
    
    # We create a sniffer and pass it a callback with the analysis logic
    # (Dependency injection: the sniffer doesn't know HOW to analyze, it just sends packets)
    sniffer = TrafficSniffer(interface=args.interface)

    try:
        # Let's start the capture. Please note: Scapy requires sudo privileges to run.
        sniffer.start_capture(count=args.count)
    except PermissionError:
        print("[!] Error: Insufficient privileges. Run the script with sudo..")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[*] Monitoring has been stopped by the user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
