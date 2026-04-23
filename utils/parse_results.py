import os
import xml.etree.ElementTree as ET

base_dir = os.path.dirname(os.path.dirname(__file__))  # go up from tests/
xml_path = os.path.join(base_dir, 'results.xml')

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