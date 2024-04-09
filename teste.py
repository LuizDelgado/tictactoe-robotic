def draw_x(pos:str, height:int, font_size:int):
    positions = pos.split(",")
    p1 = positions.copy()
    p1_aerea = p1.copy()
    p1_aerea[2] = float(p1_aerea[2].strip()) + height
    p1[0] = float(p1[0]) - 5*font_size #x
    p1[1] = float(p1[1]) - 5*font_size #y

draw_x("155.30, -146.50, 419.00, -180.00, 0.00, -180.00", 20, 5)