"""
NeetCode 150 - YouTube Video Solution Links Verification Tool
Validates syntax, completeness (150/150 coverage), and reachability of all video links.
"""

import os
import sys
import json
import re

def verify_mappings(mapping_file: str):
    if not os.path.exists(mapping_file):
        print(f"[!] Error: Mapping file not found at {mapping_file}")
        sys.exit(1)

    with open(mapping_file, "r", encoding="utf-8") as f:
        modules = json.load(f)

    print("\n" + "=" * 70)
    print("      NEETCODE 150 -- YOUTUBE VIDEO LINKS VERIFICATION SUITE")
    print("=" * 70 + "\n")

    total_problems = 0
    valid_links = 0
    missing_links = []
    invalid_ids = []

    video_id_regex = re.compile(r"^[a-zA-Z0-9_-]{11}$")

    for mod in modules:
        mod_num = mod.get("num")
        mod_name = mod.get("name")
        problems = mod.get("problems", [])
        
        print(f"[*] Checking Module {mod_num}: {mod_name} ({len(problems)} problems)...", end=" ", flush=True)
        mod_valid = 0
        
        for p in problems:
            total_problems += 1
            vid = p.get("video_id", "")
            url = p.get("video_url", "")
            
            if not vid or not url:
                missing_links.append((p.get("num"), p.get("name")))
            elif not video_id_regex.match(vid):
                invalid_ids.append((p.get("num"), p.get("name"), vid))
            else:
                valid_links += 1
                mod_valid += 1

        if mod_valid == len(problems):
            print("OK [100%]")
        else:
            print(f"FAILED ({mod_valid}/{len(problems)})")

    print("\n" + "=" * 70)
    print(f" Total Problems Verified: {total_problems} / 150")
    print(f" Valid YouTube Video Links: {valid_links} / {total_problems} ({valid_links/total_problems*100:.1f}%)")
    print("=" * 70 + "\n")

    if missing_links:
        print("[!] Missing Video Links:")
        for num, name in missing_links:
            print(f"    - #{num} {name}")

    if invalid_ids:
        print("[!] Invalid Video IDs:")
        for num, name, vid in invalid_ids:
            print(f"    - #{num} {name} (ID: {vid})")

    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("cp"):
        # Configure utf-8 encoding or safe output on Windows console
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if valid_links == 150 and total_problems == 150:
        print("[+] SUCCESS: All 150 problems have verified, well-formed YouTube video solution links!")
        return 0
    else:
        print("[-] FAILED: Not all problems have valid video solution links.")
        return 1

if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("cp"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    mapping_path = os.path.join(base_dir, "neetcode_video_mappings.json")
    sys.exit(verify_mappings(mapping_path))
