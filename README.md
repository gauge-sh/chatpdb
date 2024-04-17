[![image](https://img.shields.io/pypi/v/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://img.shields.io/pypi/l/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://img.shields.io/pypi/pyversions/chatpdb.svg)](https://pypi.python.org/pypi/chatpdb)
[![image](https://github.com/Never-Over/chatpdb/actions/workflows/ci.yml/badge.svg)](https://github.com/Never-Over/chatpdb/actions/workflows/ci.yml)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
# chatpdb
chat for your pdb

![](https://raw.githubusercontent.com/Never-Over/bridge/main/docs/runserver_demo.gif)

### Installation
```bash
pip install chatpdb
```
Ensure that you have `OPENAI_API_KEY` set in your environment.

### Use
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
Type `y "prompt"` to ask a question. 
```python3
> /Users/you/sample.py (9) test_function()
      8     
----> 9     import chatpdb; chatpdb.set_trace()
     10
ipdb> y "what does chatpdb do in this case?"
You are currently in a python debugger, etc.
```







### Advanced Usage (todo)

with context
python -m 
decorator

python -m 
CHAT_PDB..


pdb documentation
ipdb documentation