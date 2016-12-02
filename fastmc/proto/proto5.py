from proto import PLAY, protocol

protocol(5).set_name("1.7.6")
protocol(5).based_on(4)
protocol(5).state(PLAY).from_server(0x0c, "SpawnPlayer", """
    eid             varint
    uuid            string
    name            string
    data            varint_player_data_array
    x               int32
    y               int32
    z               int32
    yaw             ubyte
    pitch           ubyte
    current_item    short
    metadata        metadata
""")
