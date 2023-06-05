import sys

arrayObstacles = sys.argv[1].split(',')
minimumJump = 1
noJumped = True

while noJumped:
    minimumJump += 1
    noJumped = False
    for index in range(len(arrayObstacles)):
        if int(arrayObstacles[index]) % minimumJump == 0:
            noJumped = True
            break

print('\nThe minimum jump to avoid all obstacles is:  %d' % (minimumJump))