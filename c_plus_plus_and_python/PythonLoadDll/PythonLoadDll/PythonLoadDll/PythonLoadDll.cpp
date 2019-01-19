// FaceFilteringDS.cpp : 定义 DLL 应用程序的导出函数。
//

#include "stdafx.h"
#include "PythonLoadDll.h"
#include <mutex>
#include <map>

typedef struct _tagStructInfo
{
	int id;
	float idF;
} StructInfo;

typedef struct _tagStructBuf
{
	char buf[256];
	int size;
} StructBuf;

typedef struct _tagStructMultiBuf
{
	char* buf[100];
	int size[100];
	int count;
} StructMultiBuf;

class Obj
{
public:
	Obj() { index = 0; }
	~Obj() {}
	
public:
	int index; 
};

std::map<long, Obj*>  mapObj_;
std::mutex  mutexObj_;

Obj* GetObj(long handle)
{
	Obj* obj = NULL;
	mutexObj_.lock();
	auto it = mapObj_.find(handle);
	if (it != mapObj_.end())
	{
		obj = it->second;
	}
	else
	{
		obj = new Obj;
		mapObj_[handle] = obj;
	}
	mutexObj_.unlock();
	return obj;
}

void RemoveObj(long handle)
{
	mutexObj_.lock();
	auto it = mapObj_.find(handle);
	if (it != mapObj_.end())
	{
		delete it->second;
		mapObj_.erase(it);
	}
	mutexObj_.unlock();
}

PYTHONLOADDLL_EXPORTS int PythonLoadDll_init(long handle)
{
	return GetObj(handle)->index;
}

PYTHONLOADDLL_EXPORTS void PythonLoadDll_uninit(long handle)
{
	RemoveObj(handle);
}

PYTHONLOADDLL_EXPORTS int PythonLoadDll_process(long handle, int index, const char* buffer, const int size)
{
	printf("%s handle=%d, index=%d, buffer=%s, size=%d\n", __FUNCTION__, handle, index, buffer, size);
	return GetObj(handle)->index = index;;
}

PYTHONLOADDLL_EXPORTS int PythonLoadDll_processInfo(long handle, int index, void* obj)
{
	StructInfo* info = (StructInfo*)obj;
	printf("%s 0x%p handle=%d, index=%d, id=%d, idF=%f\n", __FUNCTION__, info, handle, index, info->id, info->idF);
	return GetObj(handle)->index = index;
}

PYTHONLOADDLL_EXPORTS int PythonLoadDll_processBuf(long handle, int index, void* obj)
{
	StructBuf* info = (StructBuf*)obj;
	printf("%s 0x%p handle=%d, index=%d, buf=%s, size=%d\n", __FUNCTION__, info, handle, index, info->buf, info->size);
	return GetObj(handle)->index = index;
}

PYTHONLOADDLL_EXPORTS int PythonLoadDll_processMultiBuf(long handle, int index, void* obj)
{
	StructMultiBuf* info = (StructMultiBuf*)obj;
	for (int i = 0; i < info->count; i++)
	{
		printf("%s 0x%p handle=%d, index=%d, buf=%s, size=%d, i=%d\n", __FUNCTION__, info, handle, index, info->buf[i], info->size[i], i);
	}
	
	return GetObj(handle)->index = index;
}

PYTHONLOADDLL_EXPORTS int PythonLoadDll_processOut(long handle, int index, char* buffer, int* size)
{
	char* msg = "PythonLoadDll_processOut";
	*size = strlen(msg);
	memcpy(buffer, msg, *size);
	return GetObj(handle)->index = index;
}

PYTHONLOADDLL_EXPORTS int PythonLoadDll_processBufOut(long handle, int index, void* obj)
{
	StructBuf* info = (StructBuf*)obj;
	char* msg = "PythonLoadDll_processBufOut";
	info->size = strlen(msg);
	memcpy(info->buf, msg, info->size);
	return GetObj(handle)->index = index;
}

PYTHONLOADDLL_EXPORTS int PythonLoadDll_processMultiBufOut(long handle, int index, void* obj)
{
	StructMultiBuf* info = (StructMultiBuf*)obj;
	info->count = 5;
	char* msg = "PythonLoadDll_processMultiBufOut";
	for (int i = 0; i < info->count; i++)
	{
		sprintf(info->buf[i], "%s %d", msg, i);
		info->size[i] = strlen(info->buf[i]);
		//printf("%s %d\n", __FUNCTION__, i);
	}
	//for (int i = 0; i < 100; i++)
	//{
	//	printf("%s %d 0x%p\n", __FUNCTION__, i, info->buf[i]);
	//}
	//for (int i = 0; i < info->count; i++)
	//{
	//	printf("%s %s %d 0x%p\n", __FUNCTION__, info->buf[i], info->size[i], info->buf[i]);
	//}
	return GetObj(handle)->index = index;
}

/*
	当用python调用c++是，接口返回数据最好转换为int，用其他类型，会降低效率；
	可以做如下优化（python端代码，返回结果需除以10000）
	PYTHONLOADDLL_EXPORTS int PythonLoadDll_processRe(long handle, int index)
	{
		return 22.33*10000;
	}
*/
PYTHONLOADDLL_EXPORTS float PythonLoadDll_processRe(long handle, int index)
{
	return 22.33;
}