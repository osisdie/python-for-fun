import subprocess


def main():
    """
    `python app_package/main.py`
    """
    subprocess.run(
        ['python', 'app_package/main.py'],
    )


def json1():
    """
    `python app_package/main.py --file res/employees1.json`
    """
    subprocess.run(
        ['python', 'app_package/main.py', '--file', 'res/employees1.json'],
    )


def json5():
    """
    `python app_package/main.py --file res/employees5.json`
    """
    subprocess.run(
        ['python', 'app_package/main.py', '--file', 'res/employees5.json'],
    )


def err_nodata():
    """
    `python app_package/main.py --file res/err_empty_data.json`
    """
    subprocess.run(
        ['python', 'app_package/main.py', '--file', 'res/err_empty_data.json'],
    )


def err_bad_src():
    """
    `python app_package/main.py --file res/err_bad_src.json`
    """
    subprocess.run(
        ['python', 'app_package/main.py', '--file', 'res/err_bad_src.json'],
    )


def err_bad_model():
    """
    `python app_package/main.py --file res/err_bad_model.json`
    """
    subprocess.run(
        ['python', 'app_package/main.py', '--file', 'res/err_bad_model.json'],
    )


def err_topmgr():
    """
    `python app_package/main.py --file res/err_missing_top_mgr.json`
    """
    subprocess.run(
        ['python', 'app_package/main.py', '--file', 'res/err_missing_top_mgr.json'],
    )


def err_infinite():
    """
    `python app_package/main.py --file res/err_inifinite_report_line.json`
    """
    subprocess.run(
        ['python', 'app_package/main.py', '--file', 'res/err_inifinite_report_line.json'],
    )
