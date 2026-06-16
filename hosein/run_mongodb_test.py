import os
import json
import subprocess

MONGO_URI = "mongodb://root:mongo@mongo:27017/leetcode?authSource=admin"

def run_js_file(script_path, capture_output=False):
    cmd = ["mongosh", MONGO_URI, "--quiet", "--file", script_path]
    if capture_output:
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise subprocess.CalledProcessError(proc.returncode, cmd, output=proc.stdout, stderr=proc.stderr)
        try:
            return json.loads(proc.stdout.strip())
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON from {script_path}: {proc.stdout}")
    else:
        subprocess.run(cmd, check=True, capture_output=True)  # will raise on error
        return None

def run_mongodb_test(base_dir):
    run_js_file(os.path.join(base_dir, "setup.js"))
    return run_js_file(os.path.join(base_dir, "test.js"), capture_output=True)