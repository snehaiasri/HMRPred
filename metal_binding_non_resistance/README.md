**Metal-binding but Non-resistance Validation Datasets**

This directory contains curated validation datasets comprising metal-binding but non-resistance proteins used to assess the specificity of HMRPred. Protein sequences were retrieved from UniProt using curated functional keywords for iron- and zinc-binding metabolic enzymes (e.g., superoxide dismutases, cytochromes, carbonic anhydrases, and alcohol dehydrogenases), while explicitly excluding resistance-related annotations. To avoid overlap with positive HMR proteins, all sequences were filtered to retain those sharing <20% sequence identity with the corresponding resistance datasets.The details are given in the follwoing table. 

## Table: Metal-binding but Non-resistance Protein Datasets from UniProt

| Metal | Functional keywords | UniProt hits | Sequences with <20% identity to HMR |
|------|--------------------|--------------|-------------------------------------|
| Fe | Superoxide dismutase, Cytochrome c/b, Ferredoxin, Catalase | 17,989 | 2,886 |
| Zn | Carbonic anhydrase, Alcohol dehydrogenase | 2,429 | 694 |


The predicted non-HMR, metal-binding proteins (for iron and zinc) are provided as the csv files showing high non-HMR probabilities predicted by HMRPred and corresponding metal-binding probabilities from MeBiPred, illustrating functional specificity.


