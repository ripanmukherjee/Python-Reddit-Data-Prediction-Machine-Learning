## Installation and Importing different packages

There are couple of steps which need to follow first :

### Python Env

There are couple of python related steps which need to follow before to start data extraction process.

1. Assumming that you have python3 installed in the system and to check that run the following command

```
$ python3 --version
```

2. Installing pip for Python 3:

```
$ sudo apt update
```
```
$ sudo apt upgrade
```

```
$ sudo apt install python3-pip
```

3. Install pandas, numpy:

```
$ sudo apt-get install python3-pandas
```


```
$ sudo apt-get install python3-numpy
```

4. Install csv, json:

```
$ pip3 install python-csv
```


```
$ pip3 install jsonlib
```

### Unix Env

The data set in https://files.pushshift.io/reddit/submissions/ is very large and with having format of .zst. It is a Zstandard compress format of JSON file. To extract or decompress we need to install zstandard in Ubuntu shell as below :

1. This package is uploaded to PyPI at https://pypi.python.org/pypi/zstandard. So, to install this package:

```
$ pip3 install zstandard
```


```
$ sudo apt install zstd
```
