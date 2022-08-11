# BinarySearch.py

# 常规版




# 函数版
def binary_contains(gene, key_codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:  # while there is still a search space
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

A = [41, 54, 95, 32, 11, 5, 7, 10, 21, 9, 85, 12, 13, 15, 64, 84]
my_A = sorted(A)
print(binary_contains(my_A, 21))

my_gene = ['cat', 'dog', 'fox', 'lion', 'acg', 'monkey', 'DNA']
my_sorted_gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, 'acg'))
