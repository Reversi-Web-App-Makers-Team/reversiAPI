def Human_vs_Human():
    a = input("player1の名前は?:")
    b = input("player2の名前は?:")
    p1 = PlayerHuman(player_w, a)
    p2 = PlayerHuman(player_b, b)
    game = ReversiOrgnaizer(p1, p2)
    game.progress()