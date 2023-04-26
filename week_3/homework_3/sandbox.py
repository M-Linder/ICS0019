import pandas as pd
from pathlib import Path

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ax = plt.axes(projection=ccrs.Mollweide())
    ax.stock_img()
    plt.show()


def merge_data():
    file1 = pd.read_csv('initial_data/otselennud20.csv', sep=';', names=["City", "IATA"])

    file2 = pd.read_csv('initial_data/otselennud23.csv', sep=';', names=["City", "IATA"])

    file3 = pd.read_table('initial_data/airports.dat', sep=',', names=["ID", "Name", "City", "Country", "IATA", "ICAO",
                                                                       "Latitude", "Longitude", "Altitude", "Timezone",
                                                                       "DST", "DZ", "Type", "Source"])
    file1.drop(index=file1.index[0], axis=0, inplace=True)
    file2.drop(index=file1.index[0], axis=0, inplace=True)
    file3.drop(index=file1.index[0], axis=0, inplace=True)

    result = file1.merge(file3, how='inner', left_on='IATA', right_on='IATA')

    print(result.columns)

    path = Path('generated_data/output.csv')
    path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(path, index=False)
