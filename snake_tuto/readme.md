# Snake

Snake est un jeu à un joueur, en deux dimensions.

Le serpent "snake" avance régulièrement. Il est composé de blocs carrés.

Lorsque sa tête rencontre de la nourriture il la mange et il grandit.

Lorsque sa tête sort de l'écran ou touche son propre corps, il meurt.

Un bloc carré de nourriture est présent à l'écran. Il réapparait
aléatoirement dans une case inoccupée chaque fois que snake
le mange.

Il peut diriger sa tête dans les directions NSEO et peut tourner de 90°
à chaque étape.

## Pygame Zero.

Nous allons utiliser la librarie "pygame zero" qui permet de créer
des jeux pygame sans trop de contrainte.

C'est une surcouche de **pygame**, la célèbre librairie de jeux vidéos de
Python.

L'intérêt de cette librairie est de pouvoir créer rapidement des jeux
en deux dimensions sans devoir s'occuper de nombre d'éléments délicats
de pygame comme l'écran, les ticks d'horloge et compagnie.


Un script PGZERO minimal est constituté de très peu d'éléments :

* une fonction `draw` qui dessine les éléments ;
* une fonction `update` qui gère les transitions entre les frames.

Contrairement à pygame seul pgzero s'occupe de toutes les transitions, de
l'horloge et compagnie.


## Que font ces deux fonctions ?

* `draw` permet de dessiner tous les éléments à l'écran. Elle est appelée 60
  fois par seconde.
* `update` calcule ce qui se passe dans le jeu, s'occupe des événéments clavier
  etc.

## Que devons nous dessiner ?

La fonction `draw` du snake est très simple, on doit :

1. vider l'écran
2. dessiner la nourriture
3. dessiner snake

## Que devons-nous mettre à jour ?

On devra :

1. détecter s'il a mangé;
2. faire avancer le serpent (en le faisant grandir s'il a mangé);
3. détecter s'il est mort;
4. détecter s'il a gagné;
5. gérer les changements de direction du joueur;

# snake_00 : débuter

C'est votre point de départ.

**A faire 0**

1. Récupérez le fichier [snake_00](snake_00.py) et enregistrez le.

2. Renommez ce fichier en `snake.py` et ouvrez le dans **sublime text**.

3. Exécutez le depuis sublime text avec CTRL+B (si nécessaire choisissez python3)

---

Une fenêtre apparaît, elle contient une grille de taille $8\times 6$.

Sa dimension est $8 \times 60$ pixels de large et $6 \times 60$ pixels de haut.

Chaque case de cette grille est une position possible pour les éléments du
serpent.


Vous pouvez fermer la fenêtre en cliquant sur la croix. Cela arrête le
programme.

~~~python
import pgzrun
from random import randint


def init_snake():
    return [[3, 0], [2, 0], [1, 0]]


def init_direction():
    return [1, 0]


def init_food():
    return [7, 0]


def draw():
    draw_grid()
    pass


def draw_grid():
    for i in range(WIDTH_BOX):
        for j in range(HEIGHT_BOX):
            r = Rect((i * CASE, j * CASE), (CASE, CASE))
            screen.draw.rect(r, 'WHITE')


def update():
    pass


# globals
count = 0
snake = init_snake()
food = init_food()
direction = init_direction()

# constants
CASE = 60
WIDTH_BOX = 8
HEIGHT_BOX = 6
MAX_SNAKE = WIDTH_BOX * HEIGHT_BOX
WIDTH = WIDTH_BOX * CASE
HEIGHT = HEIGHT_BOX * CASE

pgzrun.go()
~~~

Examinons ce code en détail.

* Ligne 1 et 2 on importe la librairie `pgzrun` (pgzero) et la fonction `randint`
    Cette fonction servira lors du choix aléatoire de la position de la
    nourriture.

* Ensuite trois fonctions font sensiblement le même travail :
  * `init_snake` renvoie le serpent de départ.
  * `init_direction` renvoie la direction de départ. Si on la voit comme un
    _vecteur_, alors on va vers la droite (1 sur les _x_, 0 sur les _y_).
  * `init_food` renvoie la case intiale de la nourriture.

* Revenons sur le serpent. Dans le code, il est stocké dans une _liste_ Python.

    Elle est appelée `snake` et contient des coordonnées de case.

    **La première coordonnée est toujours la tête.**

    Ensuite viennent les éléments de corps. Il serait _plus efficace_ de faire
    le contraire mais on s'en moque. Faisons _simple_.

    `[[3, 0], [2, 0], [1, 0]]` : la tête est en `[3, 0]`, le corps est sur sa
    gauche.

    Reprenons : `snake` est une _liste_ qui contient des _listes_ de 2 nombres.

    Par exemple `[3, 0]` : la tête est à la ligne 0 (la première), colonne 4
    (la quatrième).

* Ensuite on a la fonction `draw` et la fonction `draw_grid`

  `draw` appelle `draw_grid` et `draw_grid` contient une double boucle imbriquée.

  Sans entrer dans le détail maintenant, `draw_grid` dessine la grille que vous
  avez à l'écran.

  Chaque case est un carré dont on ne dessine que le bord en blanc.
  On pourrait être beaucoup plus efficace, mais autant que ce soit simple, à
  nouveau.

  Pour chaque ligne et chaque colonne (donc pour chaque case) :

    * on crée un objet rect avec `r = Rect(...)` : un rectangle.

      il a deux paramètres, le premier est la position de coin supérieur gauche.
      le second est un couple (largeur, hauteur), ici `(CASE, CASE)`

      On peut voir en bas du code que `CASE` vaut 60.
    * on dessine ce rectangle avec `screen.draw.rect(r, 'WHITE')`

      `screen` désigne l'écran, `draw` pour dessiner dedans, `rect` parce qu'on
      va dessiner un rectangle.

* La dernière fonction est `update`. Pour l'instant elle ne fait rien : `pass`

* Ensuite on a des variables qui seront "globales". Elle seront modifiées par
  les fonctions. C'est généralement une _mauvaise pratique_ mais on s'en moque.
  Ça fonctionne et c'est simple.

  On trouve :

  * `count`, un compteur de frame. pgzero calcule 60 images (frames) par
  secondes. Si le serpent avançait d'une case à chaque fois, le jeu serait
  injouable. Il va avancer toutes les 20 frames et on va compter les frames
  dans `count`.

  * `snake` qui est initialisé avec notre fonction crée plus haut.
  * même chose pour `food` et `direction`.

* Ensuite on a des constantes, nommées en majuscule. Ce sont des variables
  dont la valeur ne changera jamais durant l'exécution du jeu. Les nommer en
  majuscule permet de les repérer plus facilement.

  On a :
  * `CASE = 60` : à l'écran, chaque case fait 60 pixels sur 60 pixels.
  * `WIDTH_BOX = 8` : 8 cases possibles par ligne.
  * `HEIGHT_BOX = 6` : 6 cases possibles par colonne.
  * `MAX_SNAKE` : la taille maximale que le serpent peut avoir. Pour savoir
    si on a gagné la partie !
  * `WIDTH` et `HEIGHT` qui sont les dimensions de la fenêtre.

Et enfin, on lance le jeu avec `pgzrun.go()`

# snake_01 : dessiner le serpent

Nous allons dessiner le serpent.

Sa tête est jaune, son corps est vert.

La taille du serpent va varier durant la partie. Il nous faut donc :

1. une boucle qui parcourt le corps. À chaque étape :
    elle crée un objet `Rect` et le dessine
2. dessiner la tête à part.

N'oublions pas un grand principe des jeux vidéos,
**il faut vider l'écran à chaque frame.**


**À faire 1.**

1. Modifier comme ceci la fonction `draw`:

  ~~~python
  def draw():
      screen.fill('BLACK')
      draw_grid()
      draw_snake()
  ~~~

2. Créer une fonction `draw_snake()` qui contient une boucle :

  ~~~python
  def draw_snake():
      for elt in snake[1:]:
        ...
  ~~~

  Dans cette boucle nous allons faire 3 choses :

  1. créer un élément rect correspondant à la case.
  2. dessiner le fond de la case en vert
  3. dessiner le bord de la case en noir

  ~~~python
  def draw_snake():
      for elt in snake[1:]:
          elt_rect = Rect((CASE * elt[0], CASE * elt[1]), (CASE, CASE))
          screen.draw.filled_rect(elt_rect, 'GREEN')
          screen.draw.rect(elt_rect, 'BLACK')
  ~~~

  Testez votre code. Vous devriez voir les 2 elements de corps en vert
  apparaître sur la grille.

**À faire 2.**

Ajouter dans `draw_snake` (en dehors de la boucle)
de quoi dessiner la tête en jaune.

Il faut commencer par récupérer la tête avec

~~~python
head = snake[0]
...
~~~


Lorsque vous testez, vous devriez voir la tête apparaître devant le corps.

[snake_01](snake_01.py)

# snake_02 : dessiner la bouffe

Nous allons dessiner la nourriture.

**A faire 3.**

Créer une fonction `draw_food` reprenant le même principe que le dessin
de la tête. Utiliser la couleur rouge : `'RED'`.

Ajouter un appel à cette fonction dans `draw`, entre `draw_grid` et `draw_snake`

[snake_02](snake_02.py)

## snake 03 : avancer le serpent

Nous allons faire avancer le serpent.

Il se déplace comme une chenille.

* A chaque étape, tous les élément du corps sont _immobiles_.
* une nouvelle tête est calculée et ajoutée en première position du tableau `snake`.
* l'élément de queue est supprimé.

~~~
étape 0 :

_QCCCT___

étape 1 :

__QCCCT__

étape 2 :

___QCCCT_
~~~

**À faire 4.**

1. Modifier `update`

  ~~~python
  def update():
      global count, snake, food, direction
      if count == 20:
          count = 0
          snake = move_snake(snake)

      count += 1
  ~~~

  Cette fonction va modifier différentes variables globales, on lui indique
  avec `global count, snake, food, direction`

  On remarque le compteur. En bas de la fonction, il augmente de 1.

  En haut de la fonction on vérifie s'il vaut 20...

  Et, si c'est le cas,

  * on le remet à 0
  * on avance le serpent avec `move_snake`

  2. Ajouter la fonction `move_snake`

  ~~~python
  def move_snake(snake):
      del snake[-1]
      return [calc_head()] + snake
  ~~~

  * On efface la queue (le dernier élément est celui d'indice `-1`)
  * On renvoie une nouvelle liste en mettant boût à boût une liste contenant
    la nouvelle tête et l'ancien corps

  3. Ajouter la fonction `calc_head`

  ~~~python
  def calc_head():
      tete = snake[0]
      return [tete[0] + direction[0], tete[1] + direction[1]]
  ~~~

  On calcule la nouvelle tête en ajoutant la direction (pour l'instant à droite)

  Notre serpent se déplace vers la droite et sort de l'écran sans mourir.

  Il avance indéfiniment...


[snake_03](snake_03.py)

## snake 04 : diriger le serpent

C'est une étape importante.

**À faire 5.**

Dans `update`, tout en bas, ajouter un appel à la fonction `check_keys()`

~~~python
def update():

    ...

    count += 1
    check_keys()
~~~

**À faire 6.**

Pour déplacer le serpent on doit déjà comprendre le principe suivant :

il ne peut pas tourner à 180°, sans quoi il serait mort immédiatement !

S'il va à gauche, on doit donc l'empêcher de tourner vers la droite etc.

Créer une fonction `check_keys`

~~~python
def check_keys():
    global direction
    if keyboard.down and direction in ([1, 0], [-1, 0]):
          direction = [0, 1]
~~~

Dans cette fonction, on commence par rendre globale la variable direction.

Nous allons modifier cette variable si une touche du clavier est pressée.

On sait qu'une touche est pressée parce que l'attribut `keyboard` contient
beaucoup de variables correspondant à chaque touche du clavier.

Ainsi `keyboard.down` est une variable qui vaut `True` si le joueur appuie sur
la touche "BAS" des flêches du clavier.

Elle vaut `False` sinon.

Donc le test `if keyboard.down ...` est vérifié si le joueur appuie sur bas.

Ensuite on s'assure qu'on a le droit de tourner avec
`and direction in ([1, 0], [-1, 0])`

Ces directions sont respectivement à droite et à gauche.

**À faire 7.**

Compléter la fonction `check_keys` en ajoutant trois autres tests, pour les
directions manquantes.

Il suffit de copier les deux dernières lignes trois fois et de les modifier.

Vous devriez pouvoir déplacer le serpent.

Il sort toujours de l'écran.

[snake_04](snake_04.py)

# snake_05 : mourir

Le serpent peut mourir de deux manières : s'il sort de l'écran ou s'il se mange.

S'il meurt on décide qu'il va revivre immédiatement mais avec la position
initiale. Cela évite de recharger la fenêtre et rend le jeu plus dynamique.

**À faire 8.**

Ajouter une fonction `is_dead`

~~~python
def is_dead(snake):
    head = snake[0]
    if head[0] < 0 or head[0] >= WIDTH_BOX:
        return True



    if head in snake[1:]:
        return True
    return False
~~~

Elle renvoie `True` si le serpent est mort, `False` sinon.


Ici on teste deux choses : si le serpent sort par la droite ou la gauche et
s'il se mord.

Compléter cette fonction en ajoutant la sortie par le haut et le bas au milieu
de la fonction.

**À faire 9**

Ajouter un appel à cette fonction dans update et la réintialisation du serpent

~~~python
def update():
    global count, snake, food, direction
    if count == 20:
        count = 0
        snake = move_snake(snake)

        game_over = is_dead(snake)
        if game_over:
            snake = init_snake()
            food = init_food()
            direction = init_direction()

    count += 1
    check_keys()
~~~

A cette étape, on meurt normalement.

Il est presque impossible que le serpent se morde vu qu'il ne peut
encore grandir...

C'est la prochaine étape !

[snake_05](snake_05.py)


# snake_06 : manger et grandir pour devenir fort

À l'heure actuelle, le serpent traverse la nourriture sans réagir.


Cette étape est un peu délicate car il faudra faire réapparaitre la nourriture
une fois celle-ci. Problème : celle-ci doit ne peut apparaître dans le serpent.

L'approche logique serait de choisir parmi les cases restantes.
Cela demande un effort supplémentaire de programmation que nous allons éviter
afin de simplifier ce tutoriel.

On se contente de choisir des cases au hasard et de recommencer
tant qu'on est dans le serpent.

Cet algorithme est de moins en moins efficace au fur et à mesure que
le serpent remplit la grille... mais tant qu'il reste une case vide, il va
se terminer très vite.

Commençons pas détecter la nourriture.

**À faire 10**

Dans la fonction `update`, ajouter les nouvelles lignes :

~~~python
def update():
    global count, snake, food, direction
        ...
        if game_over:
            snake = init_snake()
            food = init_food()
            direction = init_direction()

        eat = (snake[0] == food)
        if eat:
            food = random_food()

    count += 1
    check_keys()
~~~

Faites bien attention à l'_indentation_, la variable `eat` est dans le test
`if count==20:`

Le contenu de cette variable est un _booléen_, c'est à dire le résultat d'une
comparaison qui renvoie Vrai (`True`) ou Faux (`False`).

Ajouter ensuite la fonction `random_food` :

~~~python

def random_food():
    x = snake[0][0]
    y = snake[0][1]
    while [x, y] in snake:
        x = randint(0, WIDTH_BOX - 1)
        y = randint(0, HEIGHT_BOX - 1)
    return [x, y]
~~~

Découpons cette fonction pour comprendre ce qu'elle fait :

On commence par définir deux variables `x` et `y`. Ce sont l'absisse et
l'ordonnée de la tête.

Ensuite on réalise une boucle qui s'arrête dès que `[x, y]` n'est plus dans la
liste `snake`.

Au départ, `[x, y]` désigne justement la tête et cette condition n'est pas
vérifiée.

À chaque fois on choisit au hasard deux nombres, `x` et `y` parmi les numéros
de colonne et de ligne à l'aide de la fonction `randint` qui choisit un entier
au hasard.

S'il y a une case vide dans la grille, on finira par tomber dessus et la boucle
va s'arrêter.

Ensuite on renvoie la liste `[x, y]` comme nouvelle position de la nourriture.

Si vous testez votre jeu à cette étape, la nourriture réapparait à une nouvelle
position vide à chaque étape mais le serpent ne grandit pas !

**À faire 11**

Modifier comme ceci la fonction `update`

~~~python
def update():
    global count, snake, food, direction
    if count == 20:
        count = 0

        game_over = is_dead(snake)
        if game_over:
            snake = init_snake()
            food = init_food()
            direction = init_direction()
        eat = (snake[0] == food)
        if eat:
            food = random_food()
        snake = move_snake(snake, eat=eat)

    count += 1
    check_keys()
~~~

Modifier comme ceci la fonction `move_snake`


~~~python
def move_snake(snake, eat=False):
    if not eat:
        del snake[-1]
    return [calc_head()] + snake
~~~

Cette fois on passe un second paramètre à la fonction `move_snake` : le résultat
de notre _booléen_ `eat`.

Si `eat` est `False`, le serpent n'a pas mangé et on efface toujours son dernier
élément.

**Si `eat` est `True`, le serpent a mangé et on n'efface pas son dernier élément.**

Vous pouvez vérifier, le serpent grandit maintenant.

[snake_06](snake_06.py)

# snake_07 : les finitions

Notre jeu cache un horrible bug.

Quand la partie est gagnée, c'est-à-dire quand il ne reste plus de case libre
pour la nourriture, la boucle qui cherche une case libre pour la nourriture
va tourner indéfiniement car il n'en existe plus...

Il faut empêcher ça.

Pour cela on ajoute un test AVANT d'aller cherche la nourriture.
Et, si la partie est finie, on réintialise le jeu et affiche un message.

On pourrait afficher du texte mais un message dans la console fera l'affaire.

**À faire 12**

~~~python
def update():
    global count, snake, food, direction
    if count % 20 == 0:
        count = 0
        victory = (len(snake) == MAX_SNAKE)
        if victory:
            print("WIN !")
        game_over = is_dead(snake) or victory
        if game_over:
            snake = init_snake()
            food = init_food()
            direction = init_direction()
        eat = (snake[0] == food)
        if eat:
            # print("eat")
            food = random_food()
        snake = move_snake(snake, eat=eat)

    count += 1
    check_keys()
~~~

[snake_07](snake_07.py)

# Extensions

Le jeu est maintenant terminé. Il est jouable, les fonctionnalités de base
sont incluses et il ne comporte pas de bug.

On peut considérablement l'améliorer en proposant, par exemple

* d'améliorer les graphisme. On pourra utiliser des sprites avec la fonction
    `actor` de pygame zero.
* de faire varier la difficulté, en modifiant le rythme auquel le serpent avance.
    Il suffit de jouer sur la valeur à laquelle on réintialise `count`.
    On a choisit de faire monter `count` jusque 20 (60/20 = 3 mouvements par
    seconde), mais on peut diminuer la difficulté en le passant à 30
    (2 mouvements par seconde) etc.

* d'intégrer des textes, "bravo" tous les 10 éléments, "victoire", "game over".
    `pygame zero` propose des fonctions pour cela.

* De changer le titre de la fenêtre : `TITLE="Snake"` serait un bon début...

* De mettre le jeu en pause après chaque mort. Il faut presser une touche pour
    redémarrer

etc.

# Conclusion

Ce tutoriel est maintenant terminé. Vous avez appris à créer un jeu vidéo en
partant de très peu d'éléments avec la librairie pygame zero.

Bien sûr, snake est un jeu très simple. Mais d'un point de vue de pure
programmation il comporte déjà une grande majorité des éléments qui font un bon
jeu en 2D.

Vous pourriez essayer "pong", "timberman" ou un jeu de plateforme à la mario,

Pour les plus dégourdis : "tetris" est envisageable.

Ou alors... **space invaders** !
