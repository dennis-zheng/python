// startDemo.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "Python.h"
#include <iostream>
#include <windows.h>

WCHAR * charToWchar(const char *s) 
{
	int w_nlen = MultiByteToWideChar(CP_ACP, 0, s, -1, NULL, 0);
	WCHAR *ret;
	ret = (WCHAR*)malloc(sizeof(WCHAR)*w_nlen);
	memset(ret, 0, sizeof(ret));
	MultiByteToWideChar(CP_ACP, 0, s, -1, ret, w_nlen);
	return ret;
}

char* WCharToChar(WCHAR *s) 
{
	int w_nlen = WideCharToMultiByte(CP_ACP, 0, s, -1, NULL, 0, NULL, false);
	char *ret = new char[w_nlen];
	memset(ret, 0, w_nlen);
	WideCharToMultiByte(CP_ACP, 0, s, -1, ret, w_nlen, NULL, false);
	return ret;
}

void initConfig(std::string& path, std::string& module)
{
	std::string strFile("./PythonServiceDS.ini");
	WCHAR* wFile = charToWchar(strFile.c_str());
	WCHAR tempChar[256] = { 0 };
	
	::GetPrivateProfileString(_T("service"), _T("mode"), _T("11"), tempChar, 256, wFile);
	char* strMode = WCharToChar(tempChar);
	int mode = atoi(strMode);
	//printf("mode=%d\n", mode);
	delete []strMode;

	memset(tempChar, 0, 256);
	char tmpModule[256] = { 0 };
	sprintf(tmpModule, "module_%d", mode);
	WCHAR* wTmpModule = charToWchar(tmpModule);
	::GetPrivateProfileString(_T("service"), wTmpModule, _T(""), tempChar, 256, wFile);
	char* strModule = WCharToChar(tempChar);
	//printf("module=%s\n", strModule);
	module = strModule;
	delete[]strModule;
	free(wTmpModule);

	memset(tempChar, 0, 256);
	::GetPrivateProfileString(_T("python"), _T("path"), _T(""), tempChar, 256, wFile);
	char* strPath = WCharToChar(tempChar);
	//printf("path=%s\n", strPath);
	path = strPath;
	delete[]strPath;
	
	free(wFile);
}

HMODULE GetSelfModuleHandle()
{
	MEMORY_BASIC_INFORMATION mbi;
	return ((::VirtualQuery(GetSelfModuleHandle, &mbi, sizeof(mbi)) != 0) ? (HMODULE)mbi.AllocationBase : NULL);
}

int main()
{
	std::string path = "";
	int path_abs = 0;
	std::string module = "";
	initConfig(path, module);

	Py_Initialize(); 
	std::string chdir = std::string("sys.path.append(\"") + path + "\")";
	printf("chdir = %s\n", chdir.c_str());

	std::string chmodule = std::string("import " + module);
	printf("chmodule = %s\n", chmodule.c_str());

	std::string chservice = std::string(module+ ".startService()");
	printf("chservice = %s\n", chservice.c_str());
	
	PyRun_SimpleString("import sys");
	PyRun_SimpleString(chdir.c_str());
	PyRun_SimpleString(chmodule.c_str());
	PyRun_SimpleString(chservice.c_str());
	
	Py_Finalize();
	return 0;
}
