from random import *
from operator import *
from time import sleep
import random
#Αυτός παίρνει 0 πόντους και οι υπόλοιποι παίρνουν πόντους ανάλογα με την αξία των φύλλων τους
def points(score, hand, names):#Η score είναι λεξικό που αντιστοιχεί τους παίκτες στους πόντους τους
        """
        >>> hand,score={}, {}
        >>> names=["a","b"]
        >>> hand["a"]=[]
        >>> hand["b"]=[('10', '♣', 10), ('A', '♥', 11)]
        >>> score['a']=0
        >>> score['b']=10
        >>> points(score, hand, names)
        {'a': 0, 'b': 31}
        """
        for player in names:
            if len(hand[player]) != 0:
                sum_points = 0
                for rem_cards in hand[player]: #rem_cards metrhths
                    sum_points += rem_cards[-1]
                score[player] += sum_points
        return score #epistrefei enhmervmenous toys pontoys olwn tvn paiktwn


#Αν τελειώσουν τα φύλλα ενός παίχτη, τελειώνει η παρτίδα 
def check_hand(names ,hand):                            
    """

    ελέγχει αν έχουν τελειώσει τα φύλλα του παίχτη
    True: Game over
    False: The game goes on
    >>> hand={}
    >>> names=["a","b"]
    >>> hand["a"]=[]
    >>> hand["b"]=[('6', '♠', 6), ('6', '♣', 6)]
    >>> check_hand(names ,hand)
    True
    
    """
    
    i = 0
    for player in names :
        if len(hand[player]) == 0:
            i += 1 #metra posoi paiktes exoyn mhden fylla
    if i > 0:#αν δεν εχει εστω ενας φύλλα σταματά 
        return True
    else: #αν έχουν ολοι φύλλα συνεχίζει
        return False

#Το παιχνίδι συνεχίζεται ως ότου κάποιος πάρει πάνω από 50 πόντους
def check_points():
    """
    καλείται μετά το τέλος κάθε παρτίδας, κ ελέγχει αν έχει κανείς πάνω από 50 πόντους
    True: κάποιος έχει πάνω από 50 πόντους, Game over for good
    False: όλοι έχουν κάτω από 50 πόντους, επόμενη παρτίδα!
    """
    flag = False
    for player in names:     #ελέγχει το σκορ κάθε παίχτη
        if scores[player] > 50 : 
            flag = True
    return flag



#Αν τελιώσουν τα φύλλα της κλειστής τράπουλας τα φύλλα της ανοιχτής τράπουλας εκτός απο το ανοιχτό φύλλο, ανακατεύονατι και γίνονται η νέα κλειστή τράπουλα
def check_deck(deck, open_trapoul):
    """
    True: τελείωσαν τα φύλλα της κλειστή τράπουλας (deck)
    False: δεν τελείωσαν
    >>> deck=[('6', '♥', 6), ('3', '♠', 3), ('K', '♦', 10), ('Q', '♦', 10), ('J', '♥', 10), ('K', '♥', 10), ('6', '♣', 6), ('A', '♠', 11), ('10', '♦', 10), ('6', '♦', 6), ('2', '♥', 2), ('Q', '♣', 10), ('A', '♥', 11), ('7', '♦', 7), ('4', '♣', 4), ('A', '♦', 11), ('7', '♣', 7), ('9', '♣', 9), ('K', '♠', 10), ('10', '♠', 10), ('2', '♣', 2), ('7', '♠', 7), ('K', '♣', 10), ('5', '♦', 5), ('Q', '♠', 10), ('5', '♣', 5), ('9', '♠', 9), ('3', '♥', 3), ('8', '♣', 8), ('2', '♦', 2), ('6', '♠', 6), ('7', '♥', 7), ('Q', '♥', 10), ('J', '♦', 10), ('8', '♠', 8), ('10', '♣', 10), ('2', '♠', 2)]
    >>> open_trapoul=[('3', '♦', 3)]
    >>> check_deck(deck, open_trapoul)
    False
    >>> deck=[]
    >>> check_deck(deck, open_trapoul)
    True
    """
    if len(deck) == 0 :
        return True
    else:
        return False

#Αν υπάρχει ισοδυναμία το παιχνίδι συνεχίζεται
def isodynamia (draw, scores, deck, open_trapoula,num_players):
        """
        draw =λιστα με ονοματα που ισοβαθμουν
        scores=λεξικο με κλειδια τα ονοματα των παικτων και τιμες τους ποντους των παικτων αυτων
        deck=κλειστή τραπουλα 
        open_trapoula = η τράπουλα που βρίσκεται ανοικτη κατώ
        num_players=πλήθος παικτών που ισοβαθμούν 
        """
        del scores
        del deck
        del open_trapoula
        scores = {}
        draw.sort()     #ταξινομεί αλφαβητικά τα ονόματα των παιχτών
        for i in draw:
                scores[i] = 0 #μηδενίζει τα σκορ ολων των παικτών
        deck = []
        if num_players % 2 != 0 or num_players // 4 == 0: #βρίσκει πόσες τράπουλες χρειάζονται
            l = 1
        else:
            l = 0
        num_decks = num_players // 4 + l
        for i in range(num_decks):
            deck.extend(create_deck()) #δημιουργεί οσες τραπουλες χρειαζονται 
        deck, open_trapoula = deck[:-1], [deck[-1]] #τοποθετεί στην ανοικτή τράπουλα (κατω) το πρωτο φυλλο 
        partida(deck, scores, draw, open_trapoula) #καλεί την παρτίδα 

def matches(card1,card2): 
    """Κοιτάει να δει αν η card1 ταιριάζει με την card2 ως προς την σειρά ή το σύμβολο/αριθμό
    >>> c1,c2=('6', '♠', 6), ('6', '♣', 6)
    >>> matches(c1,c2)
    True
    >>> c1,c2=('Q', '♣', 10), ('J', '♠', 10)
    >>> matches(c1,c2)
    False
    >>> c1,c2=('Q', '♣', 10), ('J', '♠', 10)
    >>> matches(c1,c2)
    False
    """
    if card1[0] != 'A' :
        return True if ((card1[1] == card2[1]) or (card1[0] == card2[0])) else False
    else:
        return True if (card1[1] == card2[1] or card2[0]=='A') else False

#Φτιάχνουμε την τραπουλα
def create_deck():
    """creates a new deck
    >>> deck = create_deck()
    >>> choice([('4', '♥', 4), ('3', '♣', 3), ('10', '♥', 10), ('8', '♥', 8), ('4', '♦', 4), ('4', '♠', 4), ('9', '♥', 9), ('J', '♣', 10), ('J', '♠', 10), ('8', '♦', 8), ('A', '♣', 11), ('5', '♥', 5), ('9', '♦', 9), ('5', '♠', 5), ('3', '♦', 3), ('6', '♥', 6), ('3', '♠', 3), ('K', '♦', 10), ('Q', '♦', 10), ('J', '♥', 10), ('K', '♥', 10), ('6', '♣', 6), ('A', '♠', 11), ('10', '♦', 10), ('6', '♦', 6), ('2', '♥', 2), ('Q', '♣', 10), ('A', '♥', 11), ('7', '♦', 7), ('4', '♣', 4), ('A', '♦', 11), ('7', '♣', 7), ('9', '♣', 9), ('K', '♠', 10), ('10', '♠', 10), ('2', '♣', 2), ('7', '♠', 7), ('K', '♣', 10), ('5', '♦', 5), ('Q', '♠', 10), ('5', '♣', 5), ('9', '♠', 9), ('3', '♥', 3), ('8', '♣', 8), ('2', '♦', 2), ('6', '♠', 6), ('7', '♥', 7), ('Q', '♥', 10), ('J', '♦', 10), ('8', '♠', 8), ('10', '♣', 10), ('2', '♠', 2)]) in deck
    True
    >>> len(deck)
    52
    >>> ('4', '♦', 4) in deck
    True
    >>> ('8', '♦', 8) in deck
    True
    """
    #choice επιλεγει ενα τυχαιο στοιχειο απο μια δοσμενη λιστα
    deck = [] 
    symbols = {1:'A', 11:'J', 12:'Q', 13:'K', 15: '♥', 16:'♣', 17:'♦', 18:'♠'}
    for i in range(1,14):
        for j in range(15,19):
            deck.append((str(i) if i not in symbols else symbols[i], symbols[j],     i if (i>=2 and i<=10) else (11 if i==1 else 10)))
            #                 ..αριθμο----------------------------------, συμβολο.....,  πόντους που αξίζει το φυλλο ....................................
    shuffle(deck) #ανακατεύει τη τράπουλα 
    return deck


def play(player,open_trapoul,deck, hand, names, parasyte):
    """Εκτελεί τον κύκλο παιχνιδιού για τον παίκτη με την σειρά player, όπου στην αρχή του γύρου εμφανίζει τα φύλλα του παίκτη καθώς και το ανοιχτό φύλλο
        ελένχει αν ο παίκτης μπορεί να παίξει κάτι βάσει του ανοιχτού φύλλου και στην περίπτωση που αυτό δεν ισχύει τον ειδοποιει με μήνυμα και πηγάνει αυτόματα πάσο
        μετά περιμένει την επιλογή φύλλου από τον παίκτη και αν ταιριάζει με την σειρά ή τον αριθμό/φιγούρα του ανοιχτού φύλλου τότε το ανοιχτό φύλλο μπαίνει στην ανοιχτή στίβα
        και η επιλογή γίνεται το νέο ανοιχτό φύλλο
        player--integer
        hand=λεξικό που περιεχει λιστα  με τα φυλλα π εχει ο καθε παικτης στα χερια του με κλειδια τους παικτες
        parasyte = βοηθα στο να μπει ξανα ο σωστοσ ασσος στην ανοικτη τραπουλα
    """
    k=('A', parasyte, 11)
    phand = hand[names[player]]    #player hand τα φυλλα του δωσμενου παικτη
    print("On the table: ", open_trapoul[-1])
    print("Your hand, ", names[player], ", is: ", sep='')
    print(phand)
    options = False
    card = 0
    while options == False and card < len(phand):  #εξεταζει αν ο παικτης εχει φυλλο να παιξει
        if matches(phand[card], open_trapoul[-1]) == True or phand[card][0] == 'A':
            options = True
        card +=1
    if not options: #αμα δεν εχει φυλλο να ριξει που να ταιριαζει 
         print('Sorry %s, you have no available options'%(names[player]))
         sleep(2)
         if check_deck(deck, open_trapoul): #αν τελείωσαν τα φύλλα της κλειστής τράπουλας ανακατεύει τα φυλλα της ανοικτης τράπουλας και την κανει κλειστη (το τελευταιο φυλλο της ανοικτης τράπουλας παραμένει ανοικτό)
             deck, open_trapoul = open_trapoul[:-1], [open_trapoul[-1]]
             shuffle(deck)
         phand.append(tuple(deck[-1])) #τραβάει μια κάρτα
         deck.remove(deck[-1]) #το αφαιρεί απτην κλειστη τραπουλα το φυλλο που τράβηξε προηγουμένως ο παίκτης
    while options: #όταν εχει επιλογές
        choicee=int(input('%s, please choose your card (1-%s) or choose Pass (%s) '%(names[player],len(phand),len(phand)+1)))  
        #choicee=int(input('%s, please choose your card (1-%s) '%(names[player],len(phand) )))
        if choicee-1 in range(len(phand)+1):#choicee-1 γιατί οι λίστες ξεκινούν αρίθμηση από το 0, όχι από το 1
                if choicee != len(phand) + 1:#αν δεν επιλέξει να πάει πάσο
                        drops = phand[choicee-1] #το χαρτι που ρίχνει ο παικτης
                        if matches(drops, open_trapoul[-1]) or (drops[0] == 'A'): #ελεγχει αν μπορει ν ριξει το φυλλο που επιθυμει 
                            if parasyte!=None :  #αν η parasyte εχει καποια τιμη περα του none
                                open_trapoul[-1]=k #βάζουμε στην θέση του ασσου που αλλάξαμε τον παλιό ασσο ετσι ωστε να μην υπαρξει καποιο θεμα στην opentrapoul
                                parasyte=None 
                            phand.remove(drops) #ριχνει το φυλλο
                            open_trapoul.append(drops) #προστίθεται στην ανοικτη τραπουλα 
                            if drops[0] == 'A':  #αν επελεξε να ριξει ασσο
                                if len(open_trapoul)!=1 and open_trapoul[-1][0]=="A" :
                                    k=open_trapoul[-1] #κρατάει τον ασσο που μόλις εριξε ο παικτης σε ενα tuple
                                    print("You dropped an ace! You may change the symbol.")
                                    print ("Pick a symbol: \n 1. Hearts ♥ \n 2. Clubs ♣\n 3. Spades ♠ \n 4. Diamonds ♦ ")
                                    num = input() #διαλεγει τι θέλει να γίνει 
                                    while (num != "1" and num!="2" and num!="3" and num!="4"):
                                        print ("Pick a symbol: \n 1. Hearts ♥ \n 2. Clubs ♣\n 3. Spades ♠ \n 4. Diamonds ♦ ")
                                        num = input("You need to choose a number 1-4:")
                                    if num == "1":
                                            num = '♥'
                                    elif num == "2":
                                            num = '♣'
                                    elif num == "3":
                                            num = '♠'
                                    else:
                                            num = '♦'
                                    if check_hand(names ,hand)==True: #Αν πέσει τελευταίο φύλλο ασσος !
                                            continue 
                                    else:
                                            parasyte=open_trapoul[-1][1]  #κραταμε το γεγονος οτι αλλαξε το συμβολο θα το χρησιμοποιησουμε στην ιφ παραπανω
                                            open_trapoul[-1]=('A', num, 11) #αλλάζουμε το συμβολο του  πρώτου φυλλου  που βρίσκεται ανοικτο με το συμβολο που θέλησε ο παικτης 
                                    
                            return parasyte     #επιστρεφει το parasyte για επαναχρησιμοποιηση
                            break
                else: # αν επιλέξει πάσο
                        if check_deck(deck, open_trapoul) == True:#κοιτάει να δει αν υπάρχουν φύλλα στην τράπουλα
                                deck, open_trapoul = open_trapoul[:-1], [open_trapoul[-1]]
                                shuffle(deck)
                        phand.append(tuple(deck[-1]))#τραβάει ένα φύλλο
                        deck.remove(deck[-1])
                        return parasyte

                
def partida(deck, scores, names, open_trapoul):
            """
            names=λίστα με ονοματα
            """
            if check_deck(deck, open_trapoul): #αν τελείωσαν τα φύλλα της κλειστής τράπουλας ανακατεύει τα φυλλα της ανοικτης τράπουλας και την κανει κλειστη (το τελευταιο φυλλο της ανοικτης τράπουλας παραμένει ανοικτό)
                    deck, open_trapoul = open_trapoul[:-1], [open_trapoul[-1]]
            shuffle(deck) #ανακατευει την τραπουλα
            once9=0#για να σταματησει το χαρτί 9, ουσιαστικά μετράει πόσες φορές ήταν ανοιχτό στο ταμπλό το χαρτί 9
            warning9=0#για να πιάνεται η περίπτωση που πέφτει καινούργιο 9 πάνω σε 9
            warningcount9=0#τα συνεχομενα 9 που εχουν πεσει  το ένα πάνω στο άλλο
            once8=0#τα αντίστοιχα για το φύλλο 8
            warning8=0
            warningcount8=0
            once7=0#τα αντίστοιχα για το φύλλο 7
            warning7=0
            warningcount7=0
            parasyte=None
            #Μοιράζονται 7 φύλλα σε κάθε παίχτη
            hand = {}
            for i in names:
                temp = []
                for j in range(7): 
                    x = deck.pop()
                    temp.append(x)
                hand[i] = temp
            i = 0    #αριθμός παίχτη που παίζει
            while check_hand(names,hand) == False:   #οταν εχουν ολοι εστω ενα φυλλο στα ΧΕΡΙΑ τους
                parasyte=play(i, open_trapoul, deck, hand, names, parasyte) #για να διατηρηθει η τιμη της parasyte
                if open_trapoul[-1][0]!="7" :#όταν πεσει κατω κατι διάφορο του 7
                        once7=0
                        warning7=0 #παιρνει τιμες 0 και 1  
                        warningcount7=0 
                if open_trapoul[-1][0] == "7" and len (open_trapoul)!=1:#xarti 7
                        tempi=1#μετρητής
                        coun=0#μετρα ποσα 7ρια θα πεσουν το ενα πανω στο αλλο 
                        continuous=True#ελένχει να είναι συνεχόμενα τα 7ρια
                        while tempi<len(open_trapoul)-1 and continuous==True: #κοιταει να δει αν το 7 που επεσε ειναι καινουργιο ή οχι 
                                if  open_trapoul[-tempi][0]=="7": #κοιτα την ανοικτη τραπουλα μεχρι να μην υπαρχει 7 δηλαδη μετραει τα συνεχομενα 7ρια που ειναι ηδη κατω
                                       coun+=1
                                else:
                                        continuous=False
                                tempi+=1
                        if coun>warningcount7:#αν μέτρησε περισσότερα συνεχόμενα 7ρια από όσα ήταν πριν να ξέρει να προσέχει για καινούργιο 7ρι
                                warningcount7=coun
                                warning7=0#μας λεει οτι το 7 που ειναι κατω μολις επεσε
                        if open_trapoul[-2][0]=="7": 
                                warning7+=1
                        if warning7==1:
                                once7=0 #αν πατησει ο επομενος πασο να μην υπαρξει θεμα
                        if once7==0 :#θα εκτελέσει το φύλλο 7 μόνο την πρώτη φορά που θα βρει κάτω το χαρτί 7
                                print ("You have dropped a card 7. \nNext player has to draw 2 cards")
                                j = i+1#διαλέγει τον επόμενο παικτη
                                if j > len(names) - 1:
                                    j = j - len(names)
                                m=names[j]
                                tempor=[]
                                for  k in range(2):
                                        if check_deck(deck, open_trapoul) == True:#κοιτάει να δει αν μπορεί να τραβήξει ενα φύλλο
                                                deck, open_trapoul = open_trapoul[:-1], [open_trapoul[-1]]
                                                shuffle(deck)
                                        l=deck.pop()
                                        tempor.append(l)
                                hand[m].extend(tempor)
                                once7+=1
                if open_trapoul[-1][0]!="8" :#όταν δει ότι το φύλλο δεν είναι 8 θα σταματήσει να μετράει και θα ξαναμετρήσει απότην αρχή
                        once8=0
                        warning8=0
                        warningcount8=0
                if open_trapoul[-1][0]=="8"  and len(open_trapoul) != 1 : #xarti8
                        tempi=1#μετρητής
                        coun=0#μετράει το πόσα συνεχόμενα 8 μπορείνα πέσουν
                        continuous=True#ελέγχει να είναι συνεχόμενα τα 8ρια
                        while tempi<len(open_trapoul)-1 and continuous==True:
                                if  open_trapoul[-tempi][0]=="8":
                                       coun+=1
                                else:
                                        continuous=False
                                tempi+=1
                        if coun>warningcount8:#αν μέτρησε περισσότερα συνεχόμενα 8ρια από όσα ήταν πριν να ξέρει να προσέχει για καινούργιο 8ρι
                                warningcount8=coun
                                warning8=0#πρόσεχε για καινούργιο 8ρι
                        if open_trapoul[-2][0]=="8":
                                warning8+=1
                        if warning8==1:#πρόκειται για καινούργιο 8ρι ώστε να μην το παραλείψει
                                once8=0
                        if once8==0 :#θα εκτελέσει το φύλλο 8 μόνο την πρώτη φορά που θα βρει κάτω το χαρτί 8
                                print("You have dropped a card 8.\nSame player has to play again ")
                                phandwarningcount8 = hand[names[i]]
                                options = False
                                card = 0
                                while options == False and card < len(phandwarningcount8):
                                        if matches(open_trapoul[-1], phandwarningcount8[card]) == True or (phandwarningcount8[card] == 'A'):
                                                options = True
                                        card +=1
                                if options == True and card > 0:
                                        once8+=1
                                        continue
                                
                                if not options: #αν δεν εχει φυλλο να ριξει 
                                        print('Sorry %s, you have no available options'%(names[i]))
                                        if check_deck(deck, open_trapoul): #αν τελείωσαν τα φύλλα της κλειστής τράπουλας ανακατευει αυτα της ανοικτης εκτος απο το πανω πανω 
                                             deck, open_trapoul = open_trapoul[:-1], [open_trapoul[-1]]
                                             shuffle(deck)
                                        hand[names[i]].append(tuple(deck[-1]))
                                        deck.remove(deck[-1])
                                        sleep(2)
                        once8+=1
                                
                if open_trapoul[-1][0]!="9" :#όταν δει ότι το φύλλο δεν είναι 9 θα σταματήσει να μετράει και θα ξαναμετρήσει απότην αρχή
                        once9=0
                        warning9=0
                        warningcount9=0
                if open_trapoul[-1][0]=="9" and len(open_trapoul)!=1: #xarti 9
                        tempi=1#μετρητής
                        coun=0#μετράει το πόσα συνεχόμενα 9 μπορείνα πέσουν
                        continuous=True#ελένχει να είναι συνεχόμενα τα 9ρια
                        while tempi<len(open_trapoul)-1 and continuous==True:
                                if  open_trapoul[-tempi][0]=="9":
                                       coun+=1
                                else:
                                        continuous=False
                                tempi+=1
                        if coun>warningcount9:#αν μέτρησε περισσότερα συνεχόμενα 9ρια από όσα ήταν πριν να ξέρει να προσέχει για καινούργιο 9ρι
                                warningcount9=coun
                                warning9=0#πρόσεχε για καινούργιο 9ρι
                        if open_trapoul[-2][0]=="9":
                                warning9+=1
                        if warning9==1:#πρόκειται για καινούργιο 9ρι ώστε να μην το παραλείψει
                                once9=0
                        if once9==0 :#θα εκτελέσει το φύλλο 9 μόνο την πρώτη φορά που θα βρει κάτω το χαρτί 9
                                i +=2
                                print("You have dropped a card 9.\nSorry, the next player in row may not play")
                                if i > len(names) - 1:
                                        i = i - len(names)
                                print('-'* 20)
                                phand = hand[names[i]]
                                options = False
                                card = 0
                                while options == False and card < len(phand):
                                                if check_hand(names,hand) != True :
                                                        if matches(open_trapoul[-1], phand[card]) == True or (phand[card][0] == 'A'):
                                                                options = True
                                                card +=1
                                if card>0 and options==True :
                                        once9+=1
                                        continue #μαυτο παει στην πανω πανω while
                    
                                if not options:
                                        print('Sorry %s, you have no available options'%(names[i]))
                                        if check_deck(deck, open_trapoul): #αν τελείωσαν τα φύλλα της κλειστής τράπουλας
                                             deck, open_trapoul = open_trapoul[:-1], [open_trapoul[-1]]
                                             shuffle(deck)
                                        phand.append(tuple(deck[-1]))
                                        deck.remove(deck[-1])
                                        sleep(2)
                        once9+=1#μετράει πόσες φορές συνεχόμενα έχει δει κάτω το χαρτί 9 
                i += 1
                if i > len(names) - 1: #αν μόλις έπαιξε ο τελευταίος,
                    i = i - len(names)  #η σειρά πάει από την αρχή
                print('-'* 20) 
                #points (scores, hand, names)
            if check_hand(names,hand) == True:
                points (scores, hand, names)
                if check_points()==True:        #αν τελειωσαν τα φυλλα καποιου
                        minn = scores[names[0]] 
                        winner = names[0]
                        for k in names:
                                if scores[k] < minn:
                                        minn = scores[k]
                                        winner = k
                        n = 0
                        for k in names:
                                if scores[k] == minn:
                                        n = n + 1
                        if n == 1:
                                print ("Winner is " , winner)
                                f = False #δεν υπαρχει ισοδυναμια δηλαδη 
                        else:
                                draw = [] 
                                for k in names:
                                        if scores[k] == minn:
                                                draw.append(k) #βαζουμε στη λιδτα αυτη τα ονομα οσων εχουν ισοπαλια για την πρωτη θεση
                                print ("There's been a draw between: ")
                                for k in draw:
                                    print(k)
                                print('-'*20)
                                del names
                                names = draw[:]
                                isodynamia(names, scores, deck, open_trapoul,n)
                                       
#Ζητάει αριθμό παιχτών και ονόματα
num_players = int(input("How many players? "))
names = []
for i in range(num_players):
    names.append(input("Player %s: what is your name? "%(i+1)))
names.sort() #ταξινομει αλφαβητικα την names
#Ελέγχει κ προσθέτει όσες τράπουλες χρείαζονται
#ανάλογα με τον αριθμό των παιχτών
deck = []
if num_players % 2 != 0 or num_players // 4 == 0:
    l = 1
else:
    l = 0
num_decks = num_players // 4 + l
for i in range(num_decks):
    deck.extend(create_deck())
deck, open_trapoul = deck[:-1], [deck[-1]] # βαζει ενα φυλλο ανοικτο
scores = {} #αρχικοποιει την scores
for i in names:
    scores[i] = 0
f = True #f isodynamias
while check_points()==False and f==True:
            """
            δεν έχει κανείς πάνω από 50 πόντους και
            δεν έχει ισοδυναμία
            """
            if check_deck(deck, open_trapoul): #αν τελείωσαν τα φύλλα της κλειστής τράπουλας
                                             deck, open_trapoul = open_trapoul[:-1], [open_trapoul[-1]]
                                             shuffle(deck)
            partida(deck, scores, names, open_trapoul)

