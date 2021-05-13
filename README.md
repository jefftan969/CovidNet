# 11-785 Project

Course project for 11-785: Deep Learning Applications in COVID-19.

Creating a sequence model using recurrent neural networks to identify genomic divergence, mutations, and clade in COVID-19 spike protein sequences.

Abbey Pei, Amelia Kuang, Jeff Tan, Jenny Ding, Sylvia Zhang
TA Mentor: Joseph Konan

## Repository Organization

This repository contains the following files:
 - **data**
     - **amino_list.txt**: Mapping from single-letter amino acid codes to integers
     - **clade_mapping.npy**: Mapping from clade labels to integers
     - **metadata.zip**: Metadata file from GISAID, containing data labels for each sample in the dataset
     - **pango_mapping.npy**: Mapping from pango labels to integers
     - **spikeprot0309.zip**: Spike protein sequence file from GISAID, containing spike protein sequences for each sample in the dataset
 - **data_old**: This directory contains our original and much smaller dataset, with metadata sourced from NextStrain instead of GISAID.
     - **nextstrain_original**: Original NextStrain dataset, obtained by mapping between protein sequence, metadata, and timetree files
     - **nextstrain_updated**: Updated NextStrain dataset, obtained by mapping between just protein sequence and metadata files
     - **data_preprocess_old.ipynb**: Old data processing notebook, used to produce nextstrain_updated dataset
     - **nextstrain_ncov_global_metadata.tsv**: Metadata from NextStrain dataset
     - **nextstrain_ncov_global_timetree.nexus**: Timetree from NextStrain dataset
 - **figures**: This directory contains selected figures from our final report
 - **models**
     - **baseline_model.ipynb**: Implementation of our baseline model with CNN, LSTM, and fully connected layers
     - **model_2cnn_3fc_balancedData.ipynb**: Modification of our baseline model with additional CNN and fully connected layers
     - **model_2cnn_3fc_bert.ipynb**: Implementation of our Bert Embedding with Hydrophilicity Encoding model
     - **model_pyramidal_lstm.ipynb**: Implementation of our Pyramidal LSTM model
 - **data_preprocess.ipynb**: Produces raw training / validation data from GISAID protein sequence and metadata files
 - **embedding_visualization.ipynb**: Uses T-SNE and PCA from scikit-learn to visualize the embeddings and input data of our model
 - **sequence_balance.ipynb**: Takes raw training / validation data produced by data_preprocess.ipynb, and downsamples the dataset to produce balanced data with an equal number of items per label