# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a step shape
# with N levels using the # character.  Make sure the
# step has spaces on the right hand side!
# --- Examples
# steps(2)
  # '# '
  # '##'
# steps(3)
  # '#  '
  # '## '
  # '###'
# steps(4)
  # '#   '
  # '##  '
  # '### '
  # '####'

def steps(n, rows = 0, stair=''):
    if (n == rows):
        return;
    if(len(stair) == n):
        print(stair)
        return steps(n, rows + 1)
    if(len(stair) <= rows):
        stair = stair + '#'
    else:
        stair = stair + ' '
    return steps(n, rows, stair)


# def steps(n):
#     rows = 0;
#     while(rows < n):
#         stair = ''
#         columns = 0
#         while(columns < n):
#             if(columns <= rows):
#                 stair = stair + '#'
#             else:
#                 stair = stair + ' '
#             columns = columns + 1
#         rows = rows + 1
#         print(stair)

steps(2)
steps(3)
steps(4)
