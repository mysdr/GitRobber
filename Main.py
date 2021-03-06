#!/usr/bin/env python
#coding:utf8

import os
import requests

# config-start
baseURL = "http://123.207.114.37/HackingBySearchEngine/.git/" # 注意后面添加.git和斜杠 TODO 以后对URL的容错性进行处理
# config-end

def makeDir(dicName):
	try:
		os.mkdir(dicName)
	except Exception as e:
		pass # 文件夹已存在

def makeDirs(path):
	try:
		os.makedirs(path)
	except Exception as e:
		pass # 文件夹已存在
	
def getIndexFileURL(baseURL):
	return ""

def getCommandReturn(command):
	output = os.popen(command)
	return output.read()

def downloadFile(url, fileName):
	response = requests.get(url) 
	file = open(fileName,"wb")
	file.write(response.content)
	file.close()

def getDoamin(baseURL):
	return baseURL.split("/")[2]

def getPath():
	return os.getcwd()

def init():
	os.system("")

def returnToParent():
	newPath = listLinker(os.getcwd().split("/")[0:-1])
	os.chdir(newPath)

def listLinker(splitLink):
	result = ""
	for li in splitLink:
		result += li + "/"
	return result

def getAllFileInfo(result):
	results = []
	# delete \n
	if result.endswith("\n"):
		result = result[0:-1]
	tempresults = result.split("\n")
	for tempresult in tempresults:
		filePath = tempresult.split("\t")[1] # 当文件名里面有tab的时候怎么处理
		temptempresult = tempresult.split("\t")[0]
		temparray = temptempresult.split(" ")
		number = temparray[0]
		sha1 = temparray[1]
		unknown = temparray[2]
		dic = {}
		dic['path'] = filePath
		dic['number'] = number
		dic['sha1'] = sha1
		dic['unknown'] = unknown
		results.append(dic)
	return results

def createFile(path, content):
	file = open(path, "wb")
	file.write(content)
	file.close()

# def formatePath(results):
# 	for result in results:
# 		path = result['path']
# 		print path

def createDics(results):
	for result in results:
		path = result['path']
		makedirs(path)


def getAllPaths(results):
	paths = []
	for result in results:
		path = result['path']
		if path.startswith("\"") and path.endswith("\""):
			path = path[1:-1]
			if "/" in path:
				temp = path.split("/")[0:-1]
				temppath = ""
				for t in temp:
					temppath += t + "/"
				paths.append(temppath)
			else:
				paths.append("./")
		else:
			if "/" in path:
				temp = path.split("/")[0:-1]
				temppath = ""
				for t in temp:
					temppath += t + "/"
				paths.append(temppath)
			else:
				paths.append("./")
	return paths


def getFilenames(results):
	filenames = []
	for result in results:
		path = result['path']
		if path.startswith("\"") and path.endswith("\""):
			path = path[1:-1]
			if "/" in path:
				temp = path.split("/")[-1]
				filenames.append(temp)
			else:
				filenames.append(path)
		else:
			if "/" in path:
				temp = path.split("/")[-1]
				filenames.append(temp)
			else:
				filenames.append(path)
	return filenames

def getSha1AndPath():
	sha1AndPath = []
	response = requests.get(baseURL + "objects")
	content = response.text
	print content


# # # 对每一个网站建立一个单独的文件夹
# domain = getDoamin(baseURL)
# makeDir(getPath() + "/" + domain)

# # # 建立本地.git文件夹
# newDir = getPath() + "/" + domain
# os.chdir(newDir)
# os.system("git init")

# # # # # 1. 下载index文件
# downloadFile(baseURL + "index", newDir + "/.git/index")

# # # # # 2. 解析git获取文件路径和hash的值
# indexResult = getCommandReturn("git ls-files --stage")

# # indexResult = indexResult[0:-4] # 去掉最后的两个\r\n
# results = getAllFileInfo(indexResult)
# paths = getAllPaths(results)

# # # # 3. 根据路径在本地建立相同的文件目录结构
# resultPath = set()
# for path in paths:
# 	resultPath.add(path)

# for path in resultPath:
# 	try:
# 		os.makedirs(path)
# 	except Exception as e:
# 		print e


# sha1s = []

# for result in results:
# 	sha1s.append(result['sha1'])

# filenames = getFilenames(results)



# # 4. 根据sha1和文件路径的对应关系 , 对文件进行下载和存储
# counter = 0
# for path in paths:
# 	print path + filenames[counter],sha1s[counter]
# 	# downloadFile(,path + sha1s[counter])
# 	# print path
# 	counter += 1


getSha1AndPath()