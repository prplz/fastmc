from proto import HANDSHAKE, LOGIN, PLAY, STATUS, protocol

protocol(0).set_name("13w42a")

############################################### Handshake
protocol(0).state(HANDSHAKE).from_client(0x00, "Handshake", """
    version         varint
    addr            string
    port            ushort
    state           varint
""")

############################################### Status
protocol(0).state(STATUS).from_server(0x00, "Response", """
    response        json
""")
protocol(0).state(STATUS).from_server(0x01, "Ping", """
    time            long
""")
# ---------------------------------------------------
protocol(0).state(STATUS).from_client(0x00, "Request")
protocol(0).state(STATUS).from_client(0x01, "Ping", """
    time            long
""")

############################################### Login
protocol(0).state(LOGIN).from_server(0x00, "Disconnect", """
    reason          json
""")
protocol(0).state(LOGIN).from_server(0x01, "EncryptionRequest", """
    server_id       string
    public_key      short_byte_array
    challenge_token short_byte_array
""")
protocol(0).state(LOGIN).from_server(0x02, "LoginSuccess", """
    uuid            string
    username        string
""")
# ---------------------------------------------------
protocol(0).state(LOGIN).from_client(0x00, "LoginStart", """
    name            string
""")
protocol(0).state(LOGIN).from_client(0x01, "EncryptionResponse", """
    shared_secret   short_byte_array
    response_token  short_byte_array
""")

############################################### Play
protocol(0).state(PLAY).from_server(0x00, "KeepAlive", """
    keepalive_id    int
""")
protocol(0).state(PLAY).from_server(0x01, "JoinGame", """
    eid             int
    game_mode       ubyte
    dimension       byte
    difficulty      ubyte
    max_players     ubyte
    level_type      string
""")
protocol(0).state(PLAY).from_server(0x02, "ChatMessage", """
    chat            json
""")
protocol(0).state(PLAY).from_server(0x03, "TimeUpdate", """
    world_age       long
    time_of_day     long
""")
protocol(0).state(PLAY).from_server(0x04, "EntityEquipment", """
    eid             int
    slot            short
    item            slot
""")
protocol(0).state(PLAY).from_server(0x05, "SpawnPosition", """
    x               int
    y               int
    z               int
""")
protocol(0).state(PLAY).from_server(0x06, "HealthUpdate", """
    health          float
    food            short
    food_saturation float
""")
protocol(0).state(PLAY).from_server(0x07, "Respawn", """
    dimension       int
    difficulty      ubyte
    game_mode       ubyte
    level_type      string
""")
protocol(0).state(PLAY).from_server(0x08, "PlayerPositionAndLook", """
    x               double
    y               double
    z               double
    yaw             float
    pitch           float
    on_ground       bool
""")
protocol(0).state(PLAY).from_server(0x09, "HeldItemChange", """
    slot            byte
""")
protocol(0).state(PLAY).from_server(0x0a, "UseBed", """
    eid             int
    x               int
    y               byte
    z               int
""")
protocol(0).state(PLAY).from_server(0x0b, "Animation", """
    eid             varint
    animation       ubyte
""")
protocol(0).state(PLAY).from_server(0x0c, "SpawnPlayer", """
    eid             varint
    uuid            string
    name            string
    x               int32
    y               int32
    z               int32
    yaw             ubyte
    pitch           ubyte
    current_item    short
    metadata        metadata
""")
protocol(0).state(PLAY).from_server(0x0d, "CollectItem", """
    collected_eid   int
    collector_eid   int
""")
protocol(0).state(PLAY).from_server(0x0e, "SpawnObject", """
    eid             varint
    type            byte
    x               int32
    y               int32
    z               int32
    pitch           ubyte
    yaw             ubyte
    data            objdata
""")
protocol(0).state(PLAY).from_server(0x0f, "SpawnMob", """
    eid             varint
    type            ubyte
    x               int32
    y               int32
    z               int32
    pitch           ubyte
    head_pitch      ubyte
    yaw             ubyte
    velocity_x      short
    velocity_y      short
    velocity_z      short
    metadata        metadata
""")
protocol(0).state(PLAY).from_server(0x10, "SpawnPainting", """
    eid             varint
    title           string
    x               int
    y               int
    z               int
    direction       int
""")
protocol(0).state(PLAY).from_server(0x11, "SpawnExperienceOrb", """
    eid             varint
    x               int32
    y               int32
    z               int32
    count           short
""")
protocol(0).state(PLAY).from_server(0x12, "EntityVelocity", """
    eid             int
    velocity_x      short
    velocity_y      short
    velocity_z      short
""")
protocol(0).state(PLAY).from_server(0x13, "DestroyEntities", """
    eids            byte_int_array
""")
protocol(0).state(PLAY).from_server(0x14, "Entity", """
    eid             int
""")
protocol(0).state(PLAY).from_server(0x15, "EntityRelativeMove", """
    eid             int
    dx              byte32
    dy              byte32
    dz              byte32
""")
protocol(0).state(PLAY).from_server(0x16, "EntityLook", """
    eid             int
    yaw             ubyte
    pitch           ubyte
""")
protocol(0).state(PLAY).from_server(0x17, "EntityLookAndRelativeMove", """
    eid             int
    dx              byte32
    dy              byte32
    dz              byte32
    yaw             ubyte
    pitch           ubyte
""")
protocol(0).state(PLAY).from_server(0x18, "EntityTeleport", """
    eid             int
    x               int32
    y               int32
    z               int32
    yaw             ubyte
    pitch           ubyte
""")
protocol(0).state(PLAY).from_server(0x19, "EntityHeadLook", """
    eid             int
    head_yaw        ubyte
""")
protocol(0).state(PLAY).from_server(0x1a, "EntityStatus", """
    eid             int
    status          byte
""")
protocol(0).state(PLAY).from_server(0x1b, "AttachEntity", """
    eid             int
    vehicle_id      int
    leash           bool
""")
protocol(0).state(PLAY).from_server(0x1c, "EntityMetadata", """
    eid             int
    metadata        metadata
""")
protocol(0).state(PLAY).from_server(0x1d, "EntityEffect", """
    eid             int
    effect_id       byte
    amplifier       byte
    duration        short
""")
protocol(0).state(PLAY).from_server(0x1e, "RemoveEntityEffect", """
    eid             int
    effect_id       byte
""")
protocol(0).state(PLAY).from_server(0x1f, "SetExperience", """
    bar             float
    level           short
    total_exp       short
""")
protocol(0).state(PLAY).from_server(0x20, "EntityProperty", """
    eid             int
    properties      property_array
""")
protocol(0).state(PLAY).from_server(0x21, "ChunkData", """
    chunk_x         int
    chunk_z         int
    continuous      bool
    chunk_bitmap    ushort
    add_bitmap      ushort
    compressed      int_byte_array
""")
protocol(0).state(PLAY).from_server(0x22, "MultiBlockChange", """
    chunk_x         varint
    chunk_z         varint
    changes         changes
""")
protocol(0).state(PLAY).from_server(0x23, "BlockChange", """
    x               int
    y               ubyte
    z               int
    block_type      varint
    block_data      ubyte
""")
protocol(0).state(PLAY).from_server(0x24, "BlockAction", """
    x               int
    y               short
    z               int
    b1              ubyte
    b2              ubyte
    block_type      varint
""")
protocol(0).state(PLAY).from_server(0x25, "BlockBreakAnimation", """
    eid             varint
    x               int
    y               int
    z               int
    destroy_stage   byte
""")
protocol(0).state(PLAY).from_server(0x26, "MapChunkBulk", """
    bulk            map_chunk_bulk
""")
protocol(0).state(PLAY).from_server(0x27, "Explosion", """
    x               float
    y               float
    z               float
    radius          float
    records         explosions
    motion_x        float
    motion_y        float
    motion_z        float
""")
protocol(0).state(PLAY).from_server(0x28, "Effect", """
    effect_id       int
    x               int
    y               byte
    z               int
    data            int
    constant_volume bool
""")
protocol(0).state(PLAY).from_server(0x29, "SoundEffect", """
    sound           string
    x               int8
    y               int8
    z               int8
    volume          float
    pitch           ubyte
""")
protocol(0).state(PLAY).from_server(0x2a, "Particle", """
    particle        string
    x               float
    y               float
    z               float
    offset_x        float
    offset_y        float
    offset_z        float
    speed           float
    number          int
""")
protocol(0).state(PLAY).from_server(0x2b, "ChangeGameState", """
    reason          ubyte
    value           float
""")
protocol(0).state(PLAY).from_server(0x2c, "SpawnGlobalEntity", """
    eid             varint
    type            byte
    x               int32
    y               int32
    z               int32
""")
protocol(0).state(PLAY).from_server(0x2d, "OpenWindow", """
    window_id       ubyte
    type            ubyte
    title           string
    slot_count      ubyte
    use_title       bool
    eid             int                 self.type == 11
""")
protocol(0).state(PLAY).from_server(0x2e, "CloseWindow", """
    window_id       ubyte
""")
protocol(0).state(PLAY).from_server(0x2f, "SetSlot", """
    window_id       ubyte
    slot            short
    item            slot
""")
protocol(0).state(PLAY).from_server(0x30, "WindowItems", """
    window_id       ubyte
    slots           slot_array
""")
protocol(0).state(PLAY).from_server(0x31, "WindowProperty", """
    window_id       ubyte
    property        short
    value           short
""")
protocol(0).state(PLAY).from_server(0x32, "ConfirmTransaction", """
    window_id       ubyte
    action_num      short
    accepted        bool
""")
protocol(0).state(PLAY).from_server(0x33, "UpdateSign", """
    x               int
    y               short
    z               int
    line1           string
    line2           string
    line3           string
    line4           string
""")
protocol(0).state(PLAY).from_server(0x34, "Map", """
    map_id          varint
    data            short_byte_array
""")
protocol(0).state(PLAY).from_server(0x35, "UpdateBlockEntity", """
    x               int
    y               short
    z               int
    action          ubyte
    nbt             short_byte_array
""")
protocol(0).state(PLAY).from_server(0x36, "SignEditorOpen", """
    x               int
    y               int
    z               int
""")
protocol(0).state(PLAY).from_server(0x37, "Statistics", """
    stats           statistic_array
""")
protocol(0).state(PLAY).from_server(0x38, "PlayerListItem", """
    name            string
    online          bool
    ping            short
""")
protocol(0).state(PLAY).from_server(0x39, "PlayerAbilities", """
    flags           byte
    flying_speed    float
    walking_speed   float
""")
protocol(0).state(PLAY).from_server(0x3a, "TabComplete", """
    completions     varint_string_array
""")
protocol(0).state(PLAY).from_server(0x3b, "ScoreboardObjective", """
    name            string
    value           string
    operation       byte
""")
protocol(0).state(PLAY).from_server(0x3c, "UpdateScore", """
    name            string
    remove          byte
    score_name      string              self.remove != 1
    value           int                 self.remove != 1
""")
protocol(0).state(PLAY).from_server(0x3d, "DisplayScoreboard", """
    position        byte
    score_name      string
""")
protocol(0).state(PLAY).from_server(0x3e, "Teams", """
    team_name       string
    mode            byte
    display_name    string              self.mode == 0 or self.mode == 2
    prefix          string              self.mode == 0 or self.mode == 2
    suffix          string              self.mode == 0 or self.mode == 2
    friendly_fire   byte                self.mode == 0 or self.mode == 2
    players         short_string_array  self.mode in (0, 3, 4)
""")
protocol(0).state(PLAY).from_server(0x3f, "PluginMessage", """
    channel         string
    data            short_byte_array
""")
protocol(0).state(PLAY).from_server(0x40, "Disconnect", """
    reason          json
""")
# ---------------------------------------------------
protocol(0).state(PLAY).from_client(0x00, "KeepAlive", """
    keepalive_id    int
""")
protocol(0).state(PLAY).from_client(0x01, "ChatMessage", """
    chat            string
""")
protocol(0).state(PLAY).from_client(0x02, "UseEntity", """
    target          int
    button          byte
""")
protocol(0).state(PLAY).from_client(0x03, "Player", """
    on_ground       bool
""")
protocol(0).state(PLAY).from_client(0x04, "PlayerPosition", """
    x               double
    y               double
    stance          double
    z               double
    on_ground       bool
""")
protocol(0).state(PLAY).from_client(0x05, "PlayerLook", """
    yaw             float
    pitch           float
    on_ground       bool
""")
protocol(0).state(PLAY).from_client(0x06, "PlayerPositionAndLook", """
    x               double
    y               double
    stance          double
    z               double
    yaw             float
    pitch           float
    on_ground       bool
""")
protocol(0).state(PLAY).from_client(0x07, "PlayerDigging", """
    status          byte
    x               int
    y               ubyte
    z               int
    face            byte
""")
protocol(0).state(PLAY).from_client(0x08, "BlockPlacement", """
    x               int
    y               ubyte
    z               int
    direction       byte
    held_item       slot
    cursor_x        byte
    cursor_y        byte
    cursor_z        byte
""")
protocol(0).state(PLAY).from_client(0x09, "HeldItemChange", """
    slot            short
""")
protocol(0).state(PLAY).from_client(0x0a, "Animation", """
    eid             int
    animation       ubyte
""")
protocol(0).state(PLAY).from_client(0x0b, "EntityAction", """
    eid             int
    action_id       byte
    jump_boost      int
""")
protocol(0).state(PLAY).from_client(0x0c, "SteerVehicle", """
    sideways        float
    forward         float
    jump            bool
    unmount         bool
""")
protocol(0).state(PLAY).from_client(0x0d, "CloseWindow", """
    window_id       ubyte
""")
protocol(0).state(PLAY).from_client(0x0e, "ClickWindow", """
    window_id       ubyte
    slot            short
    button          byte
    action_num      short
    mode            byte
    clicked_item    slot
""")
protocol(0).state(PLAY).from_client(0x0f, "ConfirmTransaction", """
    window_id       ubyte
    action_num      short
    accepted        bool
""")
protocol(0).state(PLAY).from_client(0x10, "CreativeInventoryAction", """
    slot            short
    clicked_item    slot
""")
protocol(0).state(PLAY).from_client(0x11, "EnchantItem", """
    window_id       ubyte
    enchantment     byte
""")
protocol(0).state(PLAY).from_client(0x12, "UpdateSign", """
    x               int
    y               short
    z               int
    line1           string
    line2           string
    line3           string
    line4           string
""")
protocol(0).state(PLAY).from_client(0x13, "PlayerAbilities", """
    flags           byte
    flying_speed    float
    walking_speed   float
""")
protocol(0).state(PLAY).from_client(0x14, "TabComplete", """
    text            string
""")
protocol(0).state(PLAY).from_client(0x15, "ClientSettings", """
    locale          string
    view_distance   byte
    chat_flags      byte
    chat_colors     bool
    difficulty      byte
    show_cape       bool
""")
protocol(0).state(PLAY).from_client(0x16, "ClientStatus", """
    action_id       byte
""")
protocol(0).state(PLAY).from_client(0x17, "PluginMessage", """
    channel         string
    data            short_byte_array
""")

protocol(1).set_name("13w42b")
protocol(1).based_on(0)

protocol(2).set_name("13w43a")
protocol(2).based_on(1)

protocol(3).set_name("1.7.1")
protocol(3).based_on(2)
