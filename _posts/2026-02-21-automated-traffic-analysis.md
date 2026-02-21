---
layout: post
title: "Automated Packet Sniffing and Traffic Analysis Protocol"
date: 2026-02-21 20:30:00 +0700
description: "An empirical demonstration of programmatic syntax highlighting utilizing a custom Python script for passive network reconnaissance."
---

## Executive Summary

During routine infrastructure monitoring, it became necessary to construct a lightweight, automated protocol to passively log incoming network requests. Relying on heavy, commercial graphical interfaces introduces unnecessary latency. Instead, a streamlined programmatic approach was executed.

## The Script Implementation

The following Python directive utilizes the `scapy` library to intercept and evaluate network packets in real-time. By isolating the `IP` and `TCP` layers, the script immediately flags unauthorized access attempts targeting restricted ports.

Notice how the syntax highlighting engine automatically isolates strings, functions, and boolean operators.

```python
import logging
from scapy.all import sniff, IP, TCP

# Configure secure logging environment
logging.basicConfig(filename='network_traffic.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def process_packet(packet):
    """
    Evaluates incoming packets and logs restricted access attempts.
    """
    if packet.haslayer(IP) and packet.haslayer(TCP):
        source_ip = packet[IP].src
        destination_port = packet[TCP].dport
        
        # Flag access attempts on secured ports (e.g., SSH, RDP)
        restricted_ports = [22, 3389]
        
        if destination_port in restricted_ports:
            alert_msg = f"[WARNING] Unauthorized scanning detected from {source_ip} on port {destination_port}"
            print(alert_msg)
            logging.warning(alert_msg)
        else:
            logging.info(f"Standard traffic: {source_ip} -> Port {destination_port}")

# Initiate passive reconnaissance
if __name__ == "__main__":
    print("[*] Initiating continuous network observation...")
    # Sniffing strictly on the primary interface
    sniff(iface="eth0", filter="tcp", prn=process_packet, store=False)