import xml.etree.ElementTree as ET

tree = ET.parse('results.xml')
root = tree.getroot()

total = int(root.attrib.get('tests', 0))
failures = int(root.attrib.get('failures', 0))
errors = int(root.attrib.get('errors', 0))
skipped = int(root.attrib.get('skipped', 0))

passed = total - failures - errors - skipped

print(f"TOTAL={total}")
print(f"PASSED={passed}")
print(f"FAILED={failures}")
print(f"ERRORS={errors}")
print(f"SKIPPED={skipped}")