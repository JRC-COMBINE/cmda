
import os
import pandas as pd


def ecgrdvq_metadata():
    _path = os.path.dirname(__file__)
    data_path = os.path.join(_path,'src/ecgrdvq_metadata.csv')
    data = pd.read_csv(data_path)

    data = data.to_dict('list')
    data['public_dir'] = data.pop('record_path')
    return data

    


if __name__ == "__main__":
    df = ecgrdvq_metadata()
    print(df['public_dir'])
