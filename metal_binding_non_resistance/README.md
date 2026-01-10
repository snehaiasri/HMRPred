**Metal-binding but Non-resistance Validation Datasets**

This directory contains curated validation datasets comprising metal-binding but non-resistance proteins used to assess the specificity of HMRPred. Protein sequences were retrieved from UniProt using curated functional keywords for iron- and zinc-binding metabolic enzymes (e.g., superoxide dismutases, cytochromes, carbonic anhydrases, and alcohol dehydrogenases), while explicitly excluding resistance-related annotations. To avoid overlap with positive HMR proteins, all sequences were filtered to retain those sharing <20% sequence identity with the corresponding resistance datasets.The details are given in the follwoing table. 

## Table: Metal-binding but Non-resistance Protein Datasets from UniProt

| Metal | Functional keywords | UniProt hits | Sequences with <20% identity to HMR |
|------|--------------------|--------------|-------------------------------------|
| Fe | Superoxide dismutase, Cytochrome c/b, Ferredoxin, Catalase | 17,989 | 2,886 |
| Zn | Carbonic anhydrase, Alcohol dehydrogenase | 2,429 | 694 |


These filtered sequences were subsequently evaluated using HMRPred. Notably, 82.3% of zinc-binding proteins and 97.8% of iron-binding proteins were correctly classified as non-HMR, despite being predicted as metal-binding proteins by MeBiPred. This targeted validation demonstrates that HMRPred effectively distinguishes functional heavy metal resistance proteins from general metabolic metalloproteins, thereby providing a clear advantage over generic metal-binding predictors that do not incorporate resistance-specific functional context.

The predicted non-HMR, metal-binding proteins for iron and zinc are provided as CSV files. These files report high non-HMR probabilities predicted by HMRPred alongside the corresponding metal-binding probabilities from MeBiPred, demonstrating functional specificity.


