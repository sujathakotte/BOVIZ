python3 -m venv ~/jupyter_env
source ~/jupyter_env/bin/activate
 
# Upgrade pip and core tools
pip install --upgrade pip setuptools wheel
 
#Install JupyterLab, Notebook 6, widgets, and kernel
pip install notebook==6.5.4 jupyterlab ipywidgets jupyterlab_widgets ipykernel
pip install ipython==8.15.0 traitlets==5.7.1

#Intsall required packages
pip install -r requirements.txt
