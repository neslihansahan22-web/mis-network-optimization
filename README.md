**E-Commerce Logistics Network Optimization**  
MIS Project: Supply Chain Cost Minimization using Dijkstra's Algorithm

**Project Overview**  
This project addresses a real-world logistics challenge for an Istanbul-based e-commerce firm. The primary objective is to determine the most cost-effective transportation routes between a central logistics hub and various regional warehouses using graph theory and network optimization techniques.

**Tech Stack**  
**Language:** Python 3.14  
**Libraries:**  NetworkX (Graph modeling and pathfinding),  Pandas (Data handling), Matplotlib (Network visualization)

Network Architecture  
The logistics network is modeled as a weighted undirected graph:  
**Nodes:** Represent warehouses and distribution branches (e.g., Kadıköy, Üsküdar, Tuzla).  
**Edges:** Represent the physical transportation routes between locations.  
**Weights:** Represent the shipping costs in Turkish Lira (TL).

**Algorithm & Logic**  
I implemented Dijkstra’s Algorithm to solve the shortest path problem. The algorithm systematically explores the network to find the path that minimizes the cumulative weight (cost) from the source node (Lojistik\_Merkezi) to the destination node (Tuzla\_Depo).

**Results & Visualization**  
Upon execution, the system generates a visual representation of the network and outputs the optimal route.

**Optimal Route:** Lojistik\_Merkezi \-\> Uskudar\_Sube \-\> Umraniye\_Sube \-\> Maltepe\_Sube \-\> Sancaktepe\_Sube \-\> Tuzla\_Depo  
**Minimum Cost:** 67 TL

The visualization is automatically saved to the \'results\' directory as 'network\_visualization.png'

**How to Run**  
1\. Ensure Python is installed.  
2\. Install dependencies:  
   \`\`\`bash  
   pip install \-r requirements.txt
