def read_file(filename):
    with open(filename, "r") as file:
        counts = []
        for line in file:
            counts.append(int(line.strip()))
        return counts
    
    
def freq(counts):
    gts = [0] * 3
    for allele_count in counts:
        gts[allele_count] += 1
    for i in range(len(gts)):
        gts[i] /= len(counts)
    return gts


def gt_freq(filename):
    counts = read_file(filename)
    return freq(counts)

def hardy_weinberg(gt_freqs):
    assert len(gt_freqs) == 3, "Genotype frequency list should have 3 entries"
    
    p = (2*gt_freqs[2] +gt_freqs[1])/2
    q = 1 - p
    
    expected_freqs = [q**2, 2*p*q, p**2]
    
    for i in range(3):
        print("AC", i, "Expected", expected_freqs[i], "Actual", gt_freqs[i])