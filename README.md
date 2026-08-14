# DocHelper

A private, self-hosted RAG application for chatting with your documents.

## Project layout

```
doc-helper/
├── app.py                    # entry point — launches the Gradio web UI
├── flowsettings.py           # main application settings (models, indices, features)
├── libs/
│   ├── dochelper/            # core library: LLMs, embeddings, indexing, agents
│   └── dochelper_app/        # application: web UI, pages, DB, user management
├── scripts/                  # install / launch helpers
└── templates/                # cookiecutter project templates
```

Two Python packages:

- **`dochelper`** — the core AI toolkit. Import this to build your own pipelines.
- **`dochelper_app`** — the RAG web application built on top of the core library.

## System requirements

1. [Python](https://www.python.org/downloads/) >= 3.10
2. [Docker](https://www.docker.com/) — optional, if you install with Docker
3. [Unstructured](https://docs.unstructured.io/open-source/installation/full-installation#full-installation) — only if you need to process files beyond `.pdf`, `.html`, `.mhtml`, and `.xlsx`

## Installation

### Option 1: Using uv (recommended)

```shell
uv sync --python 3.10
source .venv/bin/activate     # Windows: .venv\Scripts\activate
```

### Option 2: Using conda

```shell
conda create -n dochelper python=3.10
conda activate dochelper

pip install -e "libs/dochelper[all]"
pip install -e "libs/dochelper_app"
```

### Option 3: Using Docker

Build the image locally:

```shell
docker build -t dochelper:latest .
```

Then run it:

```shell
docker run \
  -e GRADIO_SERVER_NAME=0.0.0.0 \
  -e GRADIO_SERVER_PORT=7860 \
  -v ./dochelper_app_data:/app/dochelper_app_data \
  -p 7860:7860 -it --rm \
  dochelper:latest
```

The Dockerfile defines `lite`, `full`, `paddle`, and `ollama` build targets,
selectable with `--target` (defaults to the last stage if omitted). The `full`
target adds `unstructured` for extra file types at the cost of a larger image;
`ollama` bundles Ollama for fully local RAG.

```shell
docker build --target lite -t dochelper:lite .
```

## Configuration

Create a `.env` file in the project root to pre-configure models and API keys.
It is read once on first run to populate the database; afterwards, settings are
managed through the UI.

```shell
OPENAI_API_KEY=sk-...
# AZURE_OPENAI_API_KEY=...
# COHERE_API_KEY=...
```

Application behaviour (available models, indices, feature flags) is configured
in [flowsettings.py](flowsettings.py).

## Running

```shell
python app.py
```

- The app launches in your browser automatically.
- Default username and password are both `admin`. Change this immediately and
  add additional users through the UI.
- Check the `Resources` tab → `LLMs and Embeddings` to confirm your `api_key`
  values were picked up correctly.

### Optional: in-browser PDF viewer

Download [PDF_JS_DIST](https://github.com/mozilla/pdf.js/releases/download/v4.0.379/pdfjs-4.0.379-dist.zip)
and extract it to `libs/dochelper_app/dochelper_app/assets/prebuilt`.

## GraphRAG setup

GraphRAG indexing is optional. Three implementations are supported:

<details>
<summary>NanoGraphRAG (recommended)</summary>

- Install: `pip install nano-graphrag`
- If you hit version conflicts:
  `pip uninstall hnswlib chroma-hnswlib && pip install chroma-hnswlib`
- Launch with the `USE_NANO_GRAPHRAG=true` environment variable.
- Set your default LLM & embedding models in Resources; they are picked up
  automatically.

</details>

<details>
<summary>LightRAG</summary>

- Install: `pip install git+https://github.com/HKUDS/LightRAG.git`
- If you hit version conflicts:
  `pip uninstall hnswlib chroma-hnswlib && pip install chroma-hnswlib`
- Launch with the `USE_LIGHTRAG=true` environment variable.

</details>

<details>
<summary>MS GraphRAG</summary>

- Install: `pip install "graphrag<=0.3.6" future`
- Requires an OpenAI or Ollama API.
- Set `GRAPHRAG_API_KEY` in your environment.
- To customize indexing parameters, copy `settings.yaml.example` and set
  `USE_CUSTOMIZED_GRAPHRAG_SETTING=true`.

</details>

## Application data

All application data (databases, uploaded files, vector stores) is stored in
`./dochelper_app_data`. Back up or copy this folder to move an installation to
another machine.

## Development

```shell
pip install -e "libs/dochelper[dev]"
pre-commit install
pytest libs/dochelper/tests
```
