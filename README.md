# jsonasobj2
[![Latest Version](https://img.shields.io/pypi/pyversions/jsonasobj2.svg)](https://pypi.python.org/pypi/jsonasobj2)
[![Pyversions](https://img.shields.io/pypi/v/jsonasobj2.svg)](https://pypi.python.org/pypi/jsonasobj2) 
[![License](https://pypip.in/license/jsonasobj2/badge.svg)](https://pypi.python.org/pypi/jsonasobj2/)
![](https://github.com/hsolbrig/jsonasobj2/workflows/Build/badge.svg)

## About

An extension to the python json library that represents the JSON as a first class python object rather than a straight dictionary. Contents can still be accessed using dictionary format.

## Installation

## Usage

```python
import jsonasobj2
from pprint import PrettyPrinter
pp = PrettyPrinter().pprint

test_json = """{
  "@context": {
    "name": "http://xmlns.com/foaf/0.1/name",
    "knows": "http://xmlns.com/foaf/0.1/knows",
    "menu": {
      "@id": "name:foo",
      "@type": "@id"
    }
  },
  "@id": "http://me.markus-lanthaler.com/",
  "name": "Markus Lanthaler",
  "knows": [
    {
      "name": "Dave Longley",
      "menu": "something",
      "modelDate" : "01/01/2015"
    }
  ]
}"""

py_obj = jsonasobj.loads(test_json)
py_obj.knows[0].extra = {'age': 17}
py_obj.knows.append(dict(name='Barack Obama'))
del py_obj.knows[0]['menu']
```

```python
print(py_obj.name)
```

produces

```
Markus Lanthaler
```

The `as_json` method will generate json strings

```python
print(jsonasobj.as_json(py_obj))
```

Produces:

```json
{
   "@context": {
      "name": "http://xmlns.com/foaf/0.1/name",
      "knows": "http://xmlns.com/foaf/0.1/knows",
      "menu": {
         "@id": "name:foo",
         "@type": "@id"
      }
   },
   "@id": "http://me.markus-lanthaler.com/",
   "name": "Markus Lanthaler",
   "knows": [
      {
         "name": "Dave Longley",
         "modelDate": "01/01/2015",
         "extra": {
            "age": 17
         }
      },
      {
         "name": "Barack Obama"
      }
   ]
}
```

## Runnable Examples

**See:** [Jupyter notebook](notebooks/readme.ipynb) for more examples

## History

The previous version of this was [jsonasobj](https://github.com/hsolbrig/jsonasobj)

v2 introduced breaking changes so a new repo and pypi distribution were made
