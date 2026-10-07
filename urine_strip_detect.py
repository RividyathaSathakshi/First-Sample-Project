"""Detect urine test-strip pads with the Roboflow "Urine Test Strips (Main)" workflow.

Usage:
    export ROBOFLOW_API_KEY=...        # never commit this
    python urine_strip_detect.py path/to/strip.jpg [--confidence 0.4] [--json]
"""

import argparse
import json
import os
import sys

from inference_sdk import InferenceHTTPClient

API_URL = "https://serverless.roboflow.com"
WORKSPACE_NAME = "sathakshi2-gmail-com"
WORKFLOW_ID = "urine-test-strips-main-3jtim-5rdpn"


def get_client() -> InferenceHTTPClient:
    api_key = os.environ.get("ROBOFLOW_API_KEY")
    if not api_key:
        sys.exit("Error: set the ROBOFLOW_API_KEY environment variable first.")
    return InferenceHTTPClient(api_url=API_URL, api_key=api_key)


def run_workflow(image_path: str, confidence: float | None = None) -> list:
    parameters = {}
    if confidence is not None:
        parameters["confidence"] = confidence
    return get_client().run_workflow(
        workspace_name=WORKSPACE_NAME,
        workflow_id=WORKFLOW_ID,
        images={"image": image_path},
        parameters=parameters or None,
        use_cache=True,  # cache the workflow definition for 15 minutes
    )


def extract_detections(result: list) -> list[dict]:
    """Pull the list of detection dicts out of the workflow output."""
    if not result:
        return []
    predictions = result[0].get("predictions") or {}
    # Object-detection output is {"image": {...}, "predictions": [...]}
    if isinstance(predictions, dict):
        return predictions.get("predictions", [])
    return predictions


def print_detections(detections: list[dict]) -> None:
    if not detections:
        print("No detections.")
        return
    print(f"{len(detections)} detection(s):")
    print(f"{'class':<24} {'conf':>6} {'x':>8} {'y':>8} {'w':>8} {'h':>8}")
    for d in sorted(detections, key=lambda d: (d.get("y", 0), d.get("x", 0))):
        print(
            f"{str(d.get('class')):<24} {d.get('confidence', 0):>6.2f} "
            f"{d.get('x', 0):>8.1f} {d.get('y', 0):>8.1f} "
            f"{d.get('width', 0):>8.1f} {d.get('height', 0):>8.1f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("image", help="path or URL of a test-strip image")
    parser.add_argument("--confidence", type=float, default=None,
                        help="confidence threshold (workflow default: 0.4)")
    parser.add_argument("--json", action="store_true",
                        help="also print the raw workflow response")
    args = parser.parse_args()

    if not args.image.startswith(("http://", "https://")) and not os.path.isfile(args.image):
        sys.exit(f"Error: image not found: {args.image}")

    result = run_workflow(args.image, args.confidence)
    if args.json:
        print(json.dumps(result, indent=2))
    print_detections(extract_detections(result))


if __name__ == "__main__":
    main()
