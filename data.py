servers_string = r'''
t1
t2
t3
t5
LiveAU
# LiveDB
LiveDE
LiveEU
LiveHK
LiveHK2
LiveIN
LiveJP
LiveSA
LiveSG
LiveUS
LiveUSEast
'''
servers=[s.strip() for s in servers_string.splitlines() if (s.strip() != "" and not s.startswith('#'))]

hd_presets=r'''
_Preset_{preset_id}_Present=2
_Preset_{preset_id}_Name={name}
_Preset_{preset_id}__Network=0
_Preset_{preset_id}__E1=0
_Preset_{preset_id}__Telco=0
_Preset_{preset_id}__LINE_BUILD_OUT=0
_Preset_{preset_id}__Multiplex=2
_Preset_{preset_id}__udp_port=1770
_Preset_{preset_id}__IP_PackSize=1392
_Preset_{preset_id}__TTL=175
_Preset_{preset_id}__Enable IP Monitor=0
_Preset_{preset_id}__DecoderIP={decoder_ip}
_Preset_{preset_id}__DecoderIP2={decoder_ip2}
_Preset_{preset_id}__MonitorIP=192.168.1.23
_Preset_{preset_id}__FEC=0
_Preset_{preset_id}__ShuffleMaxIndex=0
_Preset_{preset_id}__UseMPUDP=0
_Preset_{preset_id}__ManualLDMP=0
_Preset_{preset_id}__MPUDP_CWND=200
_Preset_{preset_id}__MPUDP_CWND_MIN=5
_Preset_{preset_id}__MPUDP_CWND_MAX=75
_Preset_{preset_id}__MPUDP_ACK_TO=1000
_Preset_{preset_id}__MPUDP_SND_TO=2000
_Preset_{preset_id}__JITTER_RTT_X=2
_Preset_{preset_id}__JITTER2_PERCENT=10
'''

sd_presets=r'''
_Preset_{preset_id}_Present=2
_Preset_{preset_id}_Name={name}
_Preset_{preset_id}__Network=0
_Preset_{preset_id}__E1=0
_Preset_{preset_id}__Telco=0
_Preset_{preset_id}__LINE_BUILD_OUT=0
_Preset_{preset_id}__Multiplex=2
_Preset_{preset_id}__udp_port=1770
_Preset_{preset_id}__IP_PackSize=1392
_Preset_{preset_id}__TTL=175
_Preset_{preset_id}__Enable IP Monitor=0
_Preset_{preset_id}__DecoderIP={decoder_ip}
_Preset_{preset_id}__DecoderIP2={decoder_ip2}
_Preset_{preset_id}__MonitorIP=192.168.1.23
_Preset_{preset_id}__FEC=0
_Preset_{preset_id}__ShuffleMaxIndex=0
_Preset_{preset_id}__UseMPUDP=0
_Preset_{preset_id}__ManualLDMP=0
_Preset_{preset_id}__MPUDP_CWND=200
_Preset_{preset_id}__MPUDP_CWND_MIN=5
_Preset_{preset_id}__MPUDP_CWND_MAX=75
_Preset_{preset_id}__MPUDP_ACK_TO=1000
_Preset_{preset_id}__MPUDP_SND_TO=2000
_Preset_{preset_id}__JITTER_RTT_X=2
_Preset_{preset_id}__JITTER2_PERCENT=10
'''

winini_template=r'''
[annie]
SDSignal=0
UseMPUDP=0
Meta_GPS_X=
Meta_GPS_Y=
PHPENCODER=1802
UseABN=0
bypas_color=0
CaptureFile=
VideoDevice2=
AudioDevice2=
FrameRate=667111
UseFrameRate=1
CaptureAudio=1
CaptureCC=0
Video input=0
WantPreview=0
MasterStream=1
UseTimeLimit=0
TimeLimit=0
Network=0
Enable IP Monitor=0
audio_input=3
PresetCurrentName=custom
video_source=2

{SD_PRESETS_STRING}

[SB_HD_ENCODER]
SDSignal=0
UseMPUDP=0
Meta_GPS_X=
Meta_GPS_Y=
PHPENCODER=1802
UseABN=0
bypas_color=0
CaptureFile=
VideoDevice2=
AudioDevice2=
FrameRate=667111
UseFrameRate=1
CaptureAudio=1
CaptureCC=0
Video input=0
WantPreview=0
MasterStream=1
UseTimeLimit=0
TimeLimit=0
Network=0
Enable IP Monitor=0
isHDTV=0
video_standard=0
video_standard_hdtv=0
Enable2Slice=0
audio_input=3
PresetCurrentName=custom
TargetBitrate=4096
video_source=2
Meta_Slug=mtmc-slug
Meta_Location=mtmc-location
Meta_Connectivity=mtmc-connectivity
Meta_Reporter=mtmc
Meta_Producer=mtmc-producer
Meta_Network1=mtmc-network-group1
Meta_Network2=mtmc-network-group1
Meta_Network3=mtmc-network-group1
TransmitMetadata=1
TransmitMetadataGPS=0
DecoderIP=127.0.0.1
DecoderIP2=10.0.2.125
udp_port=1770
TTL=175
IP_PackSize=1392
Name=Localhost
Present=2

{HD_PRESETS_STRING}
'''
