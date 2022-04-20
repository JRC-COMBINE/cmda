

def _check_duplicated_key_names(res, res_all):

    # check the res key with res_all key and handle similar names
    for k in res.keys():
        key_updated = k
        while key_updated in res_all:
            key_splited = key_updated.split('__')
            try:
                key_updated = int(key_splited[1])+1
                key_updated = f'{k}__{str(key_updated)}'
            except:
                key_updated = f"{k}__2"

        res[key_updated] = res.pop(k)

    return res