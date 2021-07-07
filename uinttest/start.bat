set TIME_T=%time: =0%
set TEST_REPORT=%~dp0report/%date:~0,4%%date:~5,2%%date:~8,2%_%TIME_T:~0,2%%TIME_T:~3,2%%TIME_T:~6,2%


python test_var.py %TEST_REPORT%
python send_test_report.py %TEST_REPORT%