
E-Commerce Logistics Network Optimization

1. Real-World Problem Context
In the rapidly growing e-commerce sector, logistics costs represent a significant portion of operational expenses. For a firm operating in Istanbul, navigating the complex urban landscape to deliver goods efficiently is a critical challenge that directly impacts profitability and customer satisfaction.

2. Problem Definition
The objective of this project is to minimize the transportation costs between a central logistics hub and various regional warehouses. By identifying the most cost-effective routes, the firm can optimize its supply chain and reduce unnecessary mileage and fuel consumption.

3. Network Model
The logistics infrastructure is modeled as an undirected, weighted graph. In this mathematical abstraction, locations represent points of interest, and the connections between them represent available transit routes.

4. Nodes and Edges
*   **Nodes:** Represent 7 key locations, including the "Lojistik_Merkezi" (Source) and "Tuzla_Depo" (Destination).
*   **Edges:** Represent 10 primary transport corridors connecting these locations.
*   **Weights:** Represent the specific shipping costs (in TL) assigned to each corridor, as detailed in `data/network_data.csv`.

5. Selected Algorithm
**Dijkstra’s Algorithm** was selected for this optimization. It is the industry-standard choice for finding the shortest path in a graph with non-negative edge weights, ensuring that we find the absolute minimum cost route from the hub to the target warehouse.

6. Python Implementation
The solution is implemented using:
*   **NetworkX:** For graph construction and executing the Dijkstra algorithm.
*   **Pandas:** For structured data management and CSV ingestion.
*   **Matplotlib:** For generating visual network maps.

7. Results
The execution of the model yielded the following optimal parameters:
*   **Optimal Route:** Lojistik_Merkezi -> Uskudar_Sube -> Umraniye_Sube -> Maltepe_Sube -> Sancaktepe_Sube -> Tuzla_Depo
*   **Minimum Total Cost:** 67 TL

8. Managerial Interpretation
From a management perspective, this model provides a data-driven framework for logistics planning. Instead of relying on intuition, the firm can now use algorithmic pathfinding to ensure every shipment follows the most economical path, leading to measurable cost savings and improved operational transparency.

9. How to Run the Code
1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Navigate to the project root and run:
    ```bash
    python3 src/solution.py
    ```

10. References
*   NetworkX Documentation: [https://networkx.org/](https://networkx.org/)
*   Dijkstra, E. W. (1959). A note on two problems in connexion with graphs.
*   Pandas Documentation:** https://pandas.pydata.org/docs/
*   Matplotlib Pyplot:** https://matplotlib.org/stable/tutorials/introductory/pyplot.html
