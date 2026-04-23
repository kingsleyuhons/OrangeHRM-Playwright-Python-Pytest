import os
import xml.etree.ElementTree as ET

xml_path = os.path.join(os.getcwd(), 'results.xml')

if not os.path.exists(xml_path):
    print("TOTAL=0")
    print("PASSED=0")
    print("FAILED=0")
    print("SKIPPED=0")
    exit(0)

tree = ET.parse(xml_path)
root = tree.getroot()

total = int(root.attrib.get('tests', 0))
failures = int(root.attrib.get('failures', 0))
errors = int(root.attrib.get('errors', 0))
skipped = int(root.attrib.get('skipped', 0))
passed = total - failures - errors - skipped

print(f"TOTAL={total}")
print(f"PASSED={passed}")
print(f"FAILED={failures + errors}")
print(f"SKIPPED={skipped}")