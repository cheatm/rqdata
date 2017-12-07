import os


ENV_HOME_DIR = "RQDATA_HOME"


HOME = os.environ.get(ENV_HOME_DIR, "/data")
BUNDLE_ROOT = os.path.join(HOME, "bundle")
