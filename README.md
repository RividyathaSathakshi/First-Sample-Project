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
