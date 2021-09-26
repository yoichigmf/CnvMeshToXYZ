"""
/***************************************************************************
https://github.com/MIERUNE/japan-mesh-tool



MIERUNE/japan-mesh-tool is licensed under the

MIT License
A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.


Copyright 2020 MIERUNE Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 ***************************************************************************/
"""

# メッシュコード生成範囲
MINIMUM_LON = 122.00
MAXIMUM_LON = 154.00
MINIMUM_LAT = 20.00
MAXIMUM_LAT = 46.00

# メッシュ番号順で経緯度でのメッシュサイズを定義:(x, y)
FIRST_MESH_SIZE = (1, 2 / 3)

# メッシュ定義
# メッシュ次数と配列のインデックスは一致している
MESH_INFOS = [
    None,
    {"parent": 1, "ratio": 1},
    {"parent": 1, "ratio": 8},
    {"parent": 2, "ratio": 10},
    {"parent": 3, "ratio": 2},
    {"parent": 4, "ratio": 2},
    {"parent": 5, "ratio": 2},
    {"parent": 3, "ratio": 10},
    {"parent": 7, "ratio": 2},
    {"parent": 7, "ratio": 10},
    {"parent": 9, "ratio": 2},
]
