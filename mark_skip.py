import xml.etree.ElementTree as ET
import re

f="gns3_zh_CN.ts"

tree=ET.parse(f)
root=tree.getroot()

skip_exact={
"HTTP",
"HTTPS",
"VNC",
"SPICE",
"QEMU",
"TCP",
"UDP",
"Raw",
"HDD",
"HDA (Primary Master)",
"HDB (Primary Slave)",
"HDC (Secondary Master)",
"HDD (Secondary Slave)",
"CD/DVD",
"CD/DVD-ROM",
"Qemu VMs",
"Qemu VM templates",
"QEMU",
"spice",
"spice+agent",
}

count=0

for ctx in root.findall("context"):
    for msg in ctx.findall("message"):
        src=msg.findtext("source","")
        tr=msg.find("translation")

        if tr is None:
            continue

        if tr.get("type")!="unfinished":
            continue


        skip=False

        if src in skip_exact:
            skip=True

        if re.fullmatch(r"Ctrl\+.*",src):
            skip=True

        if re.fullmatch(r"\s*(\d+|[\d]+k|[\d]+M|[\d]+MiB)\s*",src):
            skip=True

        if src.strip() in ["%","MiB","ms"]:
            skip=True

        if skip:
            tr.text=src
            tr.attrib.pop("type",None)
            count+=1


tree.write(
    f,
    encoding="utf-8",
    xml_declaration=True
)

print("marked:",count)

