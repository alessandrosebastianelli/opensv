### Python Open Satellite Vision

This package contains functionalities to open, process and manipulate satellite data.

## Documentation
The documentation has been produced using [pdoc](https://pdoc.dev).

```python build_doc.py```

and it is available [here](https://alessandrosebastianelli.github.io/opensv/pyosv.html).

## Build and install the package

Move to opensv folder

opensv/  
├─ pyosv/  
├─ tests/  
├─ setup.py  
├─ LICENSE  
├─ README.md  
├─ docs  
├─ .gitignore  

and run

```python build_dist.py```

after building the wheels, you can install the library bu running

```pip install dist/pyosv-0.0.1-py3-none-any.whl```

**be aware that version (0.0.1) can change**.


## Upload to PyPi

```python3 -m twine upload dist/* --verbose```