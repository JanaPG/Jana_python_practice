'''1. Tracking Poker Rounds
Elyse is especially fond of poker, and wants to track how many rounds she plays - and which rounds those are. Every round has its own number, and every table shows the round number currently being played. Elyse chooses a table and sits down to play her first round. She plans on playing three rounds.

Implement a function get_rounds(<round_number>) that takes the current round number and returns a single list with that round and the next two that are coming up:

>>> get_rounds(27)
[27, 28, 29]
'''

def get_rounds(round_number):
    return [round_number,round_number+1,round_number+2]

print(get_rounds(-5.5))

'''2. Keeping all Rounds in the Same Place
Elyse played a few rounds at the first table, then took a break and played some more rounds at a second table ...
 but ended up with a different list for each table! She wants to put the two lists together, 
 so she can track all of the poker rounds in the same place.

Implement a function concatenate_rounds(<rounds_1>, <rounds_2>) that takes two lists and returns 
a single list consisting of all the rounds in the first list, followed by all the rounds in the second list:'''

def concatenate_rounds(list1,list2):
    return(list1+list2)

print(concatenate_rounds([5,6],[9,11]))

'''3. Finding Prior Rounds
Talking about some of the prior Poker rounds, another player remarks how similarly two of them played out. Elyse is not sure if she played those rounds or not.

Implement a function list_contains_round(<rounds>, <round_number>) that takes two arguments, a list of rounds played and a round number. The function will return True if the round is in the list of rounds played, False if not:

>>> list_contains_round([27, 28, 29, 35, 36], 29)
True

>>> list_contains_round([27, 28, 29, 35, 36], 30)
False'''

def list_contains_round(list1,list2):
    for item in list1:
        if item==list2:
            return True
    return False

print(list_contains_round([50,60,70],700))

'''4. Averaging Card Values
Elyse wants to try out a new game called Black Joe. It's similar to Black Jack - where your goal is to have the cards in your hand add up to a target value - but in Black Joe the goal is to get the average of the card values to be 7. The average can be found by summing up all the card values and then dividing that sum by the number of cards in the hand.

Implement a function card_average(<hand>) that will return the average value of a hand of Black Joe.

>>> card_average([5, 6, 7])
6.0'''

def card_average(list1):
    return(sum(list1)/len(list1))



def approx_average_is_average(hand):
    print('actual average: '+str(card_average(hand)))
    print('first last average: '+ str((hand[0]+hand[-1])/2))
    print(int(((len(hand) - 1)/2)))
    #print('median average: '+str(hand[((len(hand)-1)/2)]))
    if card_average(hand)==(hand[0]+hand[-1])/2:
        return True
    elif card_average(hand)==(hand[int(((len(hand) - 1)/2))]):
        return True 
    else:
        return False 


print(approx_average_is_average([1, 2, 4]))


print(card_average([0,0,100]))


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    even_sum=0
    even_count=0
    odd_sum=0
    odd_count=0
    count=0
    for item in hand:
        if count%2==0:
            even_sum=even_sum+item
            even_count+=1
            count+=1
        else:
            odd_sum=odd_sum+item
            odd_count+=1
            count+=1
    odd_avg=odd_sum/odd_count
    even_avg=even_sum/even_count
    print(odd_sum)
    print(odd_count)
    print(even_sum)
    print(even_count)
    if odd_avg==even_avg:
        return True
    else:
        return False
    

print(average_even_is_average_odd([1,2,3]))