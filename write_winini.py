import socket
from data import servers
from data import sd_presets
from data import hd_presets
from data import winini_template

sd1=""
hd1=""
3d=""

# ##############################
# SD
# ##############################

i=0

sd1 += sd_presets.format(
    name='Localhost',
    decoder_ip='127.0.0.1',
    decoder_ip2='224.1.1.2',
    preset_id=i
)

for server in servers:
    i += 1
    ip = socket.gethostbyname(server)
    # print "%s: %s" %(server, s)
    sd1 += sd_presets.format(
        name=server,
        decoder_ip=ip,
        decoder_ip2='224.1.1.2',
        preset_id=i
    )

# ##############################
# HD
# ##############################

i=0

hd1 += hd_presets.format(
    name='Localhost',
    decoder_ip='127.0.0.1',
    decoder_ip2='224.1.1.2',
    preset_id=i
)

for server in servers:
    i += 1
    ip = socket.gethostbyname(server)
    # print "%s: %s" %(server, s)
    hd1 += hd_presets.format(
        name=server,
        decoder_ip=ip,
        decoder_ip2='224.1.1.2',
        preset_id=i
    )

# ##############################
# 3D
# ##############################

i=0

3d += 3d_presets.format(
    name='Localhost',
    decoder_ip='127.0.0.1',
    decoder_ip2='224.1.1.2',
    preset_id=i
)

for server in servers:
    i += 1
    ip = socket.gethostbyname(server)
    # print "%s: %s" %(server, s)
    hd1 += hd_presets.format(
        name=server,
        decoder_ip=ip,
        decoder_ip2='224.1.1.2',
        preset_id=i
    )

print winini_template.format(
    3D_PRESETS_STRING=3d,
    HD_PRESETS_STRING=hd1,
    SD_PRESETS_STRING=sd1
)
