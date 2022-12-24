#Longest Common Prefix
def longestCommonPrefix(strs):
    # find minimum number of iteraion
    min_len = []
    for i in strs:
        min_len.append(len(strs))
    # find prefix
    prefix = ""
    k = 0
    for i in range(min(min_len)+1):
        collect = []
        for j in range(len(strs)):
            a = strs[k][i]
            k += 1
            collect.append(a)
        k = 0
        if len(set(collect)) == 1: #confirm it becomes prefix
            prefix += a
        else:
            break

    return prefix


print(longestCommonPrefix(['flow', 'flight', 'flower']))
