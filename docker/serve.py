"""Serve Camoufox on 0.0.0.0, configured from the environment."""

import os

from camoufox.server import launch_server

headless = os.environ["CAMOUFOX_HEADLESS"]

launch_server(
    headless=headless if headless == "virtual" else headless == "true",
    host="0.0.0.0",
    port=int(os.environ["CAMOUFOX_PORT"]),
    ws_path=os.environ["CAMOUFOX_WS_PATH"],
    geoip=os.environ.get("CAMOUFOX_PROXY") is not None,
    proxy={"server": os.environ["CAMOUFOX_PROXY"]} if os.environ.get("CAMOUFOX_PROXY") else None,
)
