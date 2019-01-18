#ifndef __PYTHON_LOAD_DLL_H__
#define __PYTHON_LOAD_DLL_H__

#ifdef WIN64
#ifdef PYTHONLOADDLL_EXPORTS
#define PYTHONLOADDLL_EXPORTS extern "C"  __declspec(dllexport) 
#else
#define PYTHONLOADDLL_EXPORTS extern "C"  __declspec(dllimport) 
#endif
#else
#define PYTHONLOADDLL_EXPORTS
#endif

PYTHONLOADDLL_EXPORTS int PythonLoadDll_init(long handle);
PYTHONLOADDLL_EXPORTS void PythonLoadDll_uninit(long handle);
PYTHONLOADDLL_EXPORTS int PythonLoadDll_process(long handle, int index, const char* buffer, const int size);
PYTHONLOADDLL_EXPORTS int PythonLoadDll_processInfo(long handle, int index, void* obj);
PYTHONLOADDLL_EXPORTS int PythonLoadDll_processBuf(long handle, int index, void* obj);
PYTHONLOADDLL_EXPORTS int PythonLoadDll_processMultiBuf(long handle, int index, void* obj);

PYTHONLOADDLL_EXPORTS int PythonLoadDll_processOut(long handle, int index, char* buffer, int* size);
PYTHONLOADDLL_EXPORTS int PythonLoadDll_processBufOut(long handle, int index, void* obj);
PYTHONLOADDLL_EXPORTS int PythonLoadDll_processMultiBufOut(long handle, int index, void* obj);
PYTHONLOADDLL_EXPORTS float PythonLoadDll_processRe(long handle, int index);

#endif//__PYTHON_LOAD_DLL_H__
