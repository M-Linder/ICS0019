import pandas as pd
from pathlib import Path

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt


# Variables for map extent and coordinate comparisons.
up = 72
down = 32
right = 35
left = -12


def main():
    fig = plt.figure(figsize=[15, 15])
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([left, right, down, up], crs=ccrs.PlateCarree())

    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle="-")
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)

    # Set map title.
    plt.title(
        "Tallinna Lennujaama Lennud aastatel 2020 ja 2023. Matthias Linder.",
        fontsize=25,
    )

    # Create the merged tables of pre- and post-covid flights.
    list1 = merge_tables("initial_data/otselennud20.csv", "output_pre_covid.csv")
    list2 = merge_tables("initial_data/otselennud23.csv", "output_post_covid.csv")

    # Save Tallinn's latitude and longitude.
    source_latitude = float(list1.iloc[0]["Latitude"])
    source_longitude = float(list1.iloc[0]["Longitude"])

    # Draw the paths laid out in the generated lists.
    draw_paths(
        list1,
        source_longitude,
        source_latitude,
        "green",
        3,
        "-",
        15,
        "Pre-Covid Flights",
    )
    draw_paths(
        list2,
        source_longitude,
        source_latitude,
        "red",
        2,
        "--",
        10,
        "Post-Covid Flights",
    )

    # Draw the map legend. Automatically detects invisible lines made within draw_paths method.
    ax.legend(loc="upper left", fontsize=25)

    # Save figure as png and display it.
    plt.savefig("map.png")
    plt.show()


def draw_paths(
    input_list, source_lon, source_lat, color, width, linestyle, markersize, label
):
    # Invisible line for automatic legend generation.
    plt.plot(
        [source_lon, source_lon],
        [source_lat, source_lat],
        linestyle=linestyle,
        markersize=markersize,
        color=color,
        linewidth=width,
        marker="o",
        transform=ccrs.Geodetic(),
        label=label,
    )

    # Iterate through list and draw the lines on a map.
    for i in range(len(input_list)):
        longitude = float(input_list.iloc[i]["Longitude"])
        latitude = float(input_list.iloc[i]["Latitude"])
        name = input_list.iloc[i]["IATA"]

        if left < longitude < right & down < latitude < up:
            plt.plot(
                [source_lon, longitude],
                [source_lat, latitude],
                linestyle=linestyle,
                markersize=markersize,
                color=color,
                linewidth=width,
                marker="o",
                transform=ccrs.Geodetic(),
            )
            plt.text(longitude, latitude, name, fontsize=15, transform=ccrs.Geodetic())


def merge_tables(input_path, output_path):
    # Merge the given tables. Either a combination of airports.dat and otselennud20.csv or otselennud23.csv.
    table_1 = pd.read_csv(input_path, sep=";")
    table_2 = pd.read_table("initial_data/airports.dat", sep=",")

    result = table_1.merge(table_2, how="inner", left_on="IATA", right_on="IATA")

    # Code to save lists to file:
    # save_to_file(result, output_path)

    return result


def save_to_file(input_table, path):
    path_to_file = Path("generated_data/" + path)
    path_to_file.parent.mkdir(parents=True, exist_ok=True)
    input_table.to_csv(path_to_file, index=False)


if __name__ == "__main__":
    # Execute the code.
    main()
