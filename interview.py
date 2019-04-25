 # first = songs[0]

    # # return songs, first

    # for dur in songs:
    #     if (dur + first) % 60 == 0:
    #         chosen_songs.append(dur)



    count = 0 

    dic = {}
    for i in songs:
        dic[i] = dic.get(i, 0) + 1

    for key1 in dic.keys():
        # Look for fitting pair in hashmap
        for key2 in dic.keys():

            if (key1 + key2) % 60 == 0:
                count += 1