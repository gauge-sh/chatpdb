[![image](https://img.shields.io/pypi/v/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://img.shields.io/pypi/l/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://img.shields.io/pypi/pyversions/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://github.com/Never-Over/chatpdb/actions/workflows/ci.yml/badge.svg)](https://github.com/Never-Over/chatpdb/actions/workflows/ci.yml)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
# chatpdb

`chatpdb` is a drop-in replacement for [ipdb](https://github.com/gotcha/ipdb) or [pdb](https://docs.python.org/3/library/pdb.html) that lets you ask questions while debugging.

![](https://raw.githubusercontent.com/Never-Over/chatpdb/main/assets/chatpdb_demo.gif)

`chatpdb` meets you where you are - AI tooling that's only invoked when you need it.

## Installation
```bash
pip install chatpdb
```
Ensure that you have `OPENAI_API_KEY` set in your environment.
```bash
export OPENAI_API_KEY=...```

## Usage
In your code:
```python3
import chatpdb; chatpdb.set_trace()
```
Simply type `y` to receive a summary of the current code and stack trace.
```python3
> /Programming/test-chatpdb/lib.py(2)echo_platform()
      1 def echo_platform(platform: str):
----> 2     print("You are running on:" + platform)
      3
ipdb> y 
The exception occurred because the function `echo_platform` tries to concatenate the string "You are running on:" with the `platform` variable, which is `None`. [...]
```

Type `y "prompt"` to ask a question. 

```python3
> /Programming/test-chatpdb/lib.py(2)echo_platform()
      1 def echo_platform(platform: str):
----> 2     print("You are running on:" + platform)
      3
ipdb> y "Why is platform coming through as None?"
The variable `platform` is coming through as `None` because the environment variable `"PLATFORM"` is not set in your system's environment variables. [...]
```


## How does it work?
`chatpdb` uses the OpenAI API to generate responses to your questions. It uses the `gpt-4-turbo` model by default.

`chatpdb` will automatically include relevant context from the current frame and stack trace, as well as
exception information if one has been raised.


### Advanced Usage

Just like [ipdb](https://github.com/gotcha/ipdb) and [pdb](https://docs.python.org/3/library/pdb.html), `chatpdb` supports many different entrypoints.

Running code:
```python3
import chatpdb; chatpdb.run('print("hello")')
import chatpdb; chatpdb.runcall(lambda x: x + 1, 1)
```
As a decorator:
```python3

@chatpdb.cex
def sample_cex_function():
    raise # any exception within the decorated function will trigger chatpdb
```
As a context manager:
```python3
with chatpdb.launch_chatpdb_on_exception():
    raise # any exception within the with block will trigger chatpdb
```
On files:
```bash
python3 -m chatpdb file.py
```
post-mortem support:
```python3
chatpdb.pm()
```

See the documentation of [ipdb](https://github.com/gotcha/ipdb) or [pdb](https://docs.python.org/3/library/pdb.html) for the full api.

### Configuration
You can use more specific environment variables to configure an OpenAI key and preferred model
for chatpdb. The following environment variables are supported:
- `CHAT_PDB_OPENAI_API_KEY`: Your OpenAI API key
- `CHAT_PDB_OPENAI_MODEL`: The model to use for chatpdb. Default is 'gpt-4-turbo'
