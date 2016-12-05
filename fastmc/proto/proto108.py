from proto import PLAY, protocol

protocol(108).set_name("1.9.1")
protocol(108).based_on(107)
protocol(108).state(PLAY).from_server(0x23, """
    eid             int
    game_mode       ubyte
    dimension       int
    difficulty      ubyte
    max_players     ubyte
    level_type      string
    reduced_debug   bool
""")

protocol(109).set_name("1.9.2")
protocol(109).based_on(108)
