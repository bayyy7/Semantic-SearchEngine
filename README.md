# Semantic Search Engine
This repository contain implementation of Search Engine on Supreme Court Dataset, specifically on Narcotics Dataset. This execution start from crawling data from Supreme Court Indonesia Web, Data Preprocessing, Train Search Engine, and Evaluation.
# Crawling
Using implementation of Scrapy as Crawl spider to perform collect some data on Supreme Court Web.
# Dataset
This dataset have 11 attribute:<br>
- Terdakwa	
- Nomor Putusan	
- Kata Kunci	
- Tanggal Register	
- Lembaga Peradilan	
- Hakim Ketua	
- Hakim Anggota	
- Panitera	
- Catatan Amar
# Technique
Using BM25 Algorithm as Semantic Search Engine and using Random Forest as evaluation performance <br>
# Result
Below is the result performance of Semantic Search Engine using BM25 algorithm. As you can see, the performance is stunning all accross the evaluation metrics with 100% rate.

|      | Precision | Recall | F1-score | Support |
|------|-----------|--------|----------|---------|
| Non Sabu | 1.00 | 1.00 | 1.00 | 11 |
| Sabu | 1.00 | 1.00 | 1.00 | 2 |
| Accuracy | | | 1.00 | 13 |
| Macro avg | 1.00 | 1.00 | 1.00 | 13 |
| Weighted avg | 1.00 | 1.00 | 1.00 | 13 |
