import curses

# Fonction à modifier 
def next_state (state):
    new_state = []
    for i in range(len(state)):
        line = ["."]*len(state[i])
        new_state.append(line)
    neighbours = 0
    for y in range(len(state)):
        for x in range(len(state[y])):
            for i in range(y-1,y+1):
                for j in range(x-1,x+1): 
                    if state[i][j]=="O":
                        neighbours+=1
                        if state[y][x]=="O":
                            neighbours-= 1 
    if state[y][x]=="." and neighbours==3:
        new_state[y][x]="O"
    elif state[y][x]=="O" and neighbours==2 or neighbours==3:
        new_state[y][x]="O"
    else: 
        new_state[y][x]="."
    return new_state

# Fonction principale, que vous n'avez pas à modifier ;
# stdscr est l'objet qui représente l'écran dans curses
def main (stdscr):
    # On désactive le curseur de texte dans la fenêtre de curses
    curses.curs_set(False) 
    
    # On lit la grille initiale, modifiable dans cells.txt
    text_file = open("cells.txt", "r")
    state = text_file.read().splitlines()

    # Boucle de jeu :
    # Tant que l'input utilisateur est différent de "q", on reste dans le jeu
    key = " "
    while key != "q":
        # On vide l'écran
        stdscr.clear()

        # Préparation de l'affichage ligne par ligne
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == "O":
                    stdscr.addstr(i, j, "O") # attention, curses met y avant x

        # Fonction qui affiche ce qu'on a préparé
        stdscr.refresh()
        
        # La fonction next_state() retourne le prochain état du jeu de la vie
        state = next_state(state)

        # Fonction qui attend un input utilisateur
        key = stdscr.getkey()

# Curses s'exécute au sein d'un wrapper, afin de ne pas perturber l'affichage du
# shell lorsqu'on ferme le programme
curses.wrapper(main)