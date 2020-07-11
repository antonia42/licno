import sys

import networkx as nx
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')


def detect_events(G_, G_cache_, theta_, avg_, std_, cc_lengths):
    """
    Function to detect connected components that indicate an event or and event
    candidate.

    Args:
        G_ (networkx.Graph()): The graph instance of the networkx Graph() class.
        
        G_cache_ (networkx.Graph()): The connected components that were cached
            as event candidates from the previous time window.

        theta_ (float): The number of similar words to add. Default value: 10.

        avg_ (float): The average size of the connected components from the
            previous time window. Default value: 0.

        std_ (float): The standard deviation of the sizes of the connected
            components from the previous time window. Default value: 0.

        cc_lengths (list): A list of the size of the connected components 
            (that will be next used to calculate average and standard deviation
            for the next time window).

    Returns:
        A tuple that contains:
            - (float) the average size of the CCs from the current time window.
            - (float) the standard deviation of the size of the CCs from the
                current time window.
            - (boolean) the event flag on whether there is at least an event or
                not in the current time window.
            - (networkx.Graph()) the updated graph with the connected
                components that were cache in the current time window.

    """
    small_ccs = []
    event_exists = 0
    threshold = theta_ * std_ + avg_

    H = nx.compose(G_, G_cache_)
    ccs = nx.connected_component_subgraphs(H)
    for cc in ccs:
        cc_nodes = cc.nodes()
        cc_len = len(cc_nodes)
        if cc_len < avg_:
            small_ccs += cc_nodes
        elif cc_len >= threshold:
            event_exists = 1

    H.remove_nodes_from(small_ccs)

    return (np.mean(cc_lengths), np.std(cc_lengths), event_exists, H)