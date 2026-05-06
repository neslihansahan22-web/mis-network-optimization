\# E-Ticaret Lojistik Dağıtım Ağı Optimizasyonu

\#\# 1\. Real-World Problem Context  
İstanbul genelinde faaliyet gösteren bir e-ticaret firmasının lojistik maliyetlerini optimize etmesi gerekmektedir.

\#\# 2\. Problem Definition  
Lojistik merkezinden çıkan ürünlerin hedef depolara en düşük nakliye maliyetiyle ulaştırılması amaçlanmıştır.

\#\# 3\. Network Model  
\- \*\*Düğümler (Nodes):\*\* Depolar ve şubeler.  
\- \*\*Kenarlar (Edges):\*\* Nakliye hatları.  
\- \*\*Ağırlıklar (Weights):\*\* Birim nakliye maliyeti (TL).

\#\# 4\. Nodes and Edges  
Ağ yapısında toplam 7 düğüm ve 10 kenar bulunmaktadır. Veri kaynağı: \`data/network\_data.csv\`.

\#\# 5\. Selected Algorithm  
Maliyet minimizasyonu için \*\*Dijkstra En Kısa Yol (Shortest Path)\*\* algoritması tercih edilmiştir.

\#\# 6\. Python Implementation  
Kodlama sürecinde \`NetworkX\` ile ağ yapısı kurulmuş, \`Matplotlib\` ile görselleştirilmiştir.

\#\# 7\. Results  
Terminal çıktısına göre belirlenen rota:   
\*\*(Buraya Terminaldeki Rota ve Maliyet sonucunu yaz\!)\*\*

\#\# 8\. Managerial Interpretation  
Elde edilen sonuçlar, işletmenin sevkiyat planlamasında veri odaklı modeller kullanarak operasyonel giderleri düşürebileceğini kanıtlamaktadır.

\#\# 9\. How to Run the Code  
1\. \`python3 \-m pip install \-r requirements.txt\`  
2\. \`python3 src/solution.py\`

\#\# 10\. References  
Bkz: \`references/references.md\`  
