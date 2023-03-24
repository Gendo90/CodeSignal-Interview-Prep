from string import ascii_lowercase

 
#works for small values - need to use dynamic programming to 
#prevent repeats
def solution(n, domain):
    all_vals = set()
    all_vals.add(domain)
    typo_len = 0
    
    last_vals = all_vals
    
    while(len(all_vals) - 1 <= n):
        typo_len += 1
        new_vals = set()
        for item in last_vals:
            new_vals.update(rightShift(item))
        if(new_vals.issubset(all_vals)):
            return -1
        last_vals = new_vals
        all_vals.update(new_vals)
        print(all_vals, typo_len) # may be commented out to remove possible typo domain names

    return typo_len - 1

def rightShift(txt):
    output = set()
    orig = txt.split(".")
    org_split = [[j for j in a] for a in orig]
    # print(orig, org_split)
    
    for l, arr in enumerate(org_split):
        for i in range(len(arr)-1):
            # print(i)
            curr = [a.copy() for a in org_split]
            curr[l][i], curr[l][i+1] = curr[l][i+1], curr[l][i]
            result = ["".join(a) for a in curr]
            fin_result = ".".join(result)
            output.add(fin_result)


    return output