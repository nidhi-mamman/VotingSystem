import pandas as pd
from pathlib import Path

# path = Path("C:/Users/Desktop/Sem-5/CS301 CN/Project/Voting/database")
path = Path("database")

def count_reset():
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    for index, row in df.iterrows():
        df.loc[index, 'hasVoted'] = 0
    df.to_csv(path/'voterList.csv')

    df=pd.read_csv(path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    for index, row in df.iterrows():
       df.loc[index, 'Vote Count'] = 0
    df.to_csv (path/'cand_list.csv')


def reset_voter_list():
    df = pd.DataFrame(columns=['voter_id','Name','Gender','Zone','City','Passw','hasVoted'])
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    df.to_csv(path/'voterList.csv')

# def reset_cand_list():
#     df = pd.DataFrame(columns=['Sign','Name','Vote Count'])
#     df=df[['Sign','Name','Vote Count']]
#     df.to_csv(path/'cand_list.csv')


def verify(vid,passw):
    df=pd.read_csv(path/'voterList.csv')
    df['Passw'] = df['Passw'].astype(str).str.strip()
    match = df[(df['voter_id'] == vid) & (df['Passw'] == passw)]
    return not match.empty


def isEligible(vid):
    df=pd.read_csv(path/'voterList.csv')
    match = df[(df['voter_id'] == vid) & (df['hasVoted'] == 0)]
    return not match.empty


def vote_update(st,vid):
    if isEligible(vid):
        df=pd.read_csv (path/'cand_list.csv')
        df=df[['Sign','Name','Vote Count']]
        for index, row in df.iterrows():
            if df.loc[index, 'Sign'] == st:
                df.loc[index, 'Vote Count'] += 1
        df.to_csv (path/'cand_list.csv')

        df=pd.read_csv(path/'voterList.csv')
        df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
        for index, row in df.iterrows():
            if df.loc[index, 'voter_id'] == vid:
                df.loc[index, 'hasVoted'] = 1
        df.to_csv(path/'voterList.csv')

        return True
    return False


def show_result():
    df=pd.read_csv (path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    v_cnt = {}
    for index, row in df.iterrows():
        v_cnt[df['Sign'].iloc[index]] = df['Vote Count'].iloc[index]
    # print(v_cnt)
    return v_cnt


def taking_data_voter(name,gender,zone,city,passw):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    
    duplicate = df[
        (df['Name'].str.strip().str.lower() == name.strip().lower()) &
        (df['Gender'].str.lower() == gender.lower()) &
        (df['Zone'].str.strip().str.lower() == zone.strip().lower()) &
        (df['City'].str.strip().str.lower() == city.strip().lower())
    ]

    if not duplicate.empty:
        return -1  

    row,col=df.shape
    if row==0:
        vid = 10001
        df = pd.DataFrame({"voter_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "hasVoted":[0]},)
    else:
        vid=df['voter_id'].iloc[-1]+1
        df1 = pd.DataFrame({"voter_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "hasVoted":[0]},)

        df = pd.concat([df, df1],ignore_index=True)

    df.to_csv(path/'voterList.csv')

    return vid
