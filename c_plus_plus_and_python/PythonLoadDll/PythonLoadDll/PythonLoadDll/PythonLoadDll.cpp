// FaceFilteringDS.cpp : 定义 DLL 应用程序的导出函数。
//

#include "stdafx.h"
#include "PythonLoadDll.h"
#include <mutex>
#include <map>

struct StructInfo
{
	int id;
	float idF;
	char* buf;
	int size;
};

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

PYTHONLOADDLL_EXPORTS int PythonLoadDll_process(long handle, int index, const char* buffer, const int size, void* structInfo)
{
	StructInfo* info = (StructInfo*)structInfo;
	info->id = handle;
	info->idF = float(handle) + 0.55;
	info->size = size;
	sprintf(info->buf, buffer, info->size);

	printf("PythonLoadDll_process id=%d, test1=%f, test2=%s, size=%d\n", info->id, info->idF, info->buf, info->size);
	printf("PythonLoadDll_process size=%d, buffer=%s\n", size, buffer);
	return GetObj(handle)->index = index;
}