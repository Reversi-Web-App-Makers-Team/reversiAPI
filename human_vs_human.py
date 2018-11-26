def Human_vs_Human(name_1, name_2):
    p1 = PlayerHuman(player_b, name_1)
    p2 = PlayerHuman(player_w, name_2)
    game = ReversiOrgnaizer(p1, p2)
    game.progress()