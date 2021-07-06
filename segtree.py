treeInput = [-1, 3, 4, 0, 2, 1]
segTree = [float('inf')] * (2**(3 + 1) - 1)

print(segTree)

def constructT(low, high, pos, tab):

    print(f'{tab} \tLow: {low}\t High: {high}\t Pos: {pos}')
    
    
    if low == high:
        segTree[pos] = treeInput[low]
        return

    if low > high:
        return

    mid = (low + high) // 2

    constructT(low, mid, 2 * pos + 1, tab + '\t')
    constructT(mid + 1, high, 2 * pos + 2, tab + '\t')

    segTree[pos] = min(segTree[ 2 * pos + 1 ], segTree[ 2 * pos + 2 ])

constructT(0, len(treeInput) - 1, 0, '')

print(segTree)



def minQuery(qL, qH, low, high, pos):
    print(f'minQuery({qL}, {qH}, {low}, {high}, {pos}')

    ## no overlap
    if qL > high or low > qH:
        return float('inf')

    ## full overlap
    if qL <= low and qH >= high:
        print(f'{qL} <= {low} and {qH} >= {high} ==> {segTree[pos]}')

        return segTree[pos]

    mid = (low + high) // 2

    return min(
        minQuery(qL, qH, low, mid, 2 * pos + 1),
        minQuery(qL, qH, mid + 1, high, 2 * pos + 2)
    )

print(minQuery(0, 3, 0, 4, 0))
