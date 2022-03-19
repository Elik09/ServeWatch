#! /bin/bash
outfile="client.bin"
python3 -m py_compile client.py && mv "__pycache__/client.cpython-36.pyc" "$outfile" && rm -rf "__pycache__" && echo "[+] Compiled and saved to $outfile" || echo "[-] Compiling failed"
