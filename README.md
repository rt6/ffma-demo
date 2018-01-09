# FFMA-DEMO

Note: You will need to install miniconda if you do not already have conda on your system

## Get started in a few steps steps:

### 1) Create conda environment and install dependencies
```sh
# 1.1) create conda environment
conda create -n plotly-dash-demo python=3

# 1.2) source conda environment
source activate plotly-dash-demo

# 1.3) install dash packages via pip
pip install dash==0.19.0  # The core dash backend
pip install dash-renderer==0.11.1  # The dash front-end
pip install dash-html-components==0.8.0  # HTML components
pip install dash-core-components==0.15.2  # Supercharged components
pip install plotly --upgrade  # Plotly graphing library used in examples

# Below one line install does not work anymore - need to investigate!
conda env create -f environment.yml
```

### 2) Start python dash application server
```sh
python app.py
```
 
### 3) Open http://<SERVER-IP>:5000 in web browser to see analytics dashboard
 
