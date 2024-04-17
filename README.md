[![image](https://img.shields.io/pypi/v/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://img.shields.io/pypi/l/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://img.shields.io/pypi/pyversions/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://github.com/Never-Over/chatpdb/actions/workflows/ci.yml/badge.svg)](https://github.com/Never-Over/chatpdb/actions/workflows/ci.yml)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
# chatpdb
chatpdb is an extension to [ipdb](https://github.com/gotcha/ipdb) that lets you ask questions while debugging your code.

![](https://raw.githubusercontent.com/Never-Over/bridge/main/docs/runserver_demo.gif)

## Installation
```bash
pip install chatpdb
```
Ensure that you have `OPENAI_API_KEY` set in your environment.

## Usage
In your code:
```python3
import chatpdb; chatpdb.set_trace()
```
chatpdb extends your python debugger to allow you to ask questions to chatgpt. Simply type `y` to receive a summary of the current code and stack trace.
```python3
> /Users/you/sample.py (9) test_function()
      8     
----> 9     import chatpdb; chatpdb.set_trace()
     10
ipdb> y
You are currently in a python debugger, etc.
```
Type `y [prompt]` to ask a question. 
```python3
> /Users/you/sample.py (9) test_function()
      8     
----> 9     import chatpdb; chatpdb.set_trace()
     10
ipdb> y what does chatpdb do in this case?
You are currently in a python debugger, etc.
```


## Advanced

### Usage
[ipdb]() and [pdb]() support many different entrypoints which `chatpdb` also supports. 
```python3
import chatpdb; chatpdb.pm()
```
```python3
import chatpdb; chatpdb.run('print("hello")')
```
```python3
import chatpdb; chatpdb.runcall(lambda x: x + 1, 1)
```
```python3
# chatpdb will launch on exception
# @chatpdb.iex is also supported
@chatpdb.cex
def sample_cex_function():
    raise
```
```python3
def sample_with_function():
    with chatpdb.launch_chatpdb_on_exception(): # or chatpdb.launch_ipdb_on_exception()
        raise
```

### Configuration
You can use more specific environment variables to configure an OpenAI key and preferred model
for chatpdb. The following environment variables are supported:
- `CHAT_PDB_OPENAI_API_KEY`: Your OpenAI API key
- `CHAT_PDB_OPENAI_MODEL`: The model to use for chatpdb. Default is 'gpt-4-turbo'
