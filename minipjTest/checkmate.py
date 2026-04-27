def checkmate(board):
    grid = board.splitlines()
    n = len(grid)
    print(f"Board size: {n}x{n}")

    # สแกนหา King
    king = None
    for i in range(n):
        for j in range(n):
            #print(f"at ({i}, {j})")
            if grid[i][j] == 'K':
                king = (i, j)
                print("Found King")
                

    if not king:
        print("No King found")
        return

    kx, ky = king
    #print(f"king located at ({kx}, {ky})")

    # ตรวจสอบขอบเขต
    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    #4 x 4 1
    #3 x 4 0

    #4 x 4 1
    #4 x 3 0

    # 
    for dx, dy in [(1, -1), (1, 1)]:
        x, y = kx + dx, ky + dy
        #1 2x, 1y = =2 1kx + 1dx, =1 2ky + -1dy
        #2 2x, 3y = 2 1kx + 1dx, =3 2ky + 1dy

        #grid = ['....','..K.','.P..','....']

        if in_bounds(x, y) and grid[x][y] == 'P':
            print("Success")
            return


    # directions
    directions = {
        'R': [(-1,0),(1,0),(0,-1),(0,1)],
        'B': [(-1,-1),(-1,1),(1,-1),(1,1)],
        'Q': [(-1,0),(1,0),(0,-1),(0,1),
              (-1,-1),(-1,1),(1,-1),(1,1)]
    }

    for piece, dirs in directions.items():
        print(f"Checking for {piece} in directions: {dirs}")
        for dx, dy in dirs:
            #r
            # -1 , 0
            # 1 , 0
            # 0 , -1
            # 0 , 1

            #q
            # -1 , 0
            # 1 , 0
            # 0 , -1
            # 0 , 1       
            # -1 , -1
            # -1 , 1
            # 1 , -1
            # 1 , 1

            x, y = kx + dx, ky + dy

            #r
            # 0 , 2
            # 2 , 2
            # 1 , 1
            # 1 , 3

            #q
            # 0 , 2
            # 2 , 2
            # 1 , 1
            # 1 , 3
            #x=0 y=1
            #x=1 y=3
            #x=2 y=0
            #x=2 y=4

            while in_bounds(x, y):
                if grid[x][y] != '.':
                    if grid[x][y] == piece:
                        print("Success")
                        return
                    break
                x += dx
                y += dy
                print(f"Checking position ({x}, {y}) for {piece}")

                #x0+=-1=-1 , y2+=0 =2
                #x2+=1 =3 , y2+=0=2
                #x1+=0=1 , y1+=-1=0
                #x1+=0=1, y3+=1=4
                



    print("Fail")