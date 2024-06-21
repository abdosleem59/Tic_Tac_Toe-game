class TicTacToe:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player = "X"
        self.shape = "X"
        self.steps = 0

    def basic_structure(self):
        n = (self.grid_size *2) -1
        shapes_lst = [['|' if j%2!=0 else ' ' for j in range(n)] for _ in range(self.grid_size)]
        return shapes_lst
    
    
    def insert_shape(self,lst_shapes,shape,r,c,win_tie_lst):
        # shape: X or O
        lst_shapes[r-1][(c-1)*2] = shape
        # (c-1)*2 because the row consists of n*shape + (n-1) * | 

        # this variable for (tie!) to count the inputs if the game ended == grid_size * grid_size
        self.steps+=1

        if shape == "X":
            win_tie_lst[0][r-1]+=1
            win_tie_lst[1][c-1]+=1
            if r==c:
                win_tie_lst[4][0]+=1
            if (r-1)+(c-1)==grid_size-1:
                win_tie_lst[6][0]+=1

        if shape == "O":
            win_tie_lst[2][r-1]+=1
            win_tie_lst[3][c-1]+=1
            if r==c:
                win_tie_lst[5][0]+=1
            if (r-1)+(c-1)==grid_size-1:
                win_tie_lst[7][0]+=1

        return lst_shapes
    
    def win_tie(self):
        '''
        x_count_row = [0] * self.grid_size == [0,0,0]
        x_count_col = [0] * self.grid_size == [0,0,0]
        o_count_row = [0] * self.grid_size == [0,0,0]
        o_count_col = [0] * self.grid_size == [0,0,0]
        x_left_daig = [0]
        o_left_daig = [0]
        x_right_diag = [0]
        o_right_diag = [0]
        '''
        win_tie_lst = [[0 for _ in range(self.grid_size)] for _ in range(4)]
        win_tie_lst.append([0])
        win_tie_lst.append([0])
        win_tie_lst.append([0])
        win_tie_lst.append([0])

        return win_tie_lst

    
    def check_win_tie(self,win_tie_lst):
        if self.grid_size*self.grid_size == self.steps:
            print("Tie!")
            return True
        for i, lst in enumerate(win_tie_lst):
            for j, item in enumerate(lst):
                if lst[j] == grid_size:
                    if i == 0 or i ==1 or i == 4 or i == 6:
                        print("Player X won!")
                        return True
                    elif i==2 or i ==3 or i ==5 or i==7:
                        print("Player O won!")
                        return True
        
        return False
    
    
    def role(self):
        if self.player=="X":
            self.shape ="X"
            self.player ="O"
            return "Player X, make a move: "
        elif self.player=="O":
            self.shape = "O"
            self.player ="X"
            return "Player O, make a move: "

    def location_validation(self,r,c,lst_shapes):

        if r-1> (self.grid_size-1) or c-1> (self.grid_size-1) or (lst_shapes[r-1][(c-1)*2] !=' '):
            if self.player=="X":
                self.player ="O"
            else:
                self.player = "X"
            print("Invalid location. Try again!")
            return False
        
        return True
        



if __name__ == "__main__":

    grid_size = int(input("Enter grid size: "))
    while grid_size<3:
        print("Please enter grid_size from 3 and above. Thanks.")
        grid_size = int(input("Enter grid size: "))

    tic = TicTacToe(grid_size)
    lst_shapes = tic.basic_structure()
    win_tie_lst = tic.win_tie()
    
    while True:
        r,c = map(int,input(f'{tic.role()}').split())
        
        while not tic.location_validation(r,c,lst_shapes):
            r,c = map(int,input(f'{tic.role()}').split())
            
        lst_shapes = tic.insert_shape(lst_shapes,tic.shape,r,c,win_tie_lst)

        for board in lst_shapes:
            print(*board)

        check  = tic.check_win_tie(win_tie_lst)
        if check:
            break
        
