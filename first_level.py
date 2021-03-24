''' ‘The cake is not a lie!’
===============
Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members of the Bunny Rebellion, and she beat her personal high score in Tetris. To celebrate, she’s ordered cake for everyone - even the lowliest of minions! But competition among minions is fierce, and if you don’t cut exactly equal slices of cake for everyone, you’ll get in big trouble.
The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.
To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).
Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

Test Cases
Your code should pass the following test cases. Note that it may also be run against hidden test cases not shown here.

Input: solution.solution("abcabcabcabc")
Output:4

Input:solution.solution("abccbaabccba")
Output: 2
'''


def solution(cake_string):
    index_second_piece = (cake_string * 2).find(cake_string, 1, -1)
    content_of_a_piece = cake_string[:index_second_piece]
    len_cake_str = len(cake_string)
    len_piece = len(content_of_a_piece)

    if len_cake_str == 1 or index_second_piece == -1:
        return 1
    elif 1 < len_cake_str < 200:
        number_of_pieces = int(len_cake_str / len_piece)
        leftovers = len_cake_str % len_piece
        if leftovers != 0:
            return 0
        else:
            return number_of_pieces
    else:
        return 0


# solution("abcabcabcabc")
# solution("23e23e23e23e23e23e23e")
# solution("aaaaaaa")
# solution("ababab")
# solution("abcabcabc")
# solution("a")
# solution('aaT')
# solution('ababT')
