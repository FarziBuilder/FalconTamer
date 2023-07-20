# FalconTamer
28th June:- I know how to fine-tune Open-Source LLMs

8th July:- Deployed fine-tuned falcon 7b on AWS SageMaker

14th July:- Increased the inference time of LLaMa 7b by 24x using vLLMs and deployed it

20th July:- Production-ready fine-tuned LLM deployed using vLLM

Use !python -m vllm.entrypoints.api_server --model FarziBuilder/fastInferencetry10 --host 127.0.0.1 --port 8080 for starting the server and then run inference.py

Note:-

The first token generation time is affected by the max number of tokens generated. Generating all at once may take >2.5 sec, while generating in small steps (20 tokens at a time) may only take ~0.5 sec.
LLaMa v1 has been fine-tuned over 80 steps on a 790 dataset. The quality can be easily improved.
You can only specify the max tokens to be generated and hope that the whole statement is delivered within that limit. Sometimes, it ends mid-sentence.
In addition, this is an API endpoint. It needs to be hosted on AWS EC2 (Sashakt said this wouldn't be an issue).