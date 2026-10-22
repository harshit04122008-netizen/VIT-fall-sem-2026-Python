import pandas as pd
L = list(map(str,input().split()))
voter_id = pd.Series(L)
print("Voter ID")
for idx , val in enumerate(voter_id):
    print(f"{idx}   {val}")