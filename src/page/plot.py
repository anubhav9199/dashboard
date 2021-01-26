from Lib.utils import title_awesome
from core.plots_n_graphs import PlotsAndGraphsEngine

def write():
    title_awesome('Plots & Graphs')
    PlotsAndGraphsEngine.plots_n_graphs_main(
        'Plots & Graphs', 'Plotting data you gave.')
