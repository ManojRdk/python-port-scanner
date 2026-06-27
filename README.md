# Python Port Scanner

A simple TCP Port Scanner written in Python using the built-in `socket` module.

This project was created as part of my cybersecurity and networking learning journey to understand how TCP connections and port scanning work.

---

## Features

- Scan TCP ports from **1 to 1024**
- Accepts IP address or hostname
- Displays open ports
- Shows scan start time
- Handles common socket errors
- Beginner-friendly implementation

---

## Technologies Used

- Python 3
- Socket Module
- Datetime Module
- Command Line Interface (CLI)

---

## Project Structure

```
scanner.py
README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/python-port-scanner.git
```

Move into the project directory:

```bash
cd python-port-scanner
```

---

## Usage

Run the scanner using:

```bash
python3 scanner.py <target>
```

Example:

```bash
python3 scanner.py scanme.nmap.org
```

or

```bash
python3 scanner.py 192.168.1.1
```

---

## Sample Output

```
--------------------------------------------------
Scanning Target : 192.168.1.1
Time Started : 2026-06-27 14:30:21
--------------------------------------------------

Checking port 22
Port is Open 22

Checking port 80
Port is Open 80
```

---

## What I Learned

- Python socket programming
- TCP connections
- Port scanning fundamentals
- Hostname resolution
- Exception handling
- Command-line arguments
- Basic networking concepts
---

## Disclaimer

This project is intended for educational purposes only.

Only scan systems that you own or have explicit permission to test. Unauthorized scanning may violate laws or organizational policies.

---

