"""conftest.pyを記述することで、下層の任意のディレクトリにある
testコード全体に対しての設定を適用できます。
"""

print("===Processing by conftest.py===")
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
print("===Processing by conftest.py completed===")
