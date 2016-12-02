from proto import PLAY, protocol

protocol(4).set_name("1.7.2")
protocol(4).based_on(3)
protocol(4).state(PLAY).from_server(0x22, "MultiBlockChange", """
    chunk_x         int
    chunk_z         int
    changes         changes
""")
