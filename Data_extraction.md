## Data Extraction Process 

Since the downloaded JSON file is too big that is why we need to extract certain data from each JSON file and then concat it. We can do that as following steps :

1. First we need to decompress the each JSON file as follow : 
```
zstd -d <filename>
```

2. Then run the python scripts : file_extraction.py : This python program as user to give input of the JSON uncompressed file and number of data the user want to extract. This python program can acept max 10 number of files. Later after extraction this python program can concatinate all the dataset into CSV file.

```$ ./file_extraction.py```

Output as below :

```
Note : You can extract Max of 10 file
Please enter the JSON file name : RS_2019-05
Please enter the number of data you want to extract : 10000

Input file : RS_2019-05 Data Count : 10000 Counter : 1

Your DataFrame Shape :  (10000, 106)

Do you want to extract another JSON file (Y/N) : Y

Please enter the JSON file name : RS_2019-06
Please enter the number of data you want to extract : 10000

Input file : RS_2019-06 Data Count : 10000 Counter : 2
Your DataFrame Shape :  (10000, 107)

Do you want to extract another JSON file (Y/N) : N

Your Final DataFrame Shape :  (20000, 108)

Do you want to save your DataFrame into CSV file (Y/N) : Y

Please Enter CSV file name : RS_2019_05_06.csv

CSV File generate sucessfully!! Done !! Thank You!!

```
