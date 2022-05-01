# Pascal triangle
You can read about Pascal triangle [here](https://en.wikipedia.org/wiki/Pascal%27s_triangle).

## Usage
```
usage: pascal_triangle.py [-h] [--no-color] [--no-superscript] degree
                                                                     
positional arguments:                                                
  degree

options:
  -h, --help        show this help message and exit
  --no-color        Remove color highlighting
  --no-superscript  Remove superscript symbols   
```
### Simple formula for 3 degree
```commandline
python pascal_triangle.py 3
```
Result: `(a - b)³ = a³ - 3a²b + 3ab² - b³`

### Remove superscript symbols
```commandline
python pascal_triangle.py 3 --no-superscript
```
Result: `(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3`
