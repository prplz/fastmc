from proto import LOGIN, PLAY, protocol

protocol(47).set_name("1.8")
protocol(47).based_on(5)

############################################### Login
protocol(47).state(LOGIN).from_server(0x01, "EncryptionRequest", """
    server_id       string
    public_key      varint_byte_array
    challenge_token varint_byte_array
""")
protocol(47).state(LOGIN).from_server(0x03, "SetCompression", """
    threshold       varint
""")
# ---------------------------------------------------
protocol(47).state(LOGIN).from_client(0x01, "EncryptionResponse", """
    shared_secret   varint_byte_array
    response_token  varint_byte_array
""")

############################################### Play
protocol(47).state(PLAY).from_server(0x00, "KeepAlive", """
    keepalive_id    varint
""")
protocol(47).state(PLAY).from_server(0x01, "JoinGame", """
    eid             int
    game_mode       ubyte
    dimension       byte
    difficulty      ubyte
    max_players     ubyte
    level_type      string
    reduced_debug   bool
""")
protocol(47).state(PLAY).from_server(0x02, "ChatMesage", """
    chat            json
    position        byte
""")
protocol(47).state(PLAY).from_server(0x04, "EntityEquipment", """
    eid             varint
    slot            short
    item            slot_1_8
""")
protocol(47).state(PLAY).from_server(0x05, "SpawnPosition", """
    location        position_packed
""")
protocol(47).state(PLAY).from_server(0x06, "HealthUpdate", """
    health          float
    food            varint
    food_saturation float
""")
protocol(47).state(PLAY).from_server(0x08, "PlayerPositionAndLook", """
    x               double
    y               double
    z               double
    yaw             float
    pitch           float
    flag            byte
""")
protocol(47).state(PLAY).from_server(0x0a, "UseBed", """
    eid             varint
    location        position_packed
""")
protocol(47).state(PLAY).from_server(0x0c, "SpawnPlayer", """
    eid             varint
    uuid            uuid
    x               int32
    y               int32
    z               int32
    yaw             ubyte
    pitch           ubyte
    current_item    short
    metadata        metadata_1_8
""")
protocol(47).state(PLAY).from_server(0x0d, "CollectItem", """
    collected_eid   varint
    collector_eid   varint
""")
protocol(47).state(PLAY).from_server(0x10, "SpawnPainting", """
    eid             varint
    title           string
    location        position_packed
    direction       ubyte
""")
protocol(47).state(PLAY).from_server(0x12, "EntityVelocity", """
    eid             varint
    velocity_x      short
    velocity_y      short
    velocity_z      short
""")
protocol(47).state(PLAY).from_server(0x13, "DestroyEntities", """
    eids            varint_varint_array
""")
protocol(47).state(PLAY).from_server(0x14, "Entity", """
    eid             varint
""")
protocol(47).state(PLAY).from_server(0x15, "EntityRelativeMove", """
    eid             varint
    dx              byte32
    dy              byte32
    dz              byte32
    on_ground       bool
""")
protocol(47).state(PLAY).from_server(0x16, "EntityLook", """
    eid             varint
    yaw             ubyte
    pitch           ubyte
    on_ground       bool
""")
protocol(47).state(PLAY).from_server(0x17, "EntityLookAndRelativeMove", """
    eid             varint
    dx              byte32
    dy              byte32
    dz              byte32
    yaw             ubyte
    pitch           ubyte
    on_ground       bool
""")
protocol(47).state(PLAY).from_server(0x18, "EntityTeleport", """
    eid             varint
    x               int32
    y               int32
    z               int32
    yaw             ubyte
    pitch           ubyte
    on_ground       bool
""")
protocol(47).state(PLAY).from_server(0x19, "EntityHeadLook", """
    eid             varint
    head_yaw        ubyte
""")
protocol(47).state(PLAY).from_server(0x1c, "EntityMetadata", """
    eid             varint
    metadata        metadata_1_8
""")
protocol(47).state(PLAY).from_server(0x1d, "EntityEffect", """
    eid             varint
    effect_id       byte
    amplifier       byte
    duration        varint
    hide_particles  bool
""")
protocol(47).state(PLAY).from_server(0x1e, "RemoveEntityEffect", """
    eid             varint
    effect_id       byte
""")
protocol(47).state(PLAY).from_server(0x1f, "SetExperience", """
    bar             float
    level           varint
    total_exp       varint
""")
protocol(47).state(PLAY).from_server(0x20, "EntityProperty", """
    eid             varint
    properties      property_array_14w04a
""")
protocol(47).state(PLAY).from_server(0x21, "ChunkData", """
    chunk_x         int
    chunk_z         int
    continuous      bool
    primary_bitmap  ushort
    data            varint_byte_array
""")
protocol(47).state(PLAY).from_server(0x22, "MultiBlockChange", """
    chunk_x         int
    chunk_z         int
    changes         changes_14w26c
""")
protocol(47).state(PLAY).from_server(0x23, "BlockChange", """
    location        position_packed
    block_id        varint
""")
protocol(47).state(PLAY).from_server(0x24, "BlockAction", """
    location        position_packed
    b1              ubyte
    b2              ubyte
    block_type      varint
""")
protocol(47).state(PLAY).from_server(0x25, "BlockBreakAnimation", """
    eid             varint
    location        position_packed
    destroy_stage   byte
""")
protocol(47).state(PLAY).from_server(0x26, "MapChunkBulk", """
    bulk            map_chunk_bulk_14w28a
""")
protocol(47).state(PLAY).from_server(0x28, "Effect", """
    effect_id       int
    location        position_packed
    data            int
    constant_volume bool
""")
protocol(47).state(PLAY).from_server(0x2a, "Particle", """
    particle_id     int
    long_distance   bool
    x               float
    y               float
    z               float
    offset_x        float
    offset_y        float
    offset_z        float
    speed           float
    number          int
    data            bytes_exhaustive    self.particle_id in (36, 37, 38)
""")
protocol(47).state(PLAY).from_server(0x2d, "OpenWindow", """
    window_id       ubyte
    type            string
    title           json
    slot_count      ubyte
    eid             int                 self.type == "EntityHorse"
""")
protocol(47).state(PLAY).from_server(0x2f, "SetSlot", """
    window_id       ubyte
    slot            short
    item            slot_1_8
""")
protocol(47).state(PLAY).from_server(0x30, "WindowItem", """
    window_id       ubyte
    slots           slot_array_1_8
""")
protocol(47).state(PLAY).from_server(0x33, "UpdateSign", """
    location        position_packed
    line1           json
    line2           json
    line3           json
    line4           json
""")
protocol(47).state(PLAY).from_server(0x34, "Maps", """
    map_id          varint
    scale           byte
    icons           map_icons
    columns         ubyte
    rows            ubyte               self.columns > 0
    x               ubyte               self.columns > 0
    y               ubyte               self.columns > 0
    data            varint_byte_array   self.columns > 0
""")
protocol(47).state(PLAY).from_server(0x35, "UpdateBlockEntity", """
    location        position_packed
    action          ubyte
    nbt             nbt
""")
protocol(47).state(PLAY).from_server(0x36, "SignEditorOpen", """
    location        position_packed
""")
protocol(47).state(PLAY).from_server(0x38, "PlayerListItem", """
    list_actions    list_actions
""")
protocol(47).state(PLAY).from_server(0x3b, "ScoreboardObjective", """
    name            string
    mode            byte
    value           string              self.mode == 0 or self.mode == 2
    type            string              self.mode == 0 or self.mode == 2
""")
protocol(47).state(PLAY).from_server(0x3c, "UpdateScore", """
    name            string
    remove          byte
    score_name      string
    value           varint              self.remove != 1
""")
protocol(47).state(PLAY).from_server(0x3e, "Teams", """
    team_name           string
    mode                byte
    display_name        string              self.mode in (0, 2)
    prefix              string              self.mode in (0, 2)
    suffix              string              self.mode in (0, 2)
    friendly_fire       byte                self.mode in (0, 2)
    named_tag_visible   string              self.mode in (0, 2)
    color               byte                self.mode in (0, 2)
    players             varint_string_array self.mode in (0, 3, 4)
""")
protocol(47).state(PLAY).from_server(0x3f, "PluginMessage", """
    channel         string
    data            bytes_exhaustive
""")
protocol(47).state(PLAY).from_server(0x41, "ServerDifficulty", """
    difficulty      ubyte
""")
protocol(47).state(PLAY).from_server(0x42, "CombatEvent", """
    event           ubyte
    duration        varint              self.event == 1
    end_eid         int                 self.event == 1
    player_id       varint              self.event == 2
    dead_eid        int                 self.event == 2
    message         string              self.event == 2
""")
protocol(47).state(PLAY).from_server(0x43, "Camera", """
    camera_id       varint
""")
protocol(47).state(PLAY).from_server(0x44, "WorldBorder", """
    action          varint
    x               double              self.action in (2, 3)
    z               double              self.action in (2, 3)
    old_radius      double              self.action in (1, 3)
    new_radius      double              self.action in (0, 1, 3)
    speed           varint              self.action in (1, 3)
    boundary        varint              self.action == 3
    warning_time    varint              self.action in (3, 4)
    warning_blocks  varint              self.action in (3, 5)
""")
protocol(47).state(PLAY).from_server(0x45, "Title", """
    action          varint
    text            json                self.action in (0, 1)
    fade_in         int                 self.action == 2
    stay            int                 self.action == 2
    fade_out        int                 self.action == 2
""")
protocol(47).state(PLAY).from_server(0x46, "SetCompression", """
    threshold       varint
""")
protocol(47).state(PLAY).from_server(0x47, "PlayerListHeaderFooter", """
    header          json
    footer          json
""")
protocol(47).state(PLAY).from_server(0x48, "ResourcePackSend", """
    url             string
    hash            string
""")
protocol(47).state(PLAY).from_server(0x49, "UpdateEntityNBT", """
    eid             varint
    nbt             short_byte_array
""")
# ---------------------------------------------------
protocol(47).state(PLAY).from_client(0x00, "KeepAlive", """
    keepalive_id    varint
""")
protocol(47).state(PLAY).from_client(0x02, "UseEntity", """
    target          varint
    type            varint
    target_x        float               self.type == 2
    target_y        float               self.type == 2
    target_z        float               self.type == 2
""")
protocol(47).state(PLAY).from_client(0x04, "PlayerPosition", """
    x               double
    y               double
    z               double
    on_ground       bool
""")
protocol(47).state(PLAY).from_client(0x06, "PlayerPositionAndLook", """
    x               double
    y               double
    z               double
    yaw             float
    pitch           float
    on_ground       bool
""")
protocol(47).state(PLAY).from_client(0x07, "PlayerDigging", """
    status          byte
    location        position_packed
    face            byte
""")
protocol(47).state(PLAY).from_client(0x08, "BlockPlacement", """
    location        position_packed
    direction       byte
    held_item       slot_1_8
    cursor_x        byte
    cursor_y        byte
    cursor_z        byte
""")
protocol(47).state(PLAY).from_client(0x0a, "Animation")
protocol(47).state(PLAY).from_client(0x0b, "EntityAction", """
    eid             varint
    action_id       ubyte
    jump_boost      varint
""")
protocol(47).state(PLAY).from_client(0x0c, "SteerVehicle", """
    sideways        float
    forward         float
    flags           ubyte
""")
protocol(47).state(PLAY).from_client(0x0e, "ClickWindow", """
    window_id       ubyte
    slot            short
    button          byte
    action_num      short
    mode            byte
    clicked_item    slot_1_8
""")
protocol(47).state(PLAY).from_client(0x10, "CreativeInventoryAction", """
    slot            short
    clicked_item    slot_1_8
""")
protocol(47).state(PLAY).from_client(0x12, "UpdateSign", """
    location        position_packed
    line1           json
    line2           json
    line3           json
    line4           json
""")
protocol(47).state(PLAY).from_client(0x14, "TabComplete", """
    text            string
    has_position    bool
    location        position_packed     self.has_position
""")
protocol(47).state(PLAY).from_client(0x15, "ClientSettings", """
    locale          string
    view_distance   byte
    chat_flags      byte
    chat_colors     bool
    displayed_skin  ubyte
""")
protocol(47).state(PLAY).from_client(0x16, "ClientStatus", """
    action_id       ubyte
""")
protocol(47).state(PLAY).from_client(0x17, "PluginMessage", """
    channel         string
    data            varint_byte_array
""")
protocol(47).state(PLAY).from_client(0x18, "Spectate", """
    target_player   string
""")
protocol(47).state(PLAY).from_client(0x19, "ResourcePackStatus", """
    hash            string
    result          varint
""")
