from proto import CLIENTBOUND, HANDSHAKE, LOGIN, PLAY, SERVERBOUND, STATUS, protocol

protocol(107).set_name("1.9")

for pkt in protocol(47).get_packets(HANDSHAKE, SERVERBOUND).values():
    protocol(107).add_packet(HANDSHAKE, SERVERBOUND, pkt)

for pkt in protocol(47).get_packets(STATUS, CLIENTBOUND).values():
    protocol(107).add_packet(STATUS, CLIENTBOUND, pkt)

for pkt in protocol(47).get_packets(STATUS, SERVERBOUND).values():
    protocol(107).add_packet(STATUS, SERVERBOUND, pkt)

for pkt in protocol(47).get_packets(LOGIN, CLIENTBOUND).values():
    protocol(107).add_packet(LOGIN, CLIENTBOUND, pkt)

for pkt in protocol(47).get_packets(LOGIN, SERVERBOUND).values():
    protocol(107).add_packet(LOGIN, SERVERBOUND, pkt)

protocol(107).state(PLAY).from_server(0x00, "SpawnObject", """
    eid             varint
    uuid            uuid
    type            byte
    x               double
    y               double
    z               double
    pitch           ubyte
    yaw             ubyte
    data            int
    velocity_x      short
    velocity_y      short
    velocity_z      short
""")
protocol(107).state(PLAY).from_server(0x01, "SpawnExperienceOrb", """
    eid             varint
    x               double
    y               double
    z               double
    count           short
""")
protocol(107).state(PLAY).from_server(0x02, "SpawnGlobalEntity", """
    eid             varint
    type            byte
    x               double
    y               double
    z               double
""")
protocol(107).state(PLAY).from_server(0x03, "SpawnMob", """
    eid             varint
    uuid            uuid
    type            ubyte
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
protocol(107).state(PLAY).from_server(0x04, "SpawnPainting", protocol(47).PlayClientboundSpawnPainting.src)
protocol(107).state(PLAY).from_server(0x05, "SpawnPlayer", """
    eid             varint
    uuid            uuid
    x               double
    y               double
    z               double
    yaw             ubyte
    pitch           ubyte
    metadata        metadata_1_9
""")
protocol(107).state(PLAY).from_server(0x06, "Animation", protocol(47).PlayClientboundAnimation.src)
protocol(107).state(PLAY).from_server(0x07, "Statistics", protocol(47).PlayClientboundStatistics.src)
protocol(107).state(PLAY).from_server(0x08, "BlockBreakAnimation", protocol(47).PlayClientboundBlockBreakAnimation.src)
protocol(107).state(PLAY).from_server(0x09, "UpdateBlockEntity", protocol(47).PlayClientboundUpdateBlockEntity.src)
protocol(107).state(PLAY).from_server(0x0a, "BlockAction", protocol(47).PlayClientboundBlockAction.src)
protocol(107).state(PLAY).from_server(0x0b, "BlockChange", protocol(47).PlayClientboundBlockChange.src)
protocol(107).state(PLAY).from_server(0x0c, "BossBar", """
    uuid            uuid
    action          varint
    title           json                self.action == 0 or self.action == 3
    health          float               self.action == 0 or self.action == 2
    color           varint              self.action == 0 or self.action == 4
    dividers        varint              self.action == 0 or self.action == 4
    flags           ubyte               self.action == 0 or self.action == 5
""")
protocol(107).state(PLAY).from_server(0x0d, "ServerDifficulty", protocol(47).PlayClientboundServerDifficulty.src)
protocol(107).state(PLAY).from_server(0x0e, "TabComplete", protocol(47).PlayClientboundTabComplete.src)
protocol(107).state(PLAY).from_server(0x0f, "ChatMessage", protocol(47).PlayClientboundChatMessage.src)
protocol(107).state(PLAY).from_server(0x10, "MultiBlockChange", protocol(47).PlayClientboundMultiBlockChange.src)
protocol(107).state(PLAY).from_server(0x11, "ConfirmTransaction", protocol(47).PlayClientboundConfirmTransaction.src)
protocol(107).state(PLAY).from_server(0x12, "CloseWindow", protocol(47).PlayClientboundCloseWindow.src)
protocol(107).state(PLAY).from_server(0x13, "OpenWindow", protocol(47).PlayClientboundOpenWindow.src)
protocol(107).state(PLAY).from_server(0x14, "WindowItems", protocol(47).PlayClientboundWindowItems.src)
protocol(107).state(PLAY).from_server(0x15, "WindowProperty", protocol(47).PlayClientboundWindowProperty.src)
protocol(107).state(PLAY).from_server(0x16, "SetSlot", protocol(47).PlayClientboundSetSlot.src)
protocol(107).state(PLAY).from_server(0x17, "SetCooldown", """
    item            varint
    cooldown        varint
""")
protocol(107).state(PLAY).from_server(0x18, "PluginMessage", protocol(47).PlayClientboundPluginMessage.src)
protocol(107).state(PLAY).from_server(0x19, "NamedSoundEffect", """
    sound           string
    category        varint
    x               int8
    y               int8
    z               int8
    volume          float
    pitch           ubyte
""")
protocol(107).state(PLAY).from_server(0x1a, "Disconnect", protocol(47).PlayClientboundDisconnect.src)
protocol(107).state(PLAY).from_server(0x1b, "EntityStatus", protocol(47).PlayClientboundEntityStatus.src)
protocol(107).state(PLAY).from_server(0x1c, "Explosion", protocol(47).PlayClientboundExplosion.src)
protocol(107).state(PLAY).from_server(0x1d, "UnloadChunk", """
    x               int
    z               int
""")
protocol(107).state(PLAY).from_server(0x1e, "ChangeGameState", protocol(47).PlayClientboundChangeGameState.src)
protocol(107).state(PLAY).from_server(0x1f, "KeepAlive", protocol(47).PlayClientboundKeepAlive.src)
protocol(107).state(PLAY).from_server(0x20, "ChunkData", """
    chunk_x         int
    chunk_z         int
    continuous      bool
    primary_bitmap  varint
    data            varint_byte_array
""")
protocol(107).state(PLAY).from_server(0x21, "Effect", protocol(47).PlayClientboundEffect.src)
protocol(107).state(PLAY).from_server(0x22, "Particle", protocol(47).PlayClientboundParticle.src)
protocol(107).state(PLAY).from_server(0x23, "JoinGame", protocol(47).PlayClientboundJoinGame.src)
protocol(107).state(PLAY).from_server(0x24, "Map", """
    map_id          varint
    scale           byte
    show_icons      bool
    icons           map_icons
    columns         ubyte
    rows            ubyte               self.columns > 0
    x               ubyte               self.columns > 0
    y               ubyte               self.columns > 0
    data            varint_byte_array   self.columns > 0
""")
protocol(107).state(PLAY).from_server(0x25, "EntityRelativeMove", """
    eid             varint
    dx              short4096
    dy              short4096
    dz              short4096
    on_ground       bool
""")
protocol(107).state(PLAY).from_server(0x26, "EntityLookAndRelativeMove", """
    eid             varint
    dx              short4096
    dy              short4096
    dz              short4096
    yaw             ubyte
    pitch           ubyte
    on_ground       bool
""")
protocol(107).state(PLAY).from_server(0x27, "EntityLook", protocol(47).PlayClientboundEntityLook.src)
protocol(107).state(PLAY).from_server(0x28, "Entity", protocol(47).PlayClientboundEntity.src)
protocol(107).state(PLAY).from_server(0x29, "VehicleMove", """
    x               double
    y               double
    z               double
    yaw             float
    pitch           float
""")
protocol(107).state(PLAY).from_server(0x2a, "SignEditorOpen", protocol(47).PlayClientboundSignEditorOpen.src)
protocol(107).state(PLAY).from_server(0x2b, "PlayerAbilities", protocol(47).PlayClientboundPlayerAbilities.src)
protocol(107).state(PLAY).from_server(0x2c, "CombatEvent", """
    event           ubyte
    duration        varint              self.event == 1
    end_eid         int                 self.event == 1
    player_id       varint              self.event == 2
    dead_eid        int                 self.event == 2
    message         json                self.event == 2
""")
protocol(107).state(PLAY).from_server(0x2d, "PlayerListItem", protocol(47).PlayClientboundPlayerListItem.src)
protocol(107).state(PLAY).from_server(0x2e, "PlayerPositionAndLook", """
    x               double
    y               double
    z               double
    yaw             float
    pitch           float
    flag            byte
    teleport_id     varint
""")
protocol(107).state(PLAY).from_server(0x2f, "UseBed", protocol(47).PlayClientboundUseBed.src)
protocol(107).state(PLAY).from_server(0x30, "DestroyEntities", protocol(47).PlayClientboundDestroyEntities.src)
protocol(107).state(PLAY).from_server(0x31, "RemoveEntityEffect", protocol(47).PlayClientboundRemoveEntityEffect.src)
protocol(107).state(PLAY).from_server(0x32, "ResourcePackSend", protocol(47).PlayClientboundResourcePackSend.src)
protocol(107).state(PLAY).from_server(0x33, "Respawn", protocol(47).PlayClientboundRespawn.src)
protocol(107).state(PLAY).from_server(0x34, "EntityHeadLook", protocol(47).PlayClientboundEntityHeadLook.src)
protocol(107).state(PLAY).from_server(0x35, "WorldBorder", protocol(47).PlayClientboundWorldBorder.src)
protocol(107).state(PLAY).from_server(0x36, "Camera", protocol(47).PlayClientboundCamera.src)
protocol(107).state(PLAY).from_server(0x37, "HeldItemChange", protocol(47).PlayClientboundHeldItemChange.src)
protocol(107).state(PLAY).from_server(0x38, "DisplayScoreboard", protocol(47).PlayClientboundDisplayScoreboard.src)
protocol(107).state(PLAY).from_server(0x39, "EntityMetadata", protocol(47).PlayClientboundEntityMetadata.src)
protocol(107).state(PLAY).from_server(0x3a, "AttachEntity", """
    eid             int
    vehicle_id      int
""")
protocol(107).state(PLAY).from_server(0x3b, "EntityVelocity", protocol(47).PlayClientboundEntityVelocity.src)
protocol(107).state(PLAY).from_server(0x3c, "EntityEquipment", """
    eid             varint
    slot            varint
    item            slot_1_8
""")
protocol(107).state(PLAY).from_server(0x3d, "SetExperience", protocol(47).PlayClientboundSetExperience.src)
protocol(107).state(PLAY).from_server(0x3e, "HealthUpdate", protocol(47).PlayClientboundHealthUpdate.src)
protocol(107).state(PLAY).from_server(0x3f, "ScoreboardObjective", protocol(47).PlayClientboundScoreboardObjective.src)
protocol(107).state(PLAY).from_server(0x40, "SetPassengers", """
    eid             varint
    passengers      varint_varint_array
""")
protocol(107).state(PLAY).from_server(0x41, "Teams", """
    team_name           string
    mode                byte
    display_name        string              self.mode in (0, 2)
    prefix              string              self.mode in (0, 2)
    suffix              string              self.mode in (0, 2)
    friendly_fire       byte                self.mode in (0, 2)
    name_tag_visible    string              self.mode in (0, 2)
    collision_rule      string              self.mode in (0, 2)
    color               byte                self.mode in (0, 2)
    players             varint_string_array self.mode in (0, 3, 4)
""")
protocol(107).state(PLAY).from_server(0x42, "UpdateScore", protocol(47).PlayClientboundUpdateScore.src)
protocol(107).state(PLAY).from_server(0x43, "SpawnPosition", protocol(47).PlayClientboundSpawnPosition.src)
protocol(107).state(PLAY).from_server(0x44, "TimeUpdate", protocol(47).PlayClientboundTimeUpdate.src)
protocol(107).state(PLAY).from_server(0x45, "Title", protocol(47).PlayClientboundTitle.src)
protocol(107).state(PLAY).from_server(0x46, "UpdateSign", protocol(47).PlayClientboundUpdateSign.src)
protocol(107).state(PLAY).from_server(0x47, "SoundEffect", """
    sound           varint
    category        varint
    x               int8
    y               int8
    z               int8
    volume          float
    pitch           ubyte
""")
protocol(107).state(PLAY).from_server(0x48, "PlayerListHeaderFooter",
                                      protocol(47).PlayClientboundPlayerListHeaderFooter.src)
protocol(107).state(PLAY).from_server(0x49, "CollectItem", protocol(47).PlayClientboundCollectItem.src)
protocol(107).state(PLAY).from_server(0x4a, "EntityTeleport", """
    eid             varint
    x               double
    y               double
    z               double
    yaw             ubyte
    pitch           ubyte
    on_ground       bool
""")
protocol(107).state(PLAY).from_server(0x4b, "EntityProperties", """
    eid             int
    properties      property_array
""")
protocol(107).state(PLAY).from_server(0x4c, "EntityEffect", protocol(47).PlayClientboundEntityEffect.src)

protocol(107).state(PLAY).from_client(0x00, "TeleportConfirm", """
    teleport_id     varint
""")
protocol(107).state(PLAY).from_client(0x01, "TabComplete", """
    text            string
    assume_command  bool
    has_position    bool
    location        position_packed     self.has_position
""")
protocol(107).state(PLAY).from_client(0x02, "ChatMessage", protocol(47).PlayServerboundChatMessage.src)
protocol(107).state(PLAY).from_client(0x03, "ClientStatus", protocol(47).PlayServerboundClientStatus.src)
protocol(107).state(PLAY).from_client(0x04, "ClientSettings", """
    locale          string
    view_distance   byte
    chat_flags      varint
    chat_colors     bool
    displayed_skin  ubyte
    main_hand       varint
""")
protocol(107).state(PLAY).from_client(0x05, "ConfirmTransaction", protocol(47).PlayServerboundConfirmTransaction.src)
protocol(107).state(PLAY).from_client(0x06, "EnchantItem", protocol(47).PlayServerboundEnchantItem.src)
protocol(107).state(PLAY).from_client(0x07, "ClickWindow", protocol(47).PlayServerboundClickWindow.src)
protocol(107).state(PLAY).from_client(0x08, "CloseWindow", protocol(47).PlayServerboundCloseWindow.src)
protocol(107).state(PLAY).from_client(0x09, "PluginMessage", protocol(47).PlayServerboundPluginMessage.src)
protocol(107).state(PLAY).from_client(0x0a, "UseEntity", """
    target          varint
    type            varint
    target_x        float               self.type == 2
    target_y        float               self.type == 2
    target_z        float               self.type == 2
    hand            varint              self.type == 0 or self.type == 2
""")
protocol(107).state(PLAY).from_client(0x0b, "KeepAlive", protocol(47).PlayServerboundKeepAlive.src)
protocol(107).state(PLAY).from_client(0x0c, "PlayerPosition", protocol(47).PlayServerboundPlayerPosition.src)
protocol(107).state(PLAY).from_client(0x0d, "PlayerPositionAndLook",
                                      protocol(47).PlayServerboundPlayerPositionAndLook.src)
protocol(107).state(PLAY).from_client(0x0e, "PlayerLook", protocol(47).PlayServerboundPlayerLook.src)
protocol(107).state(PLAY).from_client(0x0f, "Player", protocol(47).PlayServerboundPlayer.src)
protocol(107).state(PLAY).from_client(0x10, "VehicleMove", """
    x               double
    y               double
    z               double
    yaw             float
    pitch           float
""")
protocol(107).state(PLAY).from_client(0x11, "SteerBoat", """
    right_paddle    bool
    left_paddle     bool
""")
protocol(107).state(PLAY).from_client(0x12, "PlayerAbilities", protocol(47).PlayServerboundPlayerAbilities.src)
protocol(107).state(PLAY).from_client(0x13, "PlayerDigging", protocol(47).PlayServerboundPlayerDigging.src)
protocol(107).state(PLAY).from_client(0x14, "EntityAction", protocol(47).PlayServerboundEntityAction.src)
protocol(107).state(PLAY).from_client(0x15, "SteerVehicle", protocol(47).PlayServerboundSteerVehicle.src)
protocol(107).state(PLAY).from_client(0x16, "ResourcePackStatus", protocol(47).PlayServerboundResourcePackStatus.src)
protocol(107).state(PLAY).from_client(0x17, "HeldItemChange", protocol(47).PlayServerboundHeldItemChange.src)
protocol(107).state(PLAY).from_client(0x18, "CreativeInventoryAction",
                                      protocol(47).PlayServerboundCreativeInventoryAction.src)
protocol(107).state(PLAY).from_client(0x19, "UpdateSign", """
    location        position_packed
    line1           string
    line2           string
    line3           string
    line4           string
""")
protocol(107).state(PLAY).from_client(0x1a, "Animation", """
    hand            varint
""")
protocol(107).state(PLAY).from_client(0x1b, "Spectate", protocol(47).PlayServerboundSpectate.src)
protocol(107).state(PLAY).from_client(0x1c, "BlockPlacement", """
    location        position_packed
    direction       varint
    hand            varint
    cursor_x        byte
    cursor_y        byte
    cursor_z        byte
""")
protocol(107).state(PLAY).from_client(0x1d, "UseItem", """
    hand            varint
""")
