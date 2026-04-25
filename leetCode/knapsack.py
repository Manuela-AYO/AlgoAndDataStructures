def v1(totalBandwith: int, bandwiths: list[int], requests: list[int]):
    """
    Drawback: Use more space than i need. 
    Space & time Complexity: O(len(bandwiths)*totalBandwith)
    """
    m = [ [ 0 for _ in range(totalBandwith+1) ] for _ in range(len(bandwiths)+1) ]

    n = len(bandwiths) + 1

    for i in range(1, n):
        for j in range(1, totalBandwith+1):
            if bandwiths[i-1] <= j:
                currentBandwith = bandwiths[i-1]
                m[i][j] = max(m[i-1][j], m[i-1][j-currentBandwith] + requests[i-1])
            else:
                m[i][j] = m[i-1][j]

    return m[n-1][totalBandwith]


def v2(totalBandwith: int, bandwiths: list[int], requests: list[int]):
    """
    Space Complexity: O(totalBandwith)
    Time Complexity: O(len(bandwiths)*totalBandwith)
    """
    m = [ [ 0 for _ in range(totalBandwith+1) ] for _ in range(2) ]
    
    n = len(bandwiths) + 1

    for i in range(1, n):
        for j in range(1, totalBandwith+1):
            if bandwiths[i-1] <= j:
                currentBandwith = bandwiths[i-1]
                m[1][j] = max(m[0][j], m[0][j-currentBandwith] + requests[i-1])
            else:
                m[1][j] = m[0][j]
        m[0] = m[1].copy()
    return m[1][totalBandwith]


def v3(totalBandwith: int, bandwiths: list[int], requests: list[int]):
    """
    Last optimization
    """
    m = [0] * ( totalBandwith + 1 )
    n = len(bandwiths)

    for i in range(n):
        for j in range(totalBandwith, bandwiths[i]-1, -1):
            m[j] = max(m[j], m[j-bandwiths[i]] + requests[i])
        print(m)
    return m[totalBandwith]

#val = v3(500, [200, 100, 350, 50, 100], [270, 142, 450, 124, 189])
val = v3(10, [4, 2, 5, 4], [8, 3, 20, 13])
print(val)
