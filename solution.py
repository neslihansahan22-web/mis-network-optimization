import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os

# 1. Veriyi Yükleme
# Dosya yolunu proje klasör yapısına göre ayarlıyoruz
data_path = os.path.join('data', 'network_data.csv')

try:
    df = pd.read_csv(data_path)
except FileNotFoundError:
    print("Hata: 'data/network_data.csv' dosyası bulunamadı. Lütfen dosya adını ve yerini kontrol edin.")
    exit()

# 2. Ağ (Network) Oluşturma
G = nx.Graph()

# CSV'deki her satırı ağa ekliyoruz
for index, row in df.iterrows():
    G.add_edge(row['source'], row['target'], weight=row['weight'])

# 3. En Kısa Yol Algoritmasını Çalıştırma (Dijkstra)
source_node = "Lojistik_Merkezi"
target_node = "Tuzla_Depo"

try:
    path = nx.shortest_path(G, source=source_node, target=target_node, weight='weight')
    path_length = nx.shortest_path_length(G, source=source_node, target=target_node, weight='weight')

    print("-" * 30)
    print(f"BAŞARILI: En Uygun Rota Bulundu!")
    print(f"Rota: {' -> '.join(path)}")
    print(f"Toplam Minimum Maliyet: {path_length} TL")
    print("-" * 30)
except nx.NetworkXNoPath:
    print(f"Hata: {source_node} ile {target_node} arasında bir yol bulunamadı.")

# 4. Görselleştirme
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42) # Her seferinde aynı düzeni korumak için seed eklendi

# Düğümleri ve kenarları çiz
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2500, font_size=9, font_weight='bold', edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("E-Ticaret Lojistik Dağıtım Ağı Optimizasyonu (En Kısa Yol)")

# 5. Sonuçları Kaydetme
results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

output_image_path = os.path.join(results_dir, 'network_visualization.png')
plt.savefig(output_image_path)
print(f"Görselleştirme '{output_image_path}' olarak kaydedildi.")

# Grafiği ekranda göster
plt.show()
