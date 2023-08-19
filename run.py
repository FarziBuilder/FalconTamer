import uvicorn
import argparse
import json
from typing import AsyncGenerator

from fastapi import BackgroundTasks, FastAPI, Request
from fastapi.responses import JSONResponse, Response, StreamingResponse
import uvicorn

from vllm.engine.arg_utils import AsyncEngineArgs
from vllm.engine.async_llm_engine import AsyncLLMEngine
from vllm.sampling_params import SamplingParams
from vllm.utils import random_uuid
import api_server

TIMEOUT_KEEP_ALIVE = 5  # seconds.
TIMEOUT_TO_PREVENT_DEADLOCK = 1  # seconds

if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--host", type=str, default="localhost")
#     parser.add_argument("--port", type=int, default=8000)
#     parser = AsyncEngineArgs.add_cli_args(parser)
#     args = parser.parse_args()

#     engine_args = AsyncEngineArgs.from_cli_args(args)
#     engine = AsyncLLMEngine.from_engine_args(engine_args)
#     api_server.set_engine(engine)

    uvicorn.run("api_server:app",
                host="127.0.0.1",
                port=8080,
                log_level="debug",
                timeout_keep_alive=TIMEOUT_KEEP_ALIVE,
                workers=10)