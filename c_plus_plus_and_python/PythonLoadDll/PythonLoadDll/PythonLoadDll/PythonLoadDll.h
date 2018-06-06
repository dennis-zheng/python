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
PYTHONLOADDLL_EXPORTS int PythonLoadDll_process(long handle, int index, const char* buffer, const int size, void* structInfo);

#endif//__PYTHON_LOAD_DLL_H__
