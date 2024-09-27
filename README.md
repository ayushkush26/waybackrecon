********Wayback Recon Tool********

****Overview****

This Recon Tool is a Python-based utility that helps security professionals to gather the archived URLs from the Wayback Machine for a given domain.This tool extracts URLs from archived web pages which can be use in penetration testing, and recon purposes and also supports filtering URLs by file extension and saving results to a file for further analysis.

****Requirements****

* Python 3.x
* Required Python libraries:
    **requests
    **argparse

****Usage****

 => python wayback_recon.py -d <domain> -o <output_file> -e <extensions>

   Options:
   
     * -d or --domain: The domain to retrieve archived URLs for (e.g., example.com).
     * -o or --output: File to save the URLs (e.g., output.txt).
     * -e or --extensions: Filter URLs by file extensions (comma-separated list, e.g., js,php,html).

****License and discalimer****

This tool are for educational purposes only, ALL developers and contributors are not responsible for any kind of misuse.
This Project is licensed under GNU General Public License v3.0.
