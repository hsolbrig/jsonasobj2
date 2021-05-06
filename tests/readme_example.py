import jsonasobj
from jsonasobj._jsonobj import as_json, as_dict

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
print(py_obj.name)
print(py_obj['name'])
print(py_obj.knows[0].name)
print(py_obj['@context'].name)
print(as_json(py_obj))
print(as_dict(py_obj))
'''
Result:

Markus Lanthaler
Markus Lanthaler
Dave Longley
http://xmlns.com/foaf/0.1/name
{
   "@id": "http://me.markus-lanthaler.com/",
   "knows": [
      {
         "extra": {
            "age": 17
         },
         "name": "Dave Longley",
         "modelDate": "01/01/2015"
      },
      {
         "name": "Barack Obama"
      }
   ],
   "name": "Markus Lanthaler",
   "@context": {
      "menu": {
         "@id": "name:foo",
         "@type": "@id"
      },
      "knows": "http://xmlns.com/foaf/0.1/knows",
      "name": "http://xmlns.com/foaf/0.1/name"
   }
}
{'@id': 'http://me.markus-lanthaler.com/', 'knows': [{'modelDate': '01/01/2015', 'extra': {'age': 17}, 'name': 'Dave Longley'}, {'name': 'Barack Obama'}], 'name': 'Markus Lanthaler', '@context': {'menu': {'@id': 'name:foo', '@type': '@id'}, 'knows': 'http://xmlns.com/foaf/0.1/knows', 'name': 'http://xmlns.com/foaf/0.1/name'}}

'''
