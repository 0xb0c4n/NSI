def hamming(sr, sr2):
    gd_mot = sr if len(sr) < len(sr2) else sr2
    n = abs(len(sr)-len(sr2))
    for i in range(len(gd_mot)):
        if sr[i] != sr2[i]:
            n +=1
    return n
