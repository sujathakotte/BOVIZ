<h2 align="center"> <a href="https://arxiv.org/abs/25ff03.01463">Fast and inexpensive visualization of genome collection at scale</a></h2>
<h4 align="center" color="A0A0A0"> Sujatha Kotte, Naina Tiwari, Kavya Vaddadi, Vangala Govindakrishnan Saipradeep, Thomas Joseph, Aditya Rao, Rajgopal Srinivasan, Naveen Sivadasan</h4>
<h5 align="center"> If you like our project, please give us a star ⭐ on GitHub for the latest update.</h5>
<!--
<div align="center">

[![arXiv](https://img.shields.io/badge/Arxiv-2503.01463-b31b1b.svg?logo=arXiv)](https://www.arxiv.org/abs/2503.01463)
[![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/CQU-ADHRI-Lab/MI-DETR)
[![License](https://img.shields.io/badge/Code%20License-Apache2.0-yellow)](https://github.com/CQU-ADHRI-Lab/MI-DETR/blob/main/LICENSE)

</div>
-->
<div align=center>
<img src="figures/results.gif" width="960px">
</div>


# BOVIZ
This is the official implementation of the paper "Fast and inexpensive visualization of genome collection at scale".

<div align="center">
  <img src="figures/BOVIZ_Pipeline.png"/>
</div><br/>

We have developed a computationally efficient and scalable method, BOVIZ (Bag-Of-Variants visualization), to visualize and explore the spatiotemporal patterns present in large scale genome data. BOVIZ efficiently extracts variant level features of the strains and computes a novel and efficient Bag Of Variants (BOV) embedding to a lower dimensional space allowing the visualizations to effectively capture the similarity as well as divergence in the data. It can also support a variety of filters based on both the genomic regions of interest and the metadata such as geography, time interval and clade details.

## Installation

We tested our code with Python=3.10.12
#### Install git lfs - for large files download<br>
sudo apt update<br>
sudo apt install git-lfs<br>

#### jupyter environment setup<br>
python3 -m venv ~/jupyter_env<br>
source ~/jupyter_env/bin/activate
 
#### Install JupyterLab, Notebook 6, widgets, and kernel<br>
pip install --upgrade pip setuptools wheel<br>
pip install notebook==6.5.4 jupyterlab ipywidgets jupyterlab_widgets ipykernel<br>
pip install ipython==8.15.0 traitlets==5.7.1

#### Under your working directory<br>
git clone https://github.com/sujathakotte/BOVIZ.git<br>
cd BOVIZ/

#### Intsall required packages<br>
pip install -r requirements.txt

## RUN
        
### plot BOV

Visualization of Bag-Of-Variants embedding of samples. Execute the following,

#### jupyter lab plot_BOV.ipynb

After running all the cells, the following dropdown widgets will appear.<br>
1. Country: multiple selection can be performed by shift+click / ctrl+click.<br>
2. Select Lineage -  Select Lineage.<br>
3. Datapoints on canvas - User can set a maximum cap on the samples. e.g. if sample size is 1000, only 1000 samples will be picked from each country selected.<br>
4. Timestamp - Time duration.<br>
5. Type of plot : option to choose different visualization algorithm on embedding vectors.<br>
6. Genomic region of interest : option to choose specific genomic region or the whole genomic region.<br>

After selecting all the options, click on run option. Once the process gets completed, user can choose different metadata fields and analyze the visualization.


### plot VE

Visualization of Variant feature Embedding of all the samples. Execute the following,

#### jupyter lab plot_VE.ipynb

After running all the cells, the following dropdown widgets will appear.<br>
1. Country: multiple selection can be performed by shift+click / ctrl+click.<br>
2. Select Lineage -  Select Lineage.<br>
3. Datapoints on canvas - User can set a maximum cap on the samples. e.g. if sample size is 1000, only 1000 samples will be picked from each country selected.<br>
4. Timestamp - Time duration.<br>
5. Type of plot : option to choose different visualization algorithm on embedding vectors.<br>
6. Genomic region of interest : option to choose specific genomic region or the whole genomic region.<br>

After selecting all the options, click on run option. Once the process gets completed, user can choose different metadata fields and analyze the visualization.


