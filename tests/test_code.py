"""実行方法
本ディレクトリ上で以下のコマンド実行
pytest test_code.py
"""
import os,sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sample import add_val,mul_val,sub_val


# ===test関数を一通り書く===
def test_sample_add():
    result=add_val(1,2)
    assert result == 3
    result=add_val(-3,-2)
    assert result == -5
    result=add_val(0,100.2)
    assert result == 100.2

def test_sample_mul():
    result=mul_val(1,2)
    assert result == 2
    result=mul_val(-3,-2)
    assert result == 6
    result=mul_val(0,100.2)
    assert result == 0

def test_sample_sub():
    result=sub_val(1,2)
    assert result == -1
    result=sub_val(-3,-2)
    assert result == -1
    result=sub_val(0,100.2)
    assert result == -100.2