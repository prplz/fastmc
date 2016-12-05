from proto import CLIENTBOUND, HANDSHAKE, LOGIN, PLAY, SERVERBOUND, STATUS, protocol

protocol(210).set_name("1.10")

for pkt in protocol(109).get_packets(HANDSHAKE, SERVERBOUND).values():
    protocol(210).add_packet(HANDSHAKE, SERVERBOUND, pkt)

for pkt in protocol(109).get_packets(STATUS, CLIENTBOUND).values():
    protocol(210).add_packet(STATUS, CLIENTBOUND, pkt)

for pkt in protocol(109).get_packets(STATUS, SERVERBOUND).values():
    protocol(210).add_packet(STATUS, SERVERBOUND, pkt)

for pkt in protocol(109).get_packets(LOGIN, CLIENTBOUND).values():
    protocol(210).add_packet(LOGIN, CLIENTBOUND, pkt)

for pkt in protocol(109).get_packets(LOGIN, SERVERBOUND).values():
    protocol(210).add_packet(LOGIN, SERVERBOUND, pkt)

for i in xrange(0x46):
    protocol(210).add_packet(PLAY, CLIENTBOUND, protocol(109).get_packets(PLAY, CLIENTBOUND)[i])

for i in xrange(0x47, 0x4d):
    pkt = protocol(109).get_packets(PLAY, CLIENTBOUND)[i]
    protocol(210).state(PLAY).from_server(i - 1, pkt.__name__, pkt.src)

for pkt in protocol(109).get_packets(PLAY, SERVERBOUND).values():
    protocol(210).add_packet(PLAY, SERVERBOUND, pkt)


protocol(210).state(PLAY).from_server(0x19, "NamedSoundEffect", """
    sound           string
    category        varint
    x               int8
    y               int8
    z               int8
    volume          float
    pitch           float
""")
protocol(210).state(PLAY).from_server(0x47, "SoundEffect", """
    sound           varint
    category        varint
    x               int8
    y               int8
    z               int8
    volume          float
    pitch           float
""")

protocol(47).state(PLAY).from_client(0x16, "ResourcePackStatus", """
    result          varint
""")
