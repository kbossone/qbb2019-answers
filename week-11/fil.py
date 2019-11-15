#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scanpy as sc

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

sc.pp.filter_genes(adata, min_counts = 1) #only consider genes with more than 1 count
sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all') #normalize with total UMI count per cell

filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)

adata = adata[:, filter_result.gene_subset] #filter genes
sc.pp.normalize_per_cell(adata)  # need to redo normalization after filtering
sc.pp.log1p(adata)
sc.pp.scale(adata)
# sc.tl.pca(adata,n_comps=50)
# sc.pl.pca(adata)



sc.pp.neighbors(adata)
# sc.tl.umap(adata)
sc.tl.tsne(adata)
sc.tl.louvain(adata, resolution=0.3)
sc.tl.rank_genes_groups(adata, 'louvain', groups=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], method = 'logreg')
sc.pl.rank_genes_groups(adata)
# sc.pl.umap(adata, color='louvain')
# sc.logging.print_memory_usage()
# sc.pl.tsne(adata, color='louvain', legend_loc='on data')