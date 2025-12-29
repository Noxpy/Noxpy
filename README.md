
# Noxpy

**Noxpy** is an open-source, Python-based CVE inspection and validation framework designed to determine *actual exposure* to known vulnerabilities. Instead of relying solely on version matching, Noxpy uses pluggable, test-driven checks to verify whether a system, service, or configuration is genuinely vulnerable.

Noxpy is **extensible, auditable, and community-driven**, and is developed as an **ongoing project** with expanding CVE coverage and continuously refined validation logic.

---

## About the Project

Noxpy focuses on evidence-based vulnerability validation rather than simple detection. Traditional scanners often report vulnerabilities based on version strings alone; Noxpy aims to answer a more practical question:

*Can this vulnerability actually be exploited in the current environment?*

The project is designed to grow over time and to be safely extended by the community.

---

## Project Structure


noxpy/
├── noxpy.py
├── utils/
│   ├── banner.py
│   └── colors.py
├── vulnerabilities/
│   ├── **init**.py
│   ├── registry.py
│   ├── shellshock_2014.py
│   ├── bluekeep_2019.py
│   └── eternalblue_2017.py
├── README.md
└── LICENSE


- **noxpy.py** – main entry point  
- **utils/** – shared utilities (banner, colors)  
- **vulnerabilities/** – CVE validation modules and registry  

---

## Currently Implemented CVE Checks

The following vulnerability checks are currently implemented:

- **Shellshock (CVE-2014-6271)**  
  https://nvd.nist.gov/vuln/detail/CVE-2014-6271

- **BlueKeep (CVE-2019-0708)**  
  https://nvd.nist.gov/vuln/detail/CVE-2019-0708

- **EternalBlue (CVE-2017-0144)**  
  https://nvd.nist.gov/vuln/detail/CVE-2017-0144

Each module validates exploitability conditions rather than relying solely on version detection.

> Absence of a check does not imply safety. Noxpy does not aim for comprehensive CVE coverage.

---

## How It Works

1. Identify a CVE and its exploitation requirements  
2. Encode those requirements as a Python validation check  
3. Inspect the target system in a non-destructive manner  
4. Report clear vulnerable / not-vulnerable results with evidence  

---

## Disclaimer

All scripts are **non-destructive** and intended for **defensive security testing only**.

- No exploitation or payload delivery  
- No system modification  
- No denial-of-service behavior  

Use Noxpy only on systems you own or are explicitly authorized to test.

---

## Usage

Run all registered vulnerability checks:



python3 noxpy.py



---

## Adding New Checks

To add a new CVE check:

- Create a new Python module in `vulnerabilities/`  
- Implement validation logic following existing checks  
- Register the check in `vulnerabilities/registry.py`  
- Ensure the check is non-destructive and clearly documented  

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository and create a feature branch  
2. Add or improve a CVE validation module  
3. Ensure accuracy, clarity, and non-destructive behavior  
4. Submit a pull request for review  

---

## Author / Maintainer

Maintained by 0xMarturano.

---

## License

See the `LICENSE` file.
