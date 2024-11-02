# Github Action を使ってみるリポジトリ

* 設定方法
```./.github/workflows/*.yml```を配置(今回は```test.yml```)という名前。


```yml:./github/workflows/test.yml
name: Python Package Test
on:
  push:
env:
  PYTHON_VERSION: '3.12'
jobs:
  test_jobs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest --cov=sample tests/
```
これをリポジトリ内に置くだけでgithub上での操作なしでRunnerの設定が環境する。