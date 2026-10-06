def wordBreak(s, dict_list):
    memo = {}
    def backtrack(idx):
        if idx in memo:
            return memo[idx]
        if idx == len(s):
            return [[]]
        res = []
        for word in dict_list:
            if s.startswith(word,idx):
                sub_results = backtrack(idx + len(word))
                for sub in sub_results:
                    res.append([word]+sub)
        memo[idx] = res
        return res
    return backtrack(0)
   
def print_segmentations(result):
    for seg in result:
        print(" ".join(seg))

def print_segmentation_stats(result):
    print(f"Total segmentations: {len(result)}")
    if not result:
        return
    shortest = min(result , key = len)
    print(f"Shortest segmentation: {' '.join(shortest)}")
   
    longest = min(result , key = len)
    print(f"Longest segmentation: {' '.join(longest)}")

def main():
    s = input().strip()
    n = int(input().strip())
    dict_list = input().split()
   
    result = wordBreak(s, dict_list)
   
    print_segmentations(result)
    print_segmentation_stats(result)

if __name__ == '__main__':
    main()