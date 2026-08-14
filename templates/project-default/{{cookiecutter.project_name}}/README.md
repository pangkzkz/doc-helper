<div align="center">

# Project {{ cookiecutter.project_name }}

</div>

# Install

```bash
# Create new conda env (optional)
conda create -n {{ cookiecutter.project_name }} python=3.10
conda activate {{ cookiecutter.project_name }}

# Clone and install the project
git clone "<{{ cookiecutter.project_name }}-repo>"
cd "<{{ cookiecutter.project_name }}-repo>"
pip install -e .

# Generate the project structure
cd ..
dochelper start-project
```

# Usage

- Build the pipeline in `pipeline.py`
