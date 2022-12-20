# Count all possible paths from top left to the bottom right of a M X N matrix

#recursive function
def paths(n,m):
    if n==1 or m==1:
        return 1
    return paths(n-1,m) + paths(n,m-1)

print(paths(2,5))
