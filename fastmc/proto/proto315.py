from proto import PLAY, protocol

protocol(315).set_name("1.11")
protocol(315).based_on(210)

protocol(315).state(PLAY).from_server(0x03, "SpawnMob", """
    eid             varint
    uuid            uuid
    type            varint
    x               double
    y               double
    z               double
    pitch           ubyte
    head_pitch      ubyte
    yaw             ubyte
    velocity_x      short
    velocity_y      short
    velocity_z      short
    metadata        metadata_1_9
""")
protocol(315).state(PLAY).from_server(0x48, "CollectItem", """
    collected_eid   varint
    collector_eid   varint
    item_count      varint
""")

protocol(315).state(PLAY).from_client(0x1c, "BlockPlacement", """
    location        position_packed
    direction       varint
    hand            varint
    cursor_x        float
    cursor_y        float
    cursor_z        float
""")
