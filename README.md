# Python DS Libs

## Setup on Windows
Anaconda is used to run Jupyter
```
# step 1: update conda
$conda update conda -y

# step 2: create an virtual environment
$conda create -n <python-ds-libs> python=3.7.1 anaconda -y

# step 3: activate venv
$conda activate python-ds-libs

# step 4: install required libs
$pip install -r requirements.txt

# or
#conda install -n yourenvname [package]

# step 5: 
$jupyter notebook
```

To deactivate or delete venv
```
# Deactivate your virtual env
$source deactivate

# delete a no longer needed virtual env
$conda remove -n yourenvname -all
```

## Quick examples for following python libs:
* numpy
* pandas
