# First-Sample-Project
hello world !

## Urine test strip detection (Roboflow)

`urine_strip_detect.py` sends one image to the Roboflow workflow
`urine-test-strips-main-3jtim-5rdpn` (workspace `sathakshi2-gmail-com`) and prints the detections.

```bash
pip install -r requirements.txt
export ROBOFLOW_API_KEY="your_private_api_key"   # never commit your key
python urine_strip_detect.py path/to/strip.jpg
```

Options: `--confidence 0.5` changes the threshold (default 0.4), and `--json` also prints the raw response.

### Running from VS Code without the terminal

1. Install the **Python** extension (Extensions icon on the left, search "Python", by Microsoft).
2. Press **Ctrl+Shift+P**, run **Python: Create Environment**, choose **Venv**, pick your Python,
   and tick **requirements.txt** so it installs `inference-sdk`.
3. Create a file named `.env` in the project folder containing
   `ROBOFLOW_API_KEY=your_private_key`. It is gitignored, so it is never committed.
4. Open `urine_strip_detect.py` and click the **▶ Run** button (top right). A window opens so you can
   pick a test-strip image, and the detections appear in the panel at the bottom.
