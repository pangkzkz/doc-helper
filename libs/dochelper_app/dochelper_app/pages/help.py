from pathlib import Path

import gradio as gr
from decouple import config
from theflow.settings import settings

KH_DEMO_MODE = getattr(settings, "KH_DEMO_MODE", False)
HF_SPACE_URL = config("HF_SPACE_URL", default="")


class HelpPage:
    def __init__(
        self,
        app,
        doc_dir: str = settings.KH_DOC_DIR,
        app_version: str | None = settings.KH_APP_VERSION,
    ):
        self._app = app
        self.doc_dir = Path(doc_dir)
        self.app_version = app_version

        about_md_dir = self.doc_dir / "about.md"
        about_md = ""
        if about_md_dir.exists():
            with about_md_dir.open(encoding="utf-8") as fi:
                about_md = fi.read()
        if about_md:
            with gr.Accordion("About"):
                if self.app_version:
                    about_md = f"Version: {self.app_version}\n\n{about_md}"
                gr.Markdown(about_md)

        if KH_DEMO_MODE:
            with gr.Accordion("Create Your Own Space"):
                gr.Markdown(
                    "This is a demo with limited functionality. "
                    "Use **Create space** button to install DocHelper "
                    "in your own space with all features "
                    "(including upload and manage your private "
                    "documents securely)."
                )
                gr.Button(
                    value="Create Your Own Space",
                    link=HF_SPACE_URL,
                    variant="primary",
                    size="lg",
                )

        user_guide_md_dir = self.doc_dir / "usage.md"
        user_guide_md = ""
        if user_guide_md_dir.exists():
            with user_guide_md_dir.open(encoding="utf-8") as fi:
                user_guide_md = fi.read()
        if user_guide_md:
            with gr.Accordion("User Guide", open=not KH_DEMO_MODE):
                gr.Markdown(user_guide_md)
