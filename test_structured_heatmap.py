# Reference 
# http://seaborn.pydata.org/examples/structured_heatmap.html

def test_structured_heatmap():    
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    sns.set()

    # Load the brain networks example dataset
    df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

    # Select a subset of the networks
    used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
    used_columns = (df.columns.get_level_values("network")
                              .astype(int)
                              .isin(used_networks))
    df = df.loc[:, used_columns]

    # Create a categorical palette to identify the networks
    network_pal = sns.husl_palette(8, s=.45)
    network_lut = dict(zip(map(str, used_networks), network_pal))

    # Convert the palette to vectors that will be drawn on the side of the matrix
    networks = df.columns.get_level_values("network")
    network_colors = pd.Series(networks, index=df.columns).map(network_lut)

    # Draw the full plot
    g = sns.clustermap(df.corr(), center=0, cmap="hot_r",
                   row_colors=network_colors, col_colors=network_colors,
                   linewidths=.75, figsize=(13, 13))

    plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(), fontsize=12, rotation = 0)
    plt.setp(g.ax_heatmap.xaxis.get_majorticklabels(), fontsize=12, rotation = 90)

    plt.savefig('figure-structured-heatmap.png')

