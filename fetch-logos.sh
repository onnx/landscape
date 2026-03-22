#!/usr/bin/env bash
# Downloads SVG logos into hosted_logos/
# Run from the landscape/ directory: bash fetch-logos.sh

set -euo pipefail

LOGOS_DIR="$(dirname "$0")/hosted_logos"
SI="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons"

fetch() {
  local name="$1"
  local url="$2"
  echo "Fetching $name..."
  curl -fsSL "$url" -o "$LOGOS_DIR/$name"
}

# Simple Icons (https://simpleicons.org)
fetch pytorch.svg          "$SI/pytorch.svg"
fetch tensorflow.svg       "$SI/tensorflow.svg"
fetch paddlepaddle.svg     "$SI/paddlepaddle.svg"
fetch huggingface.svg      "$SI/huggingface.svg"
fetch nvidia.svg           "$SI/nvidia.svg"
fetch intel.svg            "$SI/intel.svg"
fetch microsoft.svg        "$SI/microsoft.svg"
fetch microsoftazure.svg   "$SI/microsoftazure.svg"
fetch meta.svg             "$SI/meta.svg"
fetch qualcomm.svg         "$SI/qualcomm.svg"
fetch groq.svg             "$SI/groq.svg"
fetch amazonaws.svg        "$SI/amazonaws.svg"
fetch googlecloud.svg      "$SI/googlecloud.svg"
fetch apachetvm.svg        "$SI/apachetvm.svg"
fetch llvm.svg             "$SI/llvm.svg"

# ONNX logo from onnx.ai
fetch onnx.svg "https://raw.githubusercontent.com/onnx/onnx/main/docs/ONNXLogo.svg"

# ONNX Runtime — no official SVG in repo, use Microsoft logo as fallback
cp "$LOGOS_DIR/microsoft.svg" "$LOGOS_DIR/onnxruntime.svg"

# Netron
fetch netron.svg "https://raw.githubusercontent.com/lutzroeder/netron/main/media/icon.svg"

echo ""
echo "Done. Logos written to $LOGOS_DIR/"
echo ""
echo "Missing / needs manual sourcing:"
echo "  - onnxruntime.svg (using microsoft.svg fallback — replace with official ORT logo)"
echo "  - paddlepaddle.svg (verify Simple Icons has this slug)"
echo "  - apachetvm.svg    (verify Simple Icons has this slug)"
echo "  - groq.svg         (verify Simple Icons has this slug)"
echo "  - llvm.svg         (verify Simple Icons has this slug)"
