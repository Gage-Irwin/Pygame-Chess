import pygame
import os

pygame.font.init()

NODE_SIZE = 100

WIDTH = 8*NODE_SIZE
HEIGHT = 8*NODE_SIZE
pygame.display.set_caption("chess")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
TEXT_FONT = pygame.font.SysFont('comicsans', 60)
TEXT_FONT_2 = pygame.font.SysFont('comicsans', 30)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
GREY = (169, 169, 169)
DARK_BROWN = (179,133,100)
LIGHT_BROWN = (210,179,140)

# piece images
BISHOP_BLACK_IMAGE = pygame.image.load(os.path.join('assets','bishop_b.png'))
BISHOP_BLACK = pygame.transform.scale(BISHOP_BLACK_IMAGE, (NODE_SIZE, NODE_SIZE))
BISHOP_WHITE_IMAGE = pygame.image.load(os.path.join('assets','bishop_w.png'))
BISHOP_WHITE = pygame.transform.scale(BISHOP_WHITE_IMAGE, (NODE_SIZE, NODE_SIZE))
KING_BLACK_IMAGE = pygame.image.load(os.path.join('assets','king_b.png'))
KING_BLACK = pygame.transform.scale(KING_BLACK_IMAGE, (NODE_SIZE, NODE_SIZE))
KING_WHITE_IMAGE = pygame.image.load(os.path.join('assets','king_w.png'))
KING_WHITE = pygame.transform.scale(KING_WHITE_IMAGE, (NODE_SIZE, NODE_SIZE))
KNIGHT_BLACK_IMAGE = pygame.image.load(os.path.join('assets','knight_b.png'))
KNIGHT_BLACK = pygame.transform.scale(KNIGHT_BLACK_IMAGE, (NODE_SIZE, NODE_SIZE))
KNIGHT_WHITE_IMAGE = pygame.image.load(os.path.join('assets','knight_w.png'))
KNIGHT_WHITE = pygame.transform.scale(KNIGHT_WHITE_IMAGE, (NODE_SIZE, NODE_SIZE))
PAWN_BLACK_IMAGE = pygame.image.load(os.path.join('assets','pawn_b.png'))
PAWN_BLACK = pygame.transform.scale(PAWN_BLACK_IMAGE, (NODE_SIZE, NODE_SIZE))
PAWN_WHITE_IMAGE = pygame.image.load(os.path.join('assets','pawn_w.png'))
PAWN_WHITE = pygame.transform.scale(PAWN_WHITE_IMAGE, (NODE_SIZE, NODE_SIZE))
QUEEN_BLACK_IMAGE = pygame.image.load(os.path.join('assets','queen_b.png'))
QUEEN_BLACK = pygame.transform.scale(QUEEN_BLACK_IMAGE, (NODE_SIZE, NODE_SIZE))
QUEEN_WHITE_IMAGE = pygame.image.load(os.path.join('assets','queen_w.png'))
QUEEN_WHITE = pygame.transform.scale(QUEEN_WHITE_IMAGE, (NODE_SIZE, NODE_SIZE))
ROOK_BLACK_IMAGE = pygame.image.load(os.path.join('assets','rook_b.png'))
ROOK_BLACK = pygame.transform.scale(ROOK_BLACK_IMAGE, (NODE_SIZE, NODE_SIZE))
ROOK_WHITE_IMAGE = pygame.image.load(os.path.join('assets','rook_w.png'))
ROOK_WHITE = pygame.transform.scale(ROOK_WHITE_IMAGE, (NODE_SIZE, NODE_SIZE))

STARTING_BOARD = [
    [(ROOK_BLACK,True),(KNIGHT_BLACK,True),(BISHOP_BLACK,True),(QUEEN_BLACK,True),(KING_BLACK,True),(BISHOP_BLACK,True),(KNIGHT_BLACK,True),(ROOK_BLACK,True)],
    [(PAWN_BLACK,True),(PAWN_BLACK,True),(PAWN_BLACK,True),(PAWN_BLACK,True),(PAWN_BLACK,True),(PAWN_BLACK,True),(PAWN_BLACK,True),(PAWN_BLACK,True)],
    [(None,None),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None)],
    [(None,None),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None)],
    [(None,None),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None)],
    [(None,None),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None)],
    [(PAWN_WHITE,False),(PAWN_WHITE,False),(PAWN_WHITE,False),(PAWN_WHITE,False),(PAWN_WHITE,False),(PAWN_WHITE,False),(PAWN_WHITE,False),(PAWN_WHITE,False)],
    [(ROOK_WHITE,False),(KNIGHT_WHITE,False),(BISHOP_WHITE,False),(QUEEN_WHITE,False),(KING_WHITE,False),(BISHOP_WHITE,False),(KNIGHT_WHITE,False),(ROOK_WHITE,False)]
]

END_SCREEN = pygame.Rect(NODE_SIZE+NODE_SIZE/2, 2*NODE_SIZE+NODE_SIZE/2, 5*NODE_SIZE, 2*NODE_SIZE)

class Node():

    def __init__(self, x, y, piece = None, team = None, moved = False):
        self.pos = (x,y)
        self.border = pygame.Rect(self.pos[0]*NODE_SIZE, self.pos[1]*NODE_SIZE, NODE_SIZE, NODE_SIZE)
        self.piece = piece
        self.team = team
        self.moved = moved
        self.castle_to = False
        self.selected = False
        self.clicked = False
        self.move_to = False
        self.check = False

    def move(self, node):
        node.piece, node.team, node.moved = self.piece, self.team, True
        self.piece, self.team, self.moved, self.check = None, None, False, None

    def checked(self):
        self.check = True

    def unchecked(self):
        self.check = False

    def castle(self):
        self.castle_to = True

    def uncastle(self):
        self.castle_to = False

    def unselect(self):
        self.selected = False

    def mark(self):
        self.move_to = True

    def unmark(self):
        self.move_to = False
        self.castle_to = False

    def draw(self, turn):

        action = False

        mouse_pos = pygame.mouse.get_pos()

        if self.selected:
            pygame.draw.rect(screen, GREEN, self.border, 4)

        elif self.check:
            pygame.draw.rect(screen, RED, self.border, 4)

        if self.move_to:
            pygame.draw.rect(screen, RED, self.border, 4)

            if self.border.collidepoint(mouse_pos):
                pygame.draw.rect(screen, BLUE, self.border, 4)
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

                elif pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

        if self.border.collidepoint(mouse_pos) and self.piece and self.team == turn:

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                self.selected = not self.selected

            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        if self.piece:
            screen.blit(self.piece, (self.pos[0]*NODE_SIZE, self.pos[1]*NODE_SIZE))

        return action

class Board():

    def __init__(self):
        self.reset_board()
        self.background = []
        [self.background.append([pygame.Rect(x*NODE_SIZE, y*NODE_SIZE, NODE_SIZE, NODE_SIZE) for x in range(8)]) for y in range(8)]

    def reset_board(self):
        self.board = self.new_board()
        self.turn = True
        self.winner = (None, None)
        self.selected_node = None

    def new_board(self):
        return [[Node(index_x, index_y, x[0], x[1]) for index_x, x in enumerate(y)] for index_y, y in enumerate(STARTING_BOARD)]

    def next_turn(self):
        self.turn = not self.turn

    def copy_board(self, board):
        return [[Node(index_x, index_y, x.piece, x.team, x.moved) for index_x, x in enumerate(y)] for index_y, y in enumerate(board)]

    def moveable(self, board, team, x, y, x1, y1, valid_moves):
        # out of bounds check
        if y+y1 < 0 or y+y1 > 7 or x+x1 < 0 or x+x1 > 7 or (x1 == 0 and y1 == 0):
            return True
        node = board[y+y1][x+x1]
        if node.piece == None:
            valid_moves.append(node)
            return True
        if node.team != team:
            valid_moves.append(node)
        return False

    def get_valid_moves(self, board, node, team, checking = False):
        if node.piece == None:
            return []

        valid_moves = []
        y = node.pos[1]
        x = node.pos[0]
        if node.piece in {PAWN_BLACK, PAWN_WHITE}:
            # set direction pawn s moving
            d = 1 if node.team else -1
            if board[y+1*d][x].piece == None:
                valid_moves.append(board[y+1*d][x])
                # first move double space
                if not node.moved:
                    if board[y+2*d][x].piece == None:
                        valid_moves.append(board[y+2*d][x])
            # check if pawn can attack
            for c in {1,-1}:
                if x+c < 0 or x+c >7: continue # out of bounds
                if board[y+1*d][x+c].team != team and board[y+1*d][x+c].piece != None:
                    valid_moves.append(board[y+1*d][x+c])

        if node.piece in {ROOK_BLACK, ROOK_WHITE, QUEEN_BLACK, QUEEN_WHITE}:
            for c in {(0,1),(1,0),(0,-1),(-1,0)}:
                    for n in range(8):
                        if not self.moveable(board,team,x,y,c[0]*n,c[1]*n, valid_moves): break

        if node.piece in {KNIGHT_BLACK, KNIGHT_WHITE}:
            for c in {(2,1),(1,2)}:
                for s in {(-1,-1),(-1,1),(1,-1),(1,1)}:
                    self.moveable(board,team,x,y,c[0]*s[0],c[1]*s[1], valid_moves)

        if node.piece in {BISHOP_BLACK, BISHOP_WHITE, QUEEN_BLACK, QUEEN_WHITE}:
            for c in {(1,1),(-1,1),(1,-1),(-1,-1)}:
                for n in range(8):
                    if not self.moveable(board,team,x,y,c[0]*n,c[1]*n, valid_moves): break

        if node.piece in {KING_BLACK, KING_WHITE}:
            for c in {(1,1),(-1,1),(1,-1),(-1,-1),(0,1),(1,0),(0,-1),(-1,0)}:
                if not self.moveable(board,team,x,y,c[0],c[1], valid_moves): continue

            # castling
            if not node.moved:
                if not self.board[y][x+3].moved and self.board[y][x+3].piece in {ROOK_BLACK, ROOK_WHITE} and self.board[y][x+1].piece == None and self.board[y][x+2].piece == None:
                    valid_moves.append(self.board[y][x+2])
                    self.board[y][x+2].castle()

                if not self.board[y][x-4].moved and self.board[y][x-4].piece in {ROOK_BLACK, ROOK_WHITE} and self.board[y][x-1].piece == None and self.board[y][x-2].piece == None and self.board[y][x-3].piece == None:
                    valid_moves.append(self.board[y][x-2])
                    self.board[y][x-2].castle()

        final_moves = []
        # don't allow moving into check
        if not checking:
            for valid_move in valid_moves:
                future_board = self.copy_board(self.board)
                self.move_piece(future_board, future_board[y][x], future_board[valid_move.pos[1]][valid_move.pos[0]], True)
                if not self.check_check(future_board, self.find_king(future_board, node.team)):
                    final_moves.append(valid_move)
        else:
            final_moves = valid_moves

        # remove castle move if space next to king is in check
        if node.piece in {KING_BLACK, KING_WHITE}:
            if not node.moved:
                s = 0 if node.team else 7
                if not self.board[s][5] in final_moves and self.board[s][6] in final_moves:
                    final_moves.remove(self.board[s][6])
                    self.board[s][6].uncastle()
                if not self.board[s][3] in final_moves and self.board[s][2] in final_moves:
                    final_moves.remove(self.board[s][2])
                    self.board[s][2].uncastle()

        return final_moves

    def show_valid_moves(self, node):
        valid_moves = self.get_valid_moves(self.board, node, self.turn)
        for valid_move in valid_moves:
            valid_move.mark()

    def hide_valid_moves(self):
        for y in self.board:
            for x in y:
                x.unmark()

    def unselect_other_nodes(self, node):
        for y in self.board:
            for x in y:
                if x != node:
                    x.unselect()

    def promote_pawn(self, node):
        node.piece = QUEEN_BLACK if node.team else QUEEN_WHITE

    def find_king(self, board, team):
        for y in board:
            for x in y:
                if (team and x.piece == KING_BLACK) or (not team and x.piece == KING_WHITE):
                    return x

    def move_piece(self, board, node_from, node_to, future = False):
        node_from.move(node_to)

        # move rook for castle move
        if node_to.castle_to:
            d = 0 if node_to.team else 7
            if node_to.pos[0] == 6:
                self.move_piece(board, board[d][7], board[d][5])
            if node_to.pos[0] == 2:
                self.move_piece(board, board[d][0], board[d][3])

        # check if pawn should be promoted
        if node_to.piece in {PAWN_BLACK, PAWN_WHITE}:
            if (node_to.team and node_to.pos[1] == 7) or (not node_to.team and node_to.pos[1] == 0):
                self.promote_pawn(node_to)

        # highlight enemy king if in check
        if not future:
            self.show_check(board, self.find_king(board, not node_to.team))
            self.show_check(board, self.find_king(board, node_to.team))
            if self.check_checkmate(board, self.find_king(board, not node_to.team)):
                self.winner = (True, node_to.team)

    def show_check(self, board, node):
        if self.check_check(board, node):
            node.checked()
        else:
            node.unchecked()

    def check_check(self, board, node):
        for y in board:
            for x in y:
                moves = self.get_valid_moves(board, x, x.team, True)
                if node in moves:
                    return True
        return False

    def check_checkmate(self, board, node):
        if not self.check_check(board, node):
            return False

        if self.get_valid_moves(board, self.find_king(board, node.team), node.team):
            return False

        checking_moves = []
        for y in board:
            for x in y:
                moves = self.get_valid_moves(board, x, x.team, True)
                if node in moves:
                    checking_moves += moves
                    checking_moves.append(x)

        for y in board:
            for x in y:
                if x.team == node.team:
                    moves = self.get_valid_moves(board, x, x.team)
                    for checking_move in checking_moves:
                        if checking_move in moves:
                            return False

        return True

    def draw(self):
        # draw board background
        for index_y, y in enumerate(self.background):
            for index_x, x in enumerate(y):
                if (index_x+index_y)%2 == 0:
                    pygame.draw.rect(screen, LIGHT_BROWN, x)
                else:
                    pygame.draw.rect(screen, DARK_BROWN, x)
        # draw pieces
        for y in self.board:
            for x in y:
                if x.draw(self.turn):
                    if x.selected:
                        self.selected_node = x
                        self.unselect_other_nodes(x)
                        self.hide_valid_moves()
                        self.show_valid_moves(x)
                    elif x.move_to:
                        self.move_piece(self.board, self.selected_node, x)
                        self.hide_valid_moves()
                        self.selected_node = None
                        self.unselect_other_nodes(None)
                        self.next_turn()
                    else:
                        self.hide_valid_moves()
                        self.selected_node = None
        # winner screen
        if self.winner[0]:
            pygame.draw.rect(screen, WHITE, END_SCREEN)
            pygame.draw.rect(screen, BLACK, END_SCREEN, 5)
            if self.winner[1]:
                end_text = TEXT_FONT.render("BLACK WON!", 1, BLACK)
            else:
                end_text = TEXT_FONT.render("WHITE WON!", 1, BLACK)
            screen.blit(end_text, (END_SCREEN.x+(5*NODE_SIZE - end_text.get_width())//2, END_SCREEN.y+20))
            end_text = TEXT_FONT_2.render("Press 'r' to reset board.", 1, BLACK)
            screen.blit(end_text, (END_SCREEN.x+80, END_SCREEN.y+120))

def main():

    Chess = Board()
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    Chess.reset_board()
        screen.fill(WHITE)
        Chess.draw()

        pygame.display.update()

if __name__ == '__main__':
    main()