### About

Collection of own [octave](http://www.gnu.org/software/octave/) snippets.

### Collection Description
* [jsontostruct](jsontostruct)
	- This small collection of scripts allows to convert JSON file into octave's structure. Very useful when a huge amount of parameters should be passed around between octave functions. Here is the format that is supported
	```
		{
			"variable1": {
                "value" : 1.0,
                "type"  : "float",
                "description": "Just a dummy variable"
			},
            "variable2": {
                "value" : [1.0 2.0 3.0 4.0],
                "type"  : "array",
                "description": "Just a dummy variables in one single array"
            },
            "variable3": {
                "value" : "RandomString",
                "type"  : "string",
                "description": "Just a dummy variable, type string"
            }
		}
	```

### Credits

* [Joel Feenstra](http://www.mathworks.com/matlabcentral/profile/authors/1286842-joel-feenstra) author of [JSON Parser](http://www.mathworks.com/matlabcentral/fileexchange/20565-json-parser)
* [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code)

### Author

* Viktor Dmitriyev
