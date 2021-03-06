# メッシュコード生成範囲
MINIMUM_LON = 122.00
MAXIMUM_LON = 154.00
MINIMUM_LAT = 20.00
MAXIMUM_LAT = 46.00

# メッシュ番号順で経緯度でのメッシュサイズを定義:(x, y)
FIRST_MESH_SIZE = (1, 2 / 3)

# メッシュ定義
# メッシュ次数と配列のインデックスは一致している
#  細分メッシュ用追加   Y.Kayama  2021/10/12
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
    {"parent": 3, "ratio": 10},   
    {"parent": 3, "ratio": 20},
    {"parent": 3, "ratio": 25},
    {"parent": 3, "ratio": 40},
    {"parent": 3, "ratio": 50},  
    {"parent": 3, "ratio": 80},
    {"parent": 3, "ratio": 100},
    {"parent": 3, "ratio": 200},
    {"parent": 3, "ratio": 250},
    {"parent": 3, "ratio": 400},
    {"parent": 3, "ratio": 500},
    {"parent": 3, "ratio": 800},
    {"parent": 3, "ratio": 1000},
]
