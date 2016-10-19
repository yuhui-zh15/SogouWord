使用方法 python downloadWordList.py 
如果加一个参数，则为下载该id的词库
例如：python downloadWordList.py 2 则会下载id为2的词库
也可以加一个参数，则为下载一个范围的词库
例如：python downloadWordList.py 2 5
则会下载id 2-4的词库
值得一提的是，如果该Id的词库不存在，会出现removing...

downloadIdName.py可以下载所有id的对应名字 对应运行结果为idName.txt，
由于词库是按照时间更新，可以直接从最新的id向高查找500左右判断是否有更新

