Streamed_Graph_Datasets
=======================

Collection and Streaming of Graph Datasets


-----------------------------------------------------------------------------------------------------------------------------
I have collected several graph datasets from various application domains. Those graph datasets are dynamic in nature with nodes and edges being added, deleted or modified over time. I converted the original datasets into GraphML format and streamed them using time-series representations with proper time-window sizes. This task will help people understand the implicit relations of entities within each dataset and facilitate the development of graph mining algorithms on dynamic graph datasets.

The GraphML-Attributes extension mechanism has been used to describe properties of entities and their relations in these datasets. Most of the collected datasets exhibit additions of nodes and edges over time as their dynamic nature. So in each GraphML representation, I declared an attribute named 'modification' whose default value is 'add' for a node or an edge. However, some other datasets are characterized by both additions and deletions of nodes and edges over time. Therefore, I explicitly use key/data label to indicate that the value of 'modification' attribute is 'delete' when a node or an edge is removed at a certain time window.
